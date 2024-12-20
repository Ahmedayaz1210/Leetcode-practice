'''
UNDERSTAND:
- Inputs: Array of string letters which are assumed to be a cpu task and an int number n which is the waiting time before doing the same letter task.
- Have to pick a letter, do that task and wait n number of intervals until we can do that letter again if it exists, between that interval we can either do another task of different letter or do nothing which is "idle"
- Output: Return number of intervals it takes to finish all tasks
- TC? SC?
- size of tasks 1 <= tasks.length <= 104
- size of n 0 <= n <= 100
- tasks[i] is an uppercase English Letter
- Guaranteed at least one task but interval can be 0 so in that case a task can be repeated right after doing it

MATCH:
- Will need Counter to count how many times each letter exists
- Can use a max heap to apply our greedy approach and pick the one with highest frequency each time
- Will also need a cooling down list which can temporaily hold each task until its cooling down

PLAN:
- Loop over tasks and count each task's occurences
- Now only store the frequencies in the max heap because we are returning output as just the minimum integer and not as a string output showing which goes first and which goes so on
- Heapify the max heap
- Initialize time = 0, result = 0 and cooling_down queue.
- Run a loop until both max heap and cooling down queue are not empty
    - if cooling_down has something in it:
        - if time == cooling_down's first's cooling_down period:
            - Take it out and push to heap, just the frequency
    - if max heap has smth
        - Pop out from max heap
        - Reduce frequency by 1
        - if frequency > 1
            - Put in cooling down queue as a tuple, add cooling down period to the tuple as time + n + 1
    - Increase result by 1
    - Increase time by 1
- Return result
'''
from collections import Counter
from heapq import heapify, heappush, heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)

        max_heap = list(counter.values())

        max_heap = [-x for x in max_heap]

        heapify(max_heap)

        time, result, cooling_down = 0, 0, []


        while max_heap or cooling_down:
            if cooling_down:
                if cooling_down[0][1] == time:
                    cooled_down = cooling_down.pop(0)
                    heappush(max_heap, cooled_down[0])
            if max_heap:
                frequency = -heappop(max_heap)
                frequency -= 1
                if frequency >= 1:
                    cooling_down.append([-frequency, time + n + 1])
            result += 1
            time += 1

        return result