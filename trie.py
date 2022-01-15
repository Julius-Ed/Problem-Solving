class TrieNode:
    def _init_(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def _init_(self):
        self.root = TrieNode()

    # Time: O(m); Space: O(m) where m is the length of word
    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end_of_word = True

    # Time: O(m); Space: O(1)
    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end_of_word

    # Time: O(m); Space: O(1)
    def starts_with(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True



obj = Trie()
obj.insert('apple')
obj.insert('application')
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)