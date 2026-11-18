# LinkedIn Profile Optimizer Skill (2026 AI & StorySelling Edition)

A portable, repeatable AI skill for **Claude Code**, **Claude Desktop / claude.ai**, and **Google Antigravity** that audits, scores, and rewrites LinkedIn profiles using:
- **The 2026 Unified AI Algorithm Rules** (the 5 Core Author Data Fields, semantic skill clustering, and the 265-character AI Recruiter summary hook)
- **The 5-Pillar Audit Scoring Rubric** (1–10 weighted scorecard)
- **The 5-Paragraph Brand StorySelling Framework** (Hook → Contrarian Point of View → Quantified Proof Pillars → Personality → CTA)
- **Seniority & Archetype Calibration** (automatically adapts tone across **Tier A: Boardroom / Chair / NED / C-Suite**, **Tier B: Founder / B2B Consultant**, and **Tier C: Career Changer / Job Seeker**)

---

## Repository Structure

```text
linkedin-profile-optimizer/
├── SKILL.md                                      # Main skill workflow instructions
├── references/
│   ├── 2026_ai_audit_rules.md                    # 2026 LinkedIn LLM ranking & 5-pillar rubric
│   └── storyselling_and_content_playbook.md      # 10 foundational questions, 5-part About arc & content cadence
├── scripts/
│   └── parse_linkedin_exports.py                 # Python parser for LinkedIn AggregateAnalytics_*.xlsx files
├── .agents/skills/linkedin-profile-optimizer/    # Auto-discovered by Antigravity when opened as a workspace
├── .claude/skills/linkedin-profile-optimizer/    # Auto-discovered by Claude Code when opened as a workspace
├── linkedin-profile-optimizer-claude-skill.zip   # Ready-to-upload .zip package for Claude Desktop / claude.ai
├── install.ps1                                   # 1-click global installer for Windows (Claude + Antigravity)
└── install.sh                                    # 1-click global installer for macOS / Linux (Claude + Antigravity)
```

---

## Quick Start (3 Ways to Use)

### Option 1: Install Globally on Another Machine (Claude Code & Antigravity)

Clone the repository and run the installer script for your OS:

**Windows (PowerShell):**
```powershell
git clone https://github.com/Taitai54/linkedin-profile-optimizer.git
cd linkedin-profile-optimizer
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

**macOS / Linux:**
```bash
git clone https://github.com/Taitai54/linkedin-profile-optimizer.git
cd linkedin-profile-optimizer
chmod +x install.sh && ./install.sh
```

This installs the skill globally into:
- `~/.claude/skills/linkedin-profile-optimizer` (for **Claude Code**)
- `~/.gemini/config/skills/linkedin-profile-optimizer` (for **Google Antigravity**)

---

### Option 2: Upload to Claude Desktop or claude.ai (Web)

1. Download [`linkedin-profile-optimizer-claude-skill.zip`](./linkedin-profile-optimizer-claude-skill.zip) from this repo.
2. In Claude Desktop or claude.ai, go to **Settings > Capabilities > Skills** (or **Customize > Skills**).
3. Click **Upload Skill** and select `linkedin-profile-optimizer-claude-skill.zip`.

---

### Option 3: Use Directly in This Repo Folder

1. Export your current LinkedIn profile to PDF (**Desktop Profile > More > Save to PDF**).
2. *(Optional)* Export your LinkedIn analytics (**Profile Analytics > Content Analytics > Export `.xlsx`**).
3. Drop your `Profile.pdf` (and optional `.xlsx` file) into your working folder (ignored by `.gitignore` so your private data is never committed).
4. Open the folder in **Claude** or **Antigravity** and prompt:
   > *"Audit and rewrite my LinkedIn profile using the linkedin-profile-optimizer skill."*

---

## Prerequisites for the Analytics Parser Script

If you include LinkedIn `.xlsx` analytics exports, the helper script uses `openpyxl`:
```bash
pip install openpyxl
```
