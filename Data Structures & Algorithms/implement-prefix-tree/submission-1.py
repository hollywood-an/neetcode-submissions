class PrefixTree:

    def __init__(self):
        self.tree = []

    def insert(self, word: str) -> None:
        self.tree.append(word)

    def search(self, word: str) -> bool:
        for w in self.tree:
            if word == w:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for w in self.tree:
            if w.find(prefix) == 0:
                return True
        return False
        