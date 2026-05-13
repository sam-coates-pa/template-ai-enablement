# Use Case: AI-Assisted Test Case Generation

## 🎯 Problem
Test case creation is:
- Time-consuming
- Repetitive
- Often incomplete or inconsistent

## 💡 Solution
Use AI to generate test cases from:
- Requirements
- User stories
- Acceptance criteria
- API specs

---

## 📌 When to Use
- Sprint planning
- QA preparation
- Regression test expansion
- API or feature validation

---

## ⚙️ Inputs

- User stories
- Acceptance criteria
- Functional requirements
- System specifications

---

## 📤 Outputs

- Functional test cases
- Edge cases
- Negative scenarios
- Test data suggestions

---

## ✅ Example

### Input
"User logs into the system using email and password"

### Output

#### Functional Test Cases
- Valid login with correct credentials
- Error message on incorrect password
- Account lock after multiple failed attempts

#### Edge Cases
- Empty email field
- Very long input values

#### Negative Cases
- SQL injection attempt
- Invalid email format

---

## 📈 Benefits

- Faster test creation
- Improved test coverage
- Standardised test formats
- Reduced manual effort

---

## ⚠️ Risks

| Risk | Mitigation |
|------|-----------|
| Missing domain-specific logic | Human review |
| Hallucinated scenarios | Validate against requirements |
| Over-reliance on AI | Combine with SME input |

---

## ✅ Validation Approach

- Review generated test cases with QA team
- Cross-check against requirements
- Run sample execution
- Iterate prompts

---

## 🧠 Prompt Example

See `/prompts/documentation/documentation_prompt.md` or create a dedicated test-case prompt.

Example:


