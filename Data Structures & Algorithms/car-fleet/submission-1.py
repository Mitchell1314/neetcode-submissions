class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack = []
        result= 0
        cars = sorted(zip(position, speed), reverse=True)
        for position, speed in cars:
            drive_hours = (target - position) / speed
            if len(stack) == 0 or drive_hours > stack[-1]:
                stack.append(drive_hours)
                result += 1
        return result
            

        