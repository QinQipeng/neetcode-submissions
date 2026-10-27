class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, spd) for pos, spd in zip(position, speed)]
        cars.sort(key=lambda c: c[0], reverse=True)
        stack = []
        for c in cars:
            time = (target - c[0]) / c[1]
            if (stack and time <= stack[-1]):   # Thew new car takes less or equal to the time of the previous car to each destination -> faster than the previous car -> will catchup eventually and form a fleet
                continue
            else:
                stack.append(time) # the time that a particular fleet will reach target
        return len(stack)