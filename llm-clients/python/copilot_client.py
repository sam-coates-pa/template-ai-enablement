import os
from openai import AzureOpenAI

# Environment variables required:
# AZURE_OPENAI_API_KEY
# AZURE_OPENAI_ENDPOINT
# AZURE_OPENAI_DEPLOYMENT_NAME

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")


def generate_response(prompt: str) -> str:
    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant focused on enterprise productivity."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=1024
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    test_prompt = "Generate a clean Python function to validate email addresses."
    print(generate_response(test_prompt))
