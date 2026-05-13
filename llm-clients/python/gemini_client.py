import os
from google.generativeai import configure, GenerativeModel

# Set API key via environment variable: GOOGLE_API_KEY
configure(api_key=os.getenv("GOOGLE_API_KEY"))

MODEL_NAME = "gemini-1.5-pro"


def generate_response(prompt: str) -> str:
    model = GenerativeModel(MODEL_NAME)

    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0.2,
            "max_output_tokens": 1024,
        }
    )

    return response.text


if __name__ == "__main__":
    test_prompt = "Explain AI enablement in simple terms."
    print(generate_response(test_prompt))
