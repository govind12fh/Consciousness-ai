 class DharmaEngine:
    def __init__(self):
        self.rules = {
            "truth": "Always align responses with universal truth.",
            "non-violence": "Do not generate harmful outputs.",
            "self-regulation": "Adapt to context ethically."
        }

    def evaluate(self, query):
        if "harm" in query:
            return "This action is against Dharma. Seek balance."
        return f"Dharma-compliant response: {query}"
        src/dharma_module.py
