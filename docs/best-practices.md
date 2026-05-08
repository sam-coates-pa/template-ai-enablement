# AI Enablement Best Practices

## 1. Treat Prompts as Assets
Prompts should be versioned, reviewed, and maintained like code. Avoid ad‑hoc, untracked prompts in chat tools.

## 2. Always Apply Human Review
AI outputs must be reviewed by a human before use in:
- Code
- Architecture decisions
- Documentation
- Data generation

## 3. Be Explicit in Prompts
High‑quality outputs depend on:
- Clear context
- Defined constraints
- Stated assumptions
- Required output formats

## 4. Avoid Sensitive Data
Never input:
- Personal data
- Credentials or secrets
- Confidential or regulated information

Use synthetic or anonymised examples only.

## 5. Prefer Explainability Over Speed
Ask AI to:
- Show reasoning
- Highlight assumptions
- Call out uncertainty

This improves trust and reduces misuse.

## 6. Keep Assistants Aligned
Ensure Copilot, Gemini, Claude, or other assistants follow:
- Shared coding standards
- Security expectations
- Documentation conventions

## 7. Monitor Prompt Drift
Periodically review prompts and assistant configs to ensure:
- They still meet current standards
- They reflect updated architecture or policies

## 8. AI Is a Tool, Not an Authority
AI can assist, not decide. Accountability always remains with the delivery team.
