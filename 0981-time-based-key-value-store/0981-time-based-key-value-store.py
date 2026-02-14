'''
Understand:
- Given 2 methods, set method gets a key, value and timestamp, we store the value and time stamp for that key. So like a dictionary where key is the key and value and timestamp can be stored as pairs like this {"foo": [(value1, time1), (value2, time2), (value3, time3)]}
- Second function is get which takes in a key and timestamp and returns either the value at that key or timestamp but if that timestamp doesn't exist then it returns the highest timestamp's value within the same key, if there are no values in that key it returns ""
- What if a key is called but it doesn't exist? does it return none or something or do we need to not handle that?, it returns ""
- How big can value, key and timestamp be?
- Is timestamp strictly int? and key,value are strictly strings? are they lowercase?
- All the timestamps timestamp of set are strictly increasing. I think this means that they are in sorted order when stored.

Match:
- Set seems pretty simple, you just have to store in dictionary like I showed up there
- Get is a bit trickier because you have to return based of key and timestamp. and if a ts doesn't exist then we don't just return the closest one we return the closest smaller one because timestamp_prev <= timestamp.
- Since we know time only increases, timestamps will automatically be sorted, we can run a binary search over the stamps and they key is that we first have to see where the given timestamp would fit like not exactly the index but kind of and once we have found that we can return the one towards it's left but obviously we have to run BS and find it from a middle's perspective but if there are no values we return ""

Plan
- Ini the timemap dict
- set:
    - first check if key alr exists or not
    - just store incoming inputs in dict in structured way
- get:
- first check if key does not exist, we return ""
    - ini l = 0 and  r = len(self.timemap[key]) - 1
    - now run the BS
    - if the mid == timestamp: we alr got the answer we return the value at that timestamp
    - else
'''
class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.timemap:
            self.timemap[key] = [] # or use my_dict[key] = my_dict.get(key, [])
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        l = 0
        r = len(self.timemap[key]) - 1
        result = ""
        while l <= r:
            mid = (l + r) // 2
            if self.timemap[key][mid][0] == timestamp:
                return self.timemap[key][mid][1]
            elif self.timemap[key][mid][0] <= timestamp:
                l = mid + 1
                result = self.timemap[key][mid][1]
            elif self.timemap[key][mid][0] >= timestamp:
                r = mid - 1
        return result

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)