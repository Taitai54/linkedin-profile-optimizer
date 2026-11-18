---
name: linkedin-profile-optimizer
description: >-
  Audits, scores, and rewrites LinkedIn profiles using the 2026 Unified AI
  Algorithm Rules, the 5-Pillar Audit Rubric, and the 5-Paragraph Brand
  StorySelling Framework. Use this skill whenever the user wants to audit,
  update, rewrite, or improve a LinkedIn profile (for themselves, an executive,
  a board member, a founder, or a job seeker) from a LinkedIn Profile PDF,
  analytics export, or CV.
---

# LinkedIn Profile Optimizer (2026 AI & StorySelling Edition)

This skill executes a repeatable, end-to-end LinkedIn profile audit and step-change rewrite. It combines LinkedIn's 2026 unified LLM ranking signals with human conversion psychology and brand storytelling.

---

## Step 1: Ingest Inputs & Run the Analytics Parser

1. Check the workspace folder for:
   - **LinkedIn Profile PDF** (typically `Profile.pdf` saved from LinkedIn desktop) or CV/resume files.
   - **LinkedIn Analytics Exports** (`AggregateAnalytics_*.xlsx`).
   - Any supporting notes, playbooks, or target role descriptions.
2. Read the Profile PDF using `read_file` and run the bundled parser script on the workspace directory to extract follower demographics, impression velocity, and hygiene flags:
   ```powershell
   python ".agents/skills/linkedin-profile-optimizer/scripts/parse_linkedin_exports.py" "."
   ```

---

## Step 2: Calibrate to Seniority & Strategic Goal (Do Not Skip)

Generic LinkedIn advice ruins high-status profiles. Before rewriting any copy, determine (or ask the user via `ask_question` if not yet clear) three calibration parameters:

1. **Archetype & Seniority Level:**
   - **Tier A — Boardroom / Chair / NED / PE Advisor / C-Suite:** High-gravitas, peer-to-peer tone. Ban "lead-gen bro" tactics (no "DM me a keyword", no flashy sales arrows). Focus on governance, P&L scale, commercial transformation, and executive search / PE keywords.
   - **Tier B — Founder / B2B Consultant / Fractional Executive:** Outcome-driven conversion funnel. Use the 3-second billboard banner, Cold/Warm/Hot Featured links, and lead-capture CTAs.
   - **Tier C — Career Changer / Job Seeker:** Recruiter & ATS alignment. Focus on transferable skill clusters, matching 85–90% of target job description keywords, and specific CAR (Challenge → Action → Result) proof points.
2. **Primary Target Audience:** Who needs to be convinced in 10 seconds? (e.g., PE Operating Partners & Board Headhunters, B2B Buyers, or Hiring Managers).
3. **Core Positioning "Spike" + Contrarian Belief:**
   - What is the **intersection of skills** that makes this person a "category of one" (e.g., bridging *Physical/Digital Product & Consumer Proposition* with *AI, Data & Commercial Transformation*)?
   - What do they believe about their industry that most people get wrong?

---

## Step 3: Score the Baseline Profile (5-Pillar Rubric)

Consult [2026 AI Audit Rules & Scoring Rubric](./references/2026_ai_audit_rules.md) and score the current profile from **1 to 10** across all 5 weighted pillars:

1. **Algorithmic & LLM Alignment (25%):** Check the 5 Author Data Fields (*Name, Headline, Company link, Industry, Title*) and whether the **Top 3–5 Pinned Skills** match the target niche or misclassify the user in legacy roles.
2. **Above-the-Fold Clarity / 10-Second Test (25%):** Evaluate Photo, Banner, Headline (`What + Who + Outcome/Proof`), and Contact Info / Custom Button (flag outdated company URLs immediately).
3. **About Section & 265-Character AI Hook (20%):** Simulate the exact 2-sentence summary LinkedIn Recruiter AI currently generates from the opening 265–300 characters, then show the upgraded version.
4. **Proof, Authority & Hygiene (15%):** Check Experience entries for quantified outcomes vs. passive committee/job duties, un-surfaced achievements buried only in the Summary, duplicate role entries, and spelling/grammar typos.
5. **Conversion & Reference-Check Architecture (15%):** Evaluate the Featured section, Services section, and Recommendations mix.

---

## Step 4: Generate the Full Copy-Paste Overhaul (80/20 Human Rules)

Consult [StorySelling & Content Playbook](./references/storyselling_and_content_playbook.md) and write ready-to-paste upgrades following these strict rules:
- **First-person ("I") only**—never third-person bio style.
- **Ban AI clichés:** Never use *"passionate," "results-driven," "thought leader," "delve," "tapestry," "leveraging synergies,"* or *"elevate."*
- **Deliver these 6 deliverables:**
  1. **Top 5 Under-20-Minute Quick Wins:** Immediate hygiene, typo, URL, and skill-pinning fixes.
  2. **3-Pillar Skill Cluster Architecture:** Exact Top 5 skills to pin + supporting semantic cluster skills to attach to roles.
  3. **5 Headline Options (<220 chars):** Blending `[Role/Identity] + [Who You Help & Core Spike] + [Hard Scale/Proof]`.
  4. **3-Second Banner Blueprint:** Exact text layout and credential strip calibrated to the user's archetype.
  5. **Complete "About" Section (5-Paragraph StorySelling + 265-Char AI Hook):**
     - *Paragraph 1 (The 265-Char AI Hook):* Who you help, across what domains (e.g., Product, Consumer, AI, Data), and at what scale.
     - *Paragraph 2 (Contrarian Point of View):* What most organisations/boards get wrong and why bridging your core domains solves it.
     - *Paragraph 3 (Proof Pillars with Numbers):* 3 scannable bullet pillars with P&L scale, product/consumer wins, and transformation receipts.
     - *Paragraph 4 (Human Personality & Culture):* How you show up, leadership/coaching philosophy, and 1–2 memorable human details.
     - *Paragraph 5 (Clear CTA):* Who should reach out and for what mandates.
  6. **Experience Section Rewrites (Context + CAR Outcomes):** 1–2 sentences of role context + 2–3 outcome-driven bullets per role, surfacing hidden product/commercial wins and fixing all typos.

---

## Step 5: Reactivation & Ongoing Cadence

Provide a tailored post-update activation plan matched to the user's appetite:
- **Low-Lift / Executive Mode (15 mins/week):** "Boardroom Dream 50" substantive commenting + 1–2 high-value "Point of View" posts per month + 3 targeted Recommendation requests.
- **High-Velocity Creator Mode (4 posts/week):** The Tuesday (Educate) / Wednesday (Document) / Thursday (Storytell) / Sunday (Sell) system + "3+1" post-publish comment routine detailed in [StorySelling & Content Playbook](./references/storyselling_and_content_playbook.md).
