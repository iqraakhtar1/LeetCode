class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = [(p, s) for p, s in zip(position, speed)] #list comprehension
        pair.sort(reverse=True)
#         stack = []
#         for p, s in pair:  # Reverse Sorted Order
#             stack.append((target - p) / s) #calculating time for each car
#             if len(stack) >= 2 and stack[-1] <= stack[-2]:
#                 stack.pop()
#         return len(stack)
# #(target - postion)/speed

        last_arrival_time = float('-inf')
        count = 0

        for p, s in pair:
            arrival_time = (target - p) / s

            if arrival_time > last_arrival_time:
                count += 1
                last_arrival_time = arrival_time

        return count