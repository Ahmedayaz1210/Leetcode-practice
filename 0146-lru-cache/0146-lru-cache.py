'''
UNDERSTAND:
- Input: Three things
	- Capacity of memory of our Cache
	- Can be called two methods:
		- put: 2 parameters, key value pair
		- get: takes in the key and returns the value if exists else -1
- Have to write all of the methods
- In original method we initialize the capacity which is an integer
- Create cache of the amount of capacity, so len(capacity) long cache (list)
- Put - appends the key value pair in our cache, if key already exist replace the value with new passed value
- Get - returns the value of a key if exists else - 1
- But if put is called and our cache is full, we replace the least recelty used cache or key value pair with the new key value pair passed in
- Capacity will always be an integer?
- Cache will be capacity long?
- Get returns an int and put returns None? Yes
- What are average TC for both methods? O(1)
- Space Constraints? Yes cache can only be capacity long
- How big can capacity be? 1 - 3000 inclusive
- How big can each key value be? Key is 0 to 10^4 and value is 0 to 10 ^ 5 inclusive
- How many calls can be made to each method? At most 2 * 10^5
- If capacity is 0 and put is called we just return None? 
- Is our cache a list or a dictionary? Dictionary
- 

MATCH:
- Obviously need a hashmap which will be our cache to store key value pairs
- How do we keep track of the LRU cache? In other words they key value pair we appended or called the earliest?
- Since this question is under LL topic, we can use a LL to keep track of all the calls and keep the least recently used always at the end, this way we can use a map to keep track of nodes as keys and values so it becomes a pair
- You can use left and right pointers to keep track of LRU and MRU
- We basically will be swapping these nodes which means a doubly LL
- Our node will have a key value pair and previous and next pointer
- LRU and MRU are more of like dummy nodes for O(1) operations

PLAN:
- Create a Node class for our doubly LL:
	- Have key value pair, next and previous pointers
- Default method: 
	- Initiliazes capacity from the given parameter
	- Initializes our hashmap of length capacity
- Create remove and insert helper methods to add nodes next to LRU and MRU nodes so we can have O(1) retrieval 
- Get: if key exists return value else return -1, will be done in O(1) in python dictionary
	- Update MRU 
- Put: 
- We will be using doubly LL
- Now if we get another put call and our cache is full first before removing our LRU, we assign left (LRU pointer) to next LRU node
- Now we update the key in hash map to be the key which was passed in replacing LRU key and put the right (MRU) pointer onto the new node

EVALUATE:
- Problem was way too hard, I couldn't solve it
- The idea of using doubly LL was not easy at all
- Time Complexity: O(1)
- Space Complexity: O(1)
'''

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()

        # LRU and MRU pointers
        self.left, self.right = Node(0,0), Node(0,0)
        # Pointing to each other so new nodes go in middle
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list, helper function for get
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right, helper function for get
    def insert(self, node):
        # The reason we created previous from the right is because we want node one previous from the right not the left node, it's just something I was thinking on why we created previous one behind the right and not just simply left because when LL is empty they both point to each other
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            #remove form the list and delete LRU from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)