class MemoryManager:
    def __init__(self, token_limit=2000):
        self.token_limit = token_limit
        self.memory = []

    def estimate_tokens(self, text):
        return int(len(text.split()) * 1.3)

    def add_and_compress(self, docs):
        combined = " ".join(docs)

        # compress if too big
        if self.estimate_tokens(combined) > 300:
            combined = self.compress(combined)

        self.memory.append(combined)

        # enforce limit
        while self.total_tokens() > self.token_limit:
            self.memory.pop(0)

        return combined

    def compress(self, text):
        words = text.split()
        return " ".join(words[:20]) + "..."
    

    def total_tokens(self):
        return sum(self.estimate_tokens(m) for m in self.memory)