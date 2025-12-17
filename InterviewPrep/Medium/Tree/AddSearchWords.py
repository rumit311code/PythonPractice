"""
https://neetcode.io/problems/design-word-search-data-structure/question

Video: https://www.youtube.com/watch?v=BTf05gs_8iU

Design Add and Search Word Data Structure

Design a data structure that supports adding new words and searching for existing words.

Implement the `WordDictionary` class:
- `void addWord(word)` Adds `word` to the data structure.
- `bool search(word)` Returns `true` if there is any string in the data structure that matches
`word` or `false` otherwise. word may contain dots '.' where dots can be matched with any letter.

Example 1:
Input:
["WordDictionary", "addWord", "day", "addWord", "bay", "addWord", "may", "search", "say", "search", "day", "search", ".ay", "search", "b.."]
Output:
[null, null, null, null, false, true, true, true]

Explanation:
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("day");
wordDictionary.addWord("bay");
wordDictionary.addWord("may");
wordDictionary.search("say"); // return false
wordDictionary.search("day"); // return true
wordDictionary.search(".ay"); // return true
wordDictionary.search("b.."); // return true

Constraints:
- 1 <= word.length <= 20
- word in addWord consists of lowercase English letters.
- word in search consist of '.' or lowercase English letters.
- There will be at most 2 dots in word for search queries.
- At most 10,000 calls will be made to addWord and search.
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class WordDictionary:
    # this is same as Prefix Tree problem.
    # except for search part where if we get `.` character, we move on to the next character.
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
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

        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                # wild card found. move to the next char.
                if c == '.':
                    # check each child and its subtree.
                    for child in cur.children.values():
                        # i+1 = starting index of child.
                        # child -> the child node.
                        if dfs(i+1, child):
                            return True # all chars found in one of the child nodes.
                        return False # word not found in any of the child node.
                else: # regular char.
                    if c not in cur.children:
                        return False
                    # char found in one of the children. check next char.
                    cur = cur.children[c]

            # iterated over all characters. the last char's end_of_word = true.
            return cur.end_of_word

        return dfs(0, self.root)

