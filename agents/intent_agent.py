from langchain_ollama import ChatOllama

class IntentAgent:

    def __init__(self):
        self.llm = ChatOllama(model="llama3", temperature=0)

        self.prompt = """
Classify query into ONE:

- herb_information → plant details
- health_query → explanation
- recommendation → treatment, suggestions

Examples:
- "ways to treat cough" → recommendation
- "what should I take for fever" → recommendation

Return ONLY:
herb_information OR health_query OR recommendation OR general
"""

    def run(self, question: str):

        res = self.llm.invoke(f"{self.prompt}\nQuery: {question}")

        intent = res.content.strip().lower().replace(" ", "_")

        valid = ["herb_information", "health_query", "recommendation", "general"]

        return intent if intent in valid else "herb_information"