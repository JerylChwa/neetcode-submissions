class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        def can_catch_up(a_pos, a_speed, b_pos, b_speed, target):
            time_a = (target - a_pos)/a_speed
            b_dist = time_a*b_speed + b_pos
            if b_dist >= target:
                return True
            else:
                return False
        

        stack = []
        count = 0

        # first sort the positions and its corresponding speed
        num = len(position)
        hashy = {} # sorted dict by pos, with corresponding speed
        for i in range(num):
            hashy[position[i]] = speed[i]
        keys = list(hashy.keys())
        keys.sort(reverse = True)
        sd = {i : hashy[i] for i in keys} # sorted dict
        

        # check if stack not empty and next car can catchup
        for element in sd:
            # if stack empty, push (for first element ig)
            if not stack:
                stack.append([element, hashy[element]])
            
            # next car to compare current element with
            car_infront = stack[-1]
            car_infront_pos = car_infront[0]
            car_infront_speed = car_infront[1]

            pos = element
            speed = hashy[element]
            print(hashy)
            print(stack)
            if can_catch_up(car_infront_pos, car_infront_speed, pos, speed, target):
                
                continue
            else:
                
                stack.append([pos, speed])
            
        
        return len(stack)

        
        

        



   