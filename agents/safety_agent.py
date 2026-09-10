from langchain_ollama import ChatOllama


class SafetyAgent:

    def __init__(self):
        self.llm = ChatOllama(model="llama3", temperature=0)

    def run(self, question: str):

        prompt = f"""
You are a STRICT medical safety classifier.

Your job is to classify the user's query as SAFE or UNSAFE.

Mark UNSAFE if:
- User wants to replace prescribed medicine
- User wants to stop or skip medicine
- User asks for treatment decisions without a doctor
- User asks for dosage or medical advice

Mark SAFE if:
- General herb information
- Benefits of herbs
- Non-critical recommendations

Examples:

Q: Can I replace BP medicine with Tulsi?
A: UNSAFE

Q: Should I stop my diabetes tablets?
A: UNSAFE

Q: What are benefits of Tulsi?
A: SAFE

Q: Herbs for cough?
A: SAFE

---

Now classify:

Query: {question}

Answer ONLY one word:
SAFE or UNSAFE
"""

        response = self.llm.invoke(prompt).content.strip().upper()

        # Debug print (optional)
        print("Safety LLM Response:", response)

        if "UNSAFE" in response:
            return {
                "safe": False,
                "answer": "⚠️ You should not replace or stop prescribed medicine without consulting a doctor."
            }

        return {"safe": True}