"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
'''
UNDERSTAND:
- Input: Given root of an undirected connected graph as a node
- Have to traverse over that graph and create a deep copy of it
- A deep copy is basically an exact clone of the graph but it uses entirely different memory, it doesn't point to the same memory as original
- Output: Return root node of the deep copy graph
- Node class concists of an int val and a list neighbors which keeps track of all the neighbors a node is connected to
- Each node in the given graph has the same value as it's position, 1 indexed, so node 1 has value 1 and so on
- So we have to make new nodes but with same value and pretty much connected to the same neighbors clones
- How big can the graph be? [0,100]
- 1 <= Node.val <= 100
- Is each node going to have a unique value? Yes
- The Graph is connected and all nodes can be visited starting from the given node.
- Empty graph return empty graph
- A node's neighbors are represented in an adjacency list where each sub list in the input is neighbors of the current index node we are on
- TC? SC?

MATCH:
- So what do we have to do here? Have to loop the graph and create new copies
- But how do we loop? We take the given node and explore it's all neighbors
- Let's use DFS to explore each path 
- Addtionally let's use a hashmap to create a new node and store original node's value inside it
- Then we explore neighbors

PLAN:
- A hashmap to create the clones and remember which ones we have already created
- Looping over the graph by taking the first node and visiting it's each neighbor through DFS
- Now for each node we are on, we create a new node at the original node's position and we append the original's value into the new node
- We loop over original node's neighbors inside dfs, we append its neighbors to our cloned node but we append the cloned neighbors, that is why we send the neighbor back to dfs to create or check if it has a copy
- In the end our dfs returns the current new copy we just made so it gets appended to the neighbors of copied node.

EVALUATE:
- Honestly the problem wasn't too hard, I feel like I could have gotten it, it was just a bit tricky
- I got about 50% of the logic and code myself
- TC: O(V+E) because we loop over the whole graph to create it's clone, the E comes when we go to the neighbors, even if their clones have been made, it will still try to visit them
- SC: O(V) because hashmap only stores the cloned vertices

'''
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)

            oldToNew[node] = copy

            for n in node.neighbors:
                copy.neighbors.append(dfs(n))

            return copy

        return dfs(node) if node else None
        