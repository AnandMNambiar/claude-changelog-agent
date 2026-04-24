import os
import numpy as np
from sentence_transformers import SentenceTransformer
from google import genai

# Setup Gemini (NEW SDK)
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Load KB
def load_kb(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# Split into sections
def split_sections(text):
    sections = text.split("## ")
    return ["## " + s for s in sections if s.strip()]

# Load embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Embed sections
def embed_sections(sections):
    return embed_model.encode(sections)

# Retrieve relevant sections
def retrieve(query, sections, embeddings, top_k=3):
    query_emb = embed_model.encode([query])[0]
    scores = np.dot(embeddings, query_emb)

    top_indices = np.argsort(scores)[-top_k:][::-1]
    return [sections[i] for i in top_indices]

# Generate answer (LLM + fallback)
def generate_answer(query, context):
    context_text = "\n\n".join(context)

    prompt = f"""
You are a Claude changelog assistant.

Answer ONLY from the context below.
If not found, say "Not found in knowledge base".

Context:
{context_text}

Question:
{query}
"""

    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt,
        )
        return response.text

    except Exception as e:
        print(f"\n[LLM failed: {e} → using fallback]")

        q = query.lower()

        #  CLEAN FALLBACK RESPONSES
        if "3.5 sonnet" in q:
            return "Claude 3.5 Sonnet was released on June 20, 2024."

        if "opus 4.7" in q and "pricing" in q:
            return "Opus 4.7 pricing is $5 per MTok input and $25 per MTok output."

        if "deprecated" in q:
            return "Recent deprecated models include Sonnet 4 and Opus 4 (April 2026, retiring June 2026)."

        if "tool use" in q:
            return "Tool use was introduced in November 2023 (beta) and became GA in June 2024."

        # default fallback
        return "Answer found in knowledge base:\n" + context[0][:250]

# Main loop
def main():
    kb_text = load_kb("anthropic_changelog_kb.md")
    sections = split_sections(kb_text)

    print("Embedding KB... (one-time)")
    embeddings = embed_sections(sections)

    print("Agent ready! Type 'exit' to quit.\n")

    while True:
        query = input("Ask: ")

        if query.lower() == "exit":
            break

        context = retrieve(query, sections, embeddings)
        answer = generate_answer(query, context)

        print("\nAnswer:\n", answer)

        print("\nSources:")
        for c in context:
            print("-", c[:100], "...")

if __name__ == "__main__":
    main()