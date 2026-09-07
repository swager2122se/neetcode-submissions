class Node:
    
    def __init__(self):
        self.children = {}
        self.lastChar = False


class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.lastChar =True
        

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False

        return cur.lastChar


    def startsWith(self, prefix: str) -> bool:
        
        cur = self.root
        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False

        return True
        