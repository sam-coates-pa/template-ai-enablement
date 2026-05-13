import os
import anthropic

# Set API key via environment variable: ANTHROPIC_API_KEY
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

MODEL_NAME = "claude-3-sonnet-20240229"


def generate_response(prompt: str) -> str:
    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=1024,
        temperature=0.2,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.content[0].text


if __name__ == "__main__":
    test_prompt = "Summarise benefits of AI enablement for enterprises."
    print(generate_response(test_prompt))
