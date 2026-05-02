class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair position and speed, then sort by position descending (closest to target first)
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = [] # This will store the arrival times of the fleets
        for p, s in cars:
            arrival_time = (target - p) / s
            
            # If the current car arrives LATER than the fleet in front of it,
            # it starts a NEW fleet. 
            if not stack or arrival_time > stack[-1]:
                stack.append(arrival_time)
            
            # If arrival_time <= stack[-1], it catches up and joins 
            # the existing fleet. We do nothing (it's absorbed).
                
        return len(stack)