'''
UNDERSTAND:
- Have main methods we want to implement:
    - addWord: A method which adds the given word to our data structure, returns None because all we are doing is adding the word
    - search: A method which searches for the given word, if the word exists returns True else False
- We will have to create our data structure
- In our search method, our given string can have '.' and a dot a means that it is a wildcard character and can be matched with anything as long as a character exists 
- TC? SC?
- Can search be called even if there is nothing in our DS? Yes but returns False
- How many words can our DS have?
- How big will a word be?>=1 and <= 25
- At most 104 calls will be made to addWord and search.
- There will be at most 2 dots in word for search queries.

MATCH:
- So we need an efficient DS where we can store our strings, match them
- Each word can lead to different branches with same prefixes
- The string storage + searching indicates it to Tries

PLAN:
- Start by creating our DS
- Make a TrieNode class with children hashmap to store children of the parent node. Also need isEnd boolean to check if our current character marks the end of the word and confirms we found the actual word not just a prefix
- Now let's come to our main class
- Starting with init function we can initialize our root node, which won't have any value because not all words will have the same starting character
- addWord: Here we are inserting given word into the tree
    - Make a current pointer to create our nodes and loop over them
    - Run a loop over our word, taking each character
    - If it doesn't already exist in the path, add it, because if it already exists, it can be used as a prefix to others
    - lastly update our current pointer to move to the next node or newly made node
    - remember node's don't store any values, they are key value pairs with the character they are made on so char is the key and empty node is the value.


'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True

    def search(self, word: str) -> bool:

        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                if word[i] == '.':
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]
            return curr.isEnd
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)