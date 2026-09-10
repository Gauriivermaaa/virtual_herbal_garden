from langchain_ollama import ChatOllama
from rag.retriever import search

class HealthQueryAgent:

    def __init__(self):
        self.llm = ChatOllama(model="llama3", temperature=0)

        self.prompt = """
Answer using ONLY context.

Rules:
- Understand meaning (treat = therapeutic use)
- Max 3 sentences
"""

    def run(self, question: str):

        query = question + " therapeutic use"
        docs = search(query)[:3]

        context = "\n".join(
            f"{d['name']}: {d['text']}" for d in docs
        )

        res = self.llm.invoke(
            f"{self.prompt}\n\nContext:\n{context}\n\nQuestion:\n{question}"
        )

        return {
            "answer": res.content.strip(),
            "herbs": list(set([d["name"] for d in docs])),
            "sources": docs
        }