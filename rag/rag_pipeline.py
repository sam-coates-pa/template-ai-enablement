from typing import List

def retrieve_documents(query: str) -> List[str]:
    # Placeholder retrieval logic
    return ["Document 1 content", "Document 2 content"]

def generate_answer(query: str):
    docs = retrieve_documents(query)
    context = "\n".join(docs)

    prompt = f"""
    Answer the question based only on the context.

    Context:
    {context}

    Question:
    {query}
    """

    return prompt  # Replace with LLM call


if __name__ == "__main__":
    print(generate_answer("What is AI enablement?"))
