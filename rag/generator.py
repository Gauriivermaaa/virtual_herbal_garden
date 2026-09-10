import os
import sys
import requests

# --------------------------------------------------
# PATH SETUP
# --------------------------------------------------

RAG_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

if RAG_DIR not in sys.path:
    sys.path.insert(0, RAG_DIR)

from retriever import search


# --------------------------------------------------
# OLLAMA
# --------------------------------------------------

OLLAMA_URL = "http://localhost:11434/api/chat"

MODEL = "llama3"


# --------------------------------------------------
# GENERATE ANSWER
# --------------------------------------------------

def ask_ollama(
    question,
    chunks,
    model=MODEL
):

    # Create context from retrieved chunks
    context = "\n\n".join(
        f"{c['name']}: {c['text']}"
        for c in chunks
    )

    # --------------------------------------------------
    # PROMPT
    # --------------------------------------------------

    prompt = f"""You are a friendly Virtual Herbal Garden assistant.

Answer the user's question naturally and clearly using ONLY the information provided below.

Rules:
1. Give a short, natural answer that directly addresses the user's question.
2. Do not simply copy the therapeutic-use names as a raw list.
3. Convert technical terms into simple language when possible.
4. Do not add medical information that is not present in the provided information.
5. Do not make claims stronger than the provided information supports.
6. If several therapeutic uses are relevant, combine them naturally into a sentence or a few bullet points.
7. If the information needed to answer the question is not available, say:
"I don't know based on the available data."
8. Do not mention context, retrieved chunks, dataset, RAG, or prompt.
9. Do not give unnecessary information.
10. Do not invent benefits or treatments.

INFORMATION:
{context}

USER QUESTION:
{question}

ANSWER:
"""

    # --------------------------------------------------
    # CALL OLLAMA
    # --------------------------------------------------

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "stream": False
        },
        timeout=120
    )

    # Raise error if Ollama returns an HTTP error
    response.raise_for_status()

    data = response.json()

    # Return generated answer
    return data["message"]["content"].strip()


# --------------------------------------------------
# MAIN
# --------------------------------------------------

if __name__ == "__main__":

    question = "What are the therapeutic uses of Tulsi?"

    print("\n================================")
    print("VIRTUAL HERBAL GARDEN - RAG")
    print("================================")

    print("\nUSER QUERY:")
    print(question)

    # --------------------------------------------------
    # RETRIEVE
    # --------------------------------------------------

    print("\nRETRIEVING CONTEXT...")

    chunks = search(
        question,
        top_k=8
    )

    print("\n--- RETRIEVED CONTEXT ---")

    for chunk in chunks:

        print(f"\n[{chunk['name']}]")

        print(chunk["text"])

        if "distance" in chunk:
            print(
                f"Distance: {chunk['distance']}"
            )

    # --------------------------------------------------
    # GENERATE
    # --------------------------------------------------

    print("\n--- GENERATING ANSWER ---")

    try:

        answer = ask_ollama(
            question,
            chunks
        )

        print("\n--- FINAL ANSWER ---")
        print(answer)

    except requests.exceptions.ConnectionError:

        print("\nERROR:")
        print(
            "Could not connect to Ollama."
        )
        print(
            "Make sure Ollama is running."
        )

    except requests.exceptions.Timeout:

        print("\nERROR:")
        print(
            "Ollama took too long to respond."
        )

    except Exception as e:

        print("\nERROR:")
        print(e)