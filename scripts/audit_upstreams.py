#!/usr/bin/env python3
"""Record public skill-source versions without executing any upstream content."""

from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "skill-sources.json"
LOCK_PATH = ROOT / "upstream-lock.json"
API_ROOT = "https://api.github.com"


def get_json(path: str) -> dict[str, Any]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "operating-aip-content-system-auditor",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(f"{API_ROOT}{path}", headers=headers)
    retryable_http = {429, 500, 502, 503, 504}
    for attempt in range(3):
        try:
            with urlopen(request, timeout=30) as response:
                return json.load(response)
        except HTTPError as error:
            detail = error.read().decode("utf-8", errors="replace")
            if error.code in retryable_http and attempt < 2:
                time.sleep(2**attempt)
                continue
            raise RuntimeError(f"GitHub API {error.code} for {path}: {detail}") from error
        except URLError as error:
            if attempt < 2:
                time.sleep(2**attempt)
                continue
            raise RuntimeError(f"Network error for {path}: {error.reason}") from error

    raise RuntimeError(f"Unexpected retry exhaustion for {path}")


def commit_sha(repository: str) -> str:
    result = get_json(f"/repos/{repository}/commits/HEAD")
    return result["sha"]


def skill_blob_sha(repository: str, skill_path: str) -> str:
    encoded_path = quote(skill_path, safe="/")
    result = get_json(f"/repos/{repository}/contents/{encoded_path}?ref=HEAD")
    return result["sha"]


def collect(config: dict[str, Any]) -> dict[str, Any]:
    tracked = []
    for item in config["tracked_repositories"]:
        repository = item["repository"]
        tracked.append(
            {
                "repository": repository,
                "mode": item["mode"],
                "commit": commit_sha(repository),
                "skills": [
                    {"path": path, "blob_sha": skill_blob_sha(repository, path)}
                    for path in item["skills"]
                ],
            }
        )

    upstreams = []
    for item in config["upstreams"]:
        upstreams.append(
            {
                "repository": item["repository"],
                "integration_policy": item["integration_policy"],
                "reason": item["reason"],
                "commit": commit_sha(item["repository"]),
            }
        )

    return {
        "schema_version": config["schema_version"],
        "tracked_repositories": tracked,
        "upstreams": upstreams,
    }


def main() -> int:
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    lock = collect(config)
    rendered = json.dumps(lock, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    previous = LOCK_PATH.read_text(encoding="utf-8") if LOCK_PATH.exists() else None

    if rendered == previous:
        print("Skill source audit: no changes.")
        return 0

    LOCK_PATH.write_text(rendered, encoding="utf-8")
    print("Skill source audit: lock file updated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
