class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, speed) for pos, speed in zip(position, speed)]
        cars.sort(key=lambda car: car[0], reverse=True)

        stack = []
        for car in cars:
            time = int(target - car[0]) / car[1]
            if stack and time <= int(target - stack[-1][0]) / stack[-1][1]:
                continue
            else:
                stack.append(car)

        return len(stack)