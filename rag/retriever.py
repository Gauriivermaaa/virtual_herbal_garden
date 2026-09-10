import os
import sys
import chromadb

# --------------------------------------------------
# PATH SETUP
# --------------------------------------------------

RAG_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

CHROMA_PATH = os.path.join(
    RAG_DIR,
    "chroma_db"
)

if RAG_DIR not in sys.path:
    sys.path.insert(0, RAG_DIR)

from embedding import embed


# --------------------------------------------------
# CHROMADB
# --------------------------------------------------

client = chromadb.PersistentClient(
    path=CHROMA_PATH
)

collection = client.get_collection(
    name="plants"
)


# --------------------------------------------------
# SEARCH
# --------------------------------------------------

def search(
    query,
    top_k=3
):

    query_vector = embed(
        [query],
        batch_size=1
    )[0]

    results = collection.query(
        query_embeddings=[query_vector],
        n_results=top_k
    )

    hits = []

    documents = results.get(
        "documents",
        [[]]
    )[0]

    metadatas = results.get(
        "metadatas",
        [[]]
    )[0]

    distances = results.get(
        "distances",
        [[]]
    )[0]

    for doc, meta, distance in zip(
        documents,
        metadatas,
        distances
    ):

        hits.append({
            "text": doc,
            "name": meta.get(
                "name",
                ""
            ),
            "link": meta.get(
                "link",
                ""
            ),
            "distance": distance
        })

    return hits


# --------------------------------------------------
# TEST
# --------------------------------------------------

if __name__ == "__main__":

    question = (
        "What are the therapeutic uses "
        "of Tulsi?"
    )

    print(
        "\n--- USER QUERY ---"
    )

    print(question)

    hits = search(
        question,
        top_k=3
    )

    print(
        "\n--- RETRIEVED CONTEXT ---"
    )

    for h in hits:

        print(
            f"\n[{h['name']}]"
        )

        print(
            h["text"]
        )

        print(
            f"Distance: {h['distance']}"
        )