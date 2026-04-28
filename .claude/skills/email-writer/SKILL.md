---
name: email-writer
description: Drafts emails in Roger's tone of voice — formal or casual, in Italian or English. Use this skill whenever the user asks to write, draft, compose, or reply to an email, or says things like "write an email to...", "draft a message for...", "help me reply to...", "I need to email someone about...". Always use this skill for email requests even when tone isn't mentioned explicitly.
---

# Email Writer

Drafts emails that sound like Roger wrote them — not AI-polished filler, not generic templates. The goal is a message Roger could send as-is, or with one quick read-through.

## Roger's voice

Two registers, based on his samples:

**Formal** (clients, senior stakeholders, institutions, first contact with someone he doesn't know):
- Italian: `Spettabile Signore/Signora` or `Gentile [Nome]`, `Lei` form throughout, precise and structured phrasing, closes with `Distinti saluti` or `Cordiali saluti`
- English: full sentences, no contractions, professional but not stiff — authoritative and courteous, closes with `Kind Regards`
- Tone: signals respect and competence without being obsequious

**Casual** (colleagues, team, people he already knows):
- Italian: `Ciao [Nome]` or just `Ciao`, plain conversational language, closes with `Saluti` or just the name
- English: direct, warm, may use contractions — gets to the point fast
- Tone: efficient without being cold

**No padding in either register.** Never write: "I hope this finds you well", "please don't hesitate to reach out", "as per my previous email", "kindly be advised". Roger doesn't write like that.

## Language rule

Match the language of the request:
- User writes the prompt in Italian → draft in Italian
- User writes the prompt in English → draft in English
- User explicitly specifies a language → use that language
- Mixed / unclear → ask before drafting

If the request is in English but the recipient's name or context suggests they may be Italian (e.g., "Maria Rossi", "cliente di Milano"), note this at the end: *[Written in English because your prompt was in English — let me know if you'd like it in Italian instead.]*

## How to draft

**Step 1 — Gather context (if missing)**

If the request doesn't tell you who the recipient is and what the relationship is, ask one focused question before drafting:
> "Who's this going to — client, colleague, or someone new?"

Don't ask for more than what you need. If the situation is clear from the prompt, skip straight to drafting.

**Step 2 — Pick the register**

| Recipient type | Register |
|---|---|
| Client, external stakeholder, institution, unknown | Formal |
| Colleague, teammate, internal | Casual |
| Unclear | Ask |

**Step 3 — Write the email**

Structure:
1. **Subject** — specific and informative, not vague ("Project Delta — timeline update", not "Update")
2. **Salutation** — matching the register
3. **Opening sentence** — state the purpose immediately; don't warm up with pleasantries
4. **Body** — cover the substance; if Roger gave you bullet points, weave them into prose
5. **Call to action** — end with a clear next step or explicit close (decision needed, meeting request, no reply needed, etc.)
6. **Sign-off** — matching the register

## Output format

Present the email ready to copy:

```
Subject: [subject line]

[salutation],

[body]

[sign-off],
Roger
```

If the user gives you bullet points or rough notes, don't reflect them back as bullets — convert them into natural prose in Roger's voice.

After the email, add one line in brackets if you made a register or language assumption:
> *[Drafted formal / casual, in Italian / English — let me know if you'd like a different register or language.]*

## Style reference

Sample emails in `sample-emails/` relative to the project root:
- `email1.html` — formal Italian (institutional salutation, `Lei` form, elaborate phrasing)
- `email2.html` — casual Italian (Ciao, direct, brief)
