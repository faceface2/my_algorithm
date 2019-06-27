class TrieNode:
    def __init__(self):
        self.path = 0
        self.end = 0
        self.maps = [TrieNode] * 26


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        if not word:
            return
        node = self.root
        for i in word:
            index = ord(i)
            if not node.maps[index]:
                node.maps[index] = TrieNode()
            node = node.maps[index]
            node.path += 1
        node.end += 1

    def delete(self, word: str) -> None:
        if self.search(word):
            node = self.root
            for i in word:
                index = ord(i)
                if node.maps[index].path == 1:
                    node.maps[index] = None
                    return
                node.maps[index].path -= 1
                node = node.maps[index]
            node.end -= 1

    def search(self, word: str) -> bool:
        if not word:
            return False
        node = self.root
        for i in word:
            index = ord(i)
            if not node.maps[index]:
                return False
            node = node.maps[index]
        return node.end != 0

    def prefixNumber(self, pre: str):
        if not pre:
            return 0
        node = self.root
        for i in pre:
            index = ord(i)
            if not node.maps[index]:
                return 0
            node = node.maps[index]
        return node.path

a = Trie()
a.insert('abcd')
