import os
import sys
import chromadb

# --------------------------------------------------
# PATH SETUP
# --------------------------------------------------

RAG_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

PROJECT_DIR = os.path.dirname(RAG_DIR)

DATA_PATH = os.path.join(
    PROJECT_DIR,
    "data",
    "enhanced_herb.json"
)

CHROMA_PATH = os.path.join(
    RAG_DIR,
    "chroma_db"
)


if RAG_DIR not in sys.path:
    sys.path.insert(0, RAG_DIR)                  #it can import local files we created !

from ingestion import load_plants
from splitter import make_chunks
from embedding import embed



client = chromadb.PersistentClient(
    path=CHROMA_PATH
)

collection = client.get_or_create_collection(
    name="plants"
)


# --------------------------------------------------
# ADD CHUNKS
# --------------------------------------------------

def add_chunks(chunks):

    total = len(chunks)

    batch_size = 500

    print(
        f"\nEmbedding {total} chunks..."
    )

    for start in range(
        0,
        total,
        batch_size
    ):

        batch = chunks[    #takes 500chuns at a time
            start:start + batch_size
        ]
            
#extraction
        ids = [
            c["id"]
            for c in batch
        ]

        texts = [
            c["text"]
            for c in batch
        ]

        metadatas = [
            {
                "name": c["name"],
                "link": c["link"]
            }
            for c in batch
        ]

        end = min(
            start + batch_size,
            total
        )

        print(
            f"\nEmbedding chunks "
            f"{start + 1}-{end} "
            f"of {total}"
        )

        vectors = embed(
            texts,
            batch_size=32
        )

        collection.upsert(
            ids=ids,
            embeddings=vectors,
            documents=texts,
            metadatas=metadatas
        )

        print(
            f"Stored {end}/{total}"
        )

    print(
        f"\nFinished!"
    )

    print(
        f"Total chunks in ChromaDB: "
        f"{collection.count()}"
    )


# --------------------------------------------------
# BUILD VECTOR STORE
# --------------------------------------------------

if __name__ == "__main__":

    print(
        "\n================================"
    )

    print(
        "BUILDING HERBAL VECTOR STORE"
    )

    print(
        "================================\n"
    )

    # ----------------------------------------------
    # LOAD DATA
    # ----------------------------------------------

    print(
        "Loading enhanced herb dataset..."
    )

    plants = load_plants(
        DATA_PATH
    )

    print(
        f"Loaded {len(plants)} herbs"
    )

    # ----------------------------------------------
    # CREATE CHUNKS
    # ----------------------------------------------

    print(
        "\nCreating plant chunks..."
    )

    chunks = make_chunks(
        plants
    )

    print(
        f"Created {len(chunks)} chunks"
    )

    # ----------------------------------------------
    # STORE
    # ----------------------------------------------

    add_chunks(
        chunks
    )