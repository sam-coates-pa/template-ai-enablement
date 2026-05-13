# template-ai-enablement
A full‑featured AI enablement template designed to accelerate responsible adoption across delivery teams, with ready‑made prompt patterns, Gemini and Claude Code assistant setups, and governance guardrails. Includes structured prompt libraries and policy‑led best practices.


---

## Project Layout (key folders)
```
template-ai-enablement/
├── README.md
├── .env.example
├── .github/
│   └── workflows/
│       └── ai-checks.yml
│
├── prompts/
│   ├── data-quality/
│   │   └── dq_prompt_template.md
│   ├── code-review/
│   │   └── code_review_prompt.md
│   ├── documentation/
│   │   └── documentation_prompt.md
│   └── iac/
│       └── iac_prompt_template.md
│
├── assistants/
│   ├── gemini/
│   │   └── gemini-instructions.md
│   └── claude/
│       └── claude-code-guidance.md
│
├── use-cases/
│   ├── requirements-generation/
│   │   ├── use-case.md
│   │   ├── prompts.md
│   │   └── sample-io.md
│   └── test-case-generation/
│       └── use-case.md
│
├── playbooks/
│   ├── ai-discovery-workshop.md
│   └── prompt-engineering-session.md
│
├── blueprints/
│   └── automated-code-review/
│       ├── overview.md
│       ├── architecture.puml
│       └── implementation.md
│
├── llm-clients/
│   └── python/
│       └── openai_client.py
│
├── rag/
│   └── rag_pipeline.py
│
├── templates/
│   ├── use-case-template.md
│   ├── prompt-template.md
│   └── ai-feature-spec.md
│
├── evaluation/
│   └── prompt-evaluation.md
│
└── docs/
    ├── policy.md
    └── best-practices.md

```

## What’s Included
- Standardised prompt templates
- Gemini and Claude Code assistant guidance
- AI usage policies and best practices

## How to Use
1. Click **Use this template** in GitHub
2. Clone your new repository
3. Tailor prompts, assistants, and policies to your context

## Governance
This repo is designed to support safe, compliant, and repeatable AI usage.
See `ai-enablement/docs/policy.md` for guardrails.

