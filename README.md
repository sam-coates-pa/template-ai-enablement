# template-ai-enablement
A full‑featured AI enablement template designed to accelerate responsible adoption across delivery teams, with ready‑made prompt patterns, Gemini and Claude Code assistant setups, and governance guardrails. Includes structured prompt libraries and policy‑led best practices.

This repository provides a **practical toolkit** combining:
- Standardised prompt engineering patterns  
- Reusable use cases and playbooks  
- Multi-model AI integration (Gemini, Claude, Copilot-style)  
- Governance guardrails and best practices  
- Starter architecture and implementation patterns  

---

##  Purpose

This template is built to help teams move from:

> ❌ Ad-hoc AI experimentation  
> ✅ → Structured, repeatable AI delivery capability  

It enables:
- Faster onboarding onto AI-enabled projects  
- Consistent quality of AI outputs  
- Safe and compliant usage of AI tools  
- Reuse of proven patterns across engagements  

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


---

## What’s Included

### Prompt Library
Structured prompts for common delivery activities:
- Code review
- Documentation generation
- Data quality analysis
- Infrastructure-as-Code validation  

---

### AI Assistants
Pre-configured guidance for:
- Google Gemini  
- Anthropic Claude Code  

Enables consistent usage across teams.

---

### Delivery Use Cases
Ready-to-use AI applications:
- Requirements generation  
- Test case generation  

Includes:
- Problem definition  
- Prompt patterns  
- Sample inputs/outputs  
- Risks and validation guidance  

---

### Playbooks
Step-by-step guides for running:
- AI discovery workshops  
- Prompt engineering sessions  

Helps teams **operationalise AI in projects**.

---

### Architecture Blueprints
Reusable solution designs:
- Automated code review pipeline  
- AI-integrated delivery workflows  

Includes diagrams and implementation guidance.

---

### LLM Clients
Starter Python integrations for:
- Azure OpenAI (Copilot-style)
- Gemini
- Claude  

Designed for:
- Consistency  
- Extensibility  
- Enterprise usage  

---

### RAG (Retrieval-Augmented Generation)
Basic pipeline for:
- Context-aware AI responses  
- Document-driven querying  

---

### Governance & Best Practices

Located in `/docs/`:
- AI usage policy  
- Responsible AI guidelines  
- Best practices for safe adoption  

---

### Evaluation Frameworks

Assess AI outputs using:
- Accuracy  
- Completeness  
- Consistency  
- Safety  

---

### CI/CD Guardrails

GitHub Actions workflow (`ai-checks.yml`) ensures:
- Prompt quality checks  
- Markdown validation  
- Python syntax validation  
- Governance presence  

---

## Getting Started

### 1. Create Your Repo

Click **“Use this template”** in GitHub.

---

### 2. Clone Locally

```bash
git clone https://github.com/pa-int-data-engineering-de/template-ai-enablement
cd template-ai-enablement
```
### 3. Tailor prompts, assistants, and policies to your context

### 4. Configure Environment
Copy the example file:
```bash
cp .env.example .env
```

Add your API keys:
```bash
# GeminiGOOGLE_API_KEY=

# ClaudeANTHROPIC_API_KEY=

# Azure OpenAI (Copilot-style)
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_DEPLOYMENT_NAME=
```
### 5. Start Using AI Clients
Example:
```bash
cd llm-clients/pythonpython openai_client.py
```

### 6. Apply to Delivery

Use /use-cases during backlog refinement
Run /playbooks with stakeholders
Apply /prompts in daily delivery
Follow /docs/policy.md for safe usage


##  How to Use This Repo in Projects
###  During Discovery

Run ai-discovery-workshop.md
Identify high-value use cases


###  During Design

Use blueprints for architecture patterns
Define AI-enabled features


###  During Delivery

Apply prompt templates
Use LLM clients for integration
Generate outputs (code, docs, tests)


###  During Governance

Enforce policy and best practices
Validate outputs using evaluation frameworks
## Governance
This repository is designed to support:

- Safe handling of sensitive data
- Reduction of hallucinations
- Human-in-the-loop validation
- Compliance with enterprise standards
See `ai-enablement/docs/policy.md` for guardrails.

