# Artifact Contracts

## AIP Brief

```markdown
# AIP Brief
- Audience:
- Person — relevant background and credible lived experience:
- Offer — useful knowledge, service, product, or trust value under test:
- Scene — public content, private conversion, or other approved path:
- Account promise in one reader-facing sentence:
- Account signals — name, bio, avatar direction, and topic boundary:
- Point of view:
- Credible proof and missing proof:
- Stories, judgments, and boundaries that can appear in content:
- Topics to own / topics to avoid:
- Monetization hypothesis and qualification/policy evidence needed:
- Claims that need verification:
- Next validation action:
```

## Content Evidence Packet

```markdown
# Content Evidence Packet — YYYY-MM-DD-slug

## Reader problem
- Audience segment:
- Situation:
- Outcome needed:

## Original angle
- Account-specific point of view:
- Experience, case, or test that makes it credible:

## Source ledger
| Claim or pattern | Source URL or file | Access date | Status | Use |
| --- | --- | --- | --- | --- |

## Evidence and assets
- Evidence:
- Asset path and rights status:
- Missing evidence:

## Platform plan
- Article promise:
- Video hook and core tension:
- Selected final HTML lane:
- Human decision required:
```

`needs-evidence` and `needs-human-decision` are valid states. Never convert them into publication-ready claims.

## Benchmark Card

```markdown
# Benchmark Card — source / date
- Fit to our reader and positioning:
- Account-level learning:
- Article-level learning:
- Element-level learning:
- Reader-visible notes: title, opening, flow, usable value, action:
- Deeper notes: emotion, insight, action trigger:
- Original transformation: audience/context/evidence/voice:
- Material that cannot be reused:
- Source and access date:
```

## Topic Candidate Card

```markdown
# Topic Candidate — YYYY-MM-DD
- Reader's observed question:
- Source: own test | consented reader question | benchmark pattern | primary source:
- Account-specific angle:
- Useful outcome promised:
- Evidence available and missing:
- Story, failure, judgment, or limit that makes it ours:
- Originality and rights decision:
- Status: ready | needs-evidence | needs-human-decision
```

## Article Review

```markdown
## Article Review
- Reader and promised outcome are explicit:
- Opening mode: verified outcome | verified value | reader pain | honest curiosity:
- Account-specific evidence is present:
- Reader receives a usable method, decision, or stated limit:
- Personal story serves the topic rather than displacing it:
- Claims match the source ledger:
- Benchmark structure was transformed:
- No unsupported earnings, performance, or product claim:
- One final HTML lane is selected:
- Asset rights and SVG compatibility are resolved:
- Human decision: approve | revise | hold
```

## Publishing-Lane Handoff

```markdown
# Publishing-Lane Handoff — YYYY-MM-DD-slug
- Approved source Markdown:
- Packet and article-review decision:
- Selected final HTML lane:
- Other lanes deliberately not used:
- Theme/layout decision:
- Validation and preview result:
- HTML output path:
- Asset and cover rights:
- Requested external action: none | human paste | upload | create draft
- `md2wechat inspect` target and blockers (required only for upload/draft):
- Human decision and timestamp:
```

## Video Handoff

```json
{
  "packet": "research/YYYY-MM-DD-slug",
  "lane": "tool-tutorial | product-explainer | opinion-explainer | data-explainer | book-summary",
  "hook": "",
  "coreTension": "",
  "durationSec": 60,
  "dimensions": "1080x1920 vertical | project-specific",
  "claims": [{"text": "", "evidence": "", "status": "verified"}],
  "scenes": [{"purpose": "", "voiceover": "", "caption": "", "visual": "", "assetRights": ""}],
  "engine": "hyperframes-validation | remotion-production",
  "humanReview": "sample direction | still frame | final MP4",
  "renderChecks": ["caption safe zone", "overflow", "asset path", "contrast", "timing", "cover", "duration"],
  "output": "outputs/"
}
```
