from math import ceil
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(key=lambda c: c[0], reverse=True)
        stack = []

        for c in cars:
            pos, spd = c
            time = (target - pos) / spd
            if stack and stack[-1] >= time:
                continue
            stack.append(time)

        return len(stack)