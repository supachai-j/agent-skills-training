# EN → TH glossary

Running list of decisions made while translating technical content. Reference
this so the same English term gets the same Thai treatment across pages.

> **Convention:** column 1 = English source · column 2 = how to handle in Thai prose · column 3 = optional Thai gloss for first-use only

| EN term | Handle as | Optional gloss (first use) |
|---|---|---|
| Skill / Agent Skill | `<code>Skill</code>` (proper noun) | — |
| skill (lowercase, generic) | "skill" (italic or `<code>`) | "ความสามารถเฉพาะ" |
| frontmatter | `<code>frontmatter</code>` | — |
| YAML | YAML | — |
| markdown | markdown | — |
| description | "description" (`<code>` if frontmatter field) or "คำอธิบาย" | — |
| name (frontmatter field) | `<code>name</code>` | — |
| field (frontmatter) | "ฟิลด์" or `<code>field</code>` | — |
| validation | "validation" or "การตรวจสอบ" | — |
| repo / repository | "repo" / "repository" | — |
| commit (verb) | "commit" | — |
| commit (noun) | "commit" | — |
| pull request / PR | "PR" / "pull request" | — |
| branch | "branch" | — |
| merge | "merge" / "รวมเข้า" | — |
| deploy / deployment | "deploy" / "นำขึ้นใช้งาน" | — |
| publish | "publish" / "เผยแพร่" | — |
| release | "release" | — |
| pipeline | "pipeline" | "กระบวนการอัตโนมัติ" |
| workflow | "workflow" | "กระบวนการทำงาน" |
| process (noun) | "กระบวนการ" | — |
| token (LLM) | "token" | — |
| context window | "context window" | "หน้าต่างบริบท" |
| prompt | "prompt" | "คำสั่งเริ่มต้น" |
| subagent | "subagent" | — |
| MCP / Model Context Protocol | "MCP" | — |
| progressive disclosure | "progressive disclosure" | "เปิดเผยทีละชั้น" |
| anti-pattern | "anti-pattern" | "รูปแบบที่ควรเลี่ยง" |
| best practice | "best practice" | "แนวปฏิบัติที่ดี" |
| evaluation / eval | "eval" / "evaluation" | "การทดสอบประเมิน" |
| trigger (noun, agent) | "trigger" | "การกระตุ้นใช้" |
| trigger (verb) | "ทริกเกอร์" or "กระตุ้น" | — |
| activation | "activation" | "การเปิดใช้" |
| client (agent client) | "client" | "เครื่องมือ" |
| host | "host" | — |
| sandbox | "sandbox" | — |
| runtime | "runtime" | "ขณะรัน" |
| spec / specification | "spec" / "specification" | "ข้อกำหนด" |
| open standard | "open standard" | "มาตรฐานเปิด" |
| ecosystem | "ecosystem" | "ระบบนิเวศ" |
| cross-client | "cross-client" | "ใช้ข้าม client" |
| portability | "portability" | "ความเคลื่อนย้ายได้" |
| canonical | "canonical" | "หลัก / ที่ยึดถือเป็นหลัก" |
| frontmatter rules | "กฎของ frontmatter" | — |
| description rules | "กฎของ description" | — |
| security model | "โมเดลความปลอดภัย" | — |
| threat model | "threat model" | "แบบจำลองภัยคุกคาม" |
| audit | "audit" | "ตรวจสอบ" |
| permission | "permission" | "สิทธิ์" |
| trust boundary | "trust boundary" | "ขอบเขตความน่าเชื่อถือ" |
| feedback loop | "feedback loop" | "วงจรการปรับปรุง" |
| iterate | "iterate" | "วนซ้ำ" |
| hands-on | "hands-on" | "ลงมือทำจริง" |
| lab / workshop | "Lab" / "Workshop" | — |
| takeaway | "ใจความสำคัญ" | — |
| use case | "use case" | "กรณีใช้งาน" |
| edge case | "edge case" | "กรณีพิเศษ/ซอกมุม" |
| Coming soon | "Coming soon" / "เร็วๆ นี้" | — |
| Drafting | "Drafting" / "กำลังเขียน" | — |
| Read more | "อ่านต่อ" | — |
| Back to top | "↑ กลับด้านบน" | — |
| Theme (UI) | "Theme" / "ธีม" | — |
| Light / Dark mode | "โหมดสว่าง / โหมดมืด" | — |

## How to extend this

When you encounter a new technical term not in the table:

1. Check if there's a settled Thai term in major Thai tech communities
   (LongdoDict, Thai dev Twitter, Wikipedia Thai)
2. If none — keep the English (Rule 2) and optionally gloss on first use
3. Add the decision to this file so the next translator stays consistent

## Don't translate

These should NEVER be translated, regardless of context:

- File names: `SKILL.md`, `index.html`, `README.md`
- Code: identifiers, syntax, error messages
- URLs / paths
- Tool names: `gh`, `git`, `curl`, `bash`, `npm`
- Library names: `pdfplumber`, `reveal.js`, `Inter`, `Noto Sans Thai`
- Brand names: `Anthropic`, `Claude`, `GitHub`, `OpenAI`
- Spec names: `agentskills.io`, `MCP`, `JSON`, `YAML`, `OAuth`
