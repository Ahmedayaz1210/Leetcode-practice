'''
UNDERSTAND:
- Input: Have 4 functions we need to implement. 
    - 1. Initializing our TrieNode
    - 2. Insert function to put a word into our trie tree
    - 3. Search function which searches for the given word inside our tree
    - 4. startsWith function which checks if the given string exists in the tree as a prefix BUT NOT as a complete word
- Output: inser returns nothing because it's just adding to the tree. search return boolean if the word exists as a "word" not prefix. Same for startsWith but this time the given word has to be a prefix not a "word". Prefix means characters in the same sequence from the start
- TC?
- SC?
- How big can our word be? >= 1 and <= 2000
- Same thing for prefix
- At most 3 * 104 calls in total will be made to insert, search, and startsWith.
- Unlike a Binary Tree, a Trie Tree's node can have upto 26 descendants from it because it's in letters so we can have at max 26 letters
- Also the root node in the Trie tree is always empty, doesn't have any value because you won't always have the same starting character for every word

MATCH:
- Obviously a Trie problem and I have done practice with AI so I am confident

PLAN:
- Firstly our Trie Tree structure:
    - A hashmap which can store every node's child(ren). (A word's first character is parent of it's next)
    - We need to check if our current node or character marks the end of the word. So a boolean variable "isEnd". Need this for startsWith and search function because this is going to be the distinction between them

- Secondly insert method:
    - Initialize your root node
    - Initialize your curr pointer node which will do the looping
    - Loop over the word and add a character if it doesn't already exist in the path
    - Lastly when we are at the last character make that node's boolean isEnd value True

- Thirdly, search method:
    - Once again make a current pointer node which starts at the root
    - Loop over the word and for each character check if it's inside the current nodes children, if not instantly return False because then no point in looking further if it isn't from the root or any parent node
    - Else move current to the character which has it in it's descendants
    - Lastly return current node's isEnd's boolean value because when we are at the last character of the current path or word, if it's not the end or isn't the whole world then search has to return False because search looks for a word and not a prefix

- Lastly, startsWith method
    - Pretty much the same thing except if our current node is end of a word we return False as we only it as a prefix not a word
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    
    def insert(self, word: str) -> None:
        
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True


    def search(self, word: str) -> bool:
        if not self.root:
            return None
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        if not self.root:
            return None
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)