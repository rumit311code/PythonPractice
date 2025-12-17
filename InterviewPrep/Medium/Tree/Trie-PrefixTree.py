"""
https://neetcode.io/problems/implement-prefix-tree/question

Video:

Implement Trie (Prefix Tree)

A prefix tree (also known as a trie) is a tree data structure used to efficiently
store and retrieve keys in a set of strings. Some applications of this data structure
include auto-complete and spell checker systems.

Implement the PrefixTree class:
- 'PrefixTree()' Initializes the prefix tree object.
- 'void insert(String word)' Inserts the string 'word' into the prefix tree.
- 'boolean search(String word)' Returns 'true' if the string 'word' is in the prefix tree
    (i.e., was inserted before), and 'false' otherwise.
- 'boolean startsWith(String prefix)' Returns 'true' if there is a previously inserted string
    'word' that has the prefix 'prefix', and 'false' otherwise.

Example 1:
Input:
["Trie", "insert", "dog", "search", "dog", "search", "do", "startsWith", "do", "insert", "do", "search", "do"]
Output:
[null, null, true, false, true, null, true]

Explanation:
PrefixTree prefixTree = new PrefixTree();
prefixTree.insert("dog");
prefixTree.search("dog");    // return true
prefixTree.search("do");     // return false
prefixTree.startsWith("do"); // return true
prefixTree.insert("do");
prefixTree.search("do");     // return true

Constraints:
- 1 <= word.length, prefix.length <= 1000
- word and prefix are made up of lowercase English letters.
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            # new char
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # char found in one of the children. insert next char.
            cur = cur.children[c]
        # iterated over all characters. mark the current node as end of word.
        cur.end_of_word = True


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            # char not found in any children.
            if c not in cur.children:
                return False
            # char found in one of the children. check next char.
            cur = cur.children[c]
        # iterated over all characters. the last char's end_of_word = true.
        return cur.end_of_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            # char not found in any children.
            if c not in cur.children:
                return False
            # char found in one of the children. check next char.
            cur = cur.children[c]
        # iterated over all characters and all were found. return True.
        return True
