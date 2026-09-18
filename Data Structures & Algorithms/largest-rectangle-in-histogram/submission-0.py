class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        stack = []
        max_height = 0

        for index, height in enumerate(heights):
            if not stack:
                stack.append([index, height])
            
            if height >= stack[-1][1]:
                stack.append([index, height])
            else:
                x = None
                while stack and height < stack[-1][1]:
                    # curr_area = 
                    # height of top_stack * (current index - index of top_stack)
                    curr_area = stack[-1][1]*(index - stack[-1][0])
                    if curr_area > max_height:
                        max_height = curr_area
                    x = stack.pop()
                    
                if x:
                    stack.append([x[0], height])

        
        print(stack)
        for bar in stack:
            # [index, height]
            height = bar[1]
            curr_area = height*(length-bar[0])
            if curr_area > max_height:
                max_height = curr_area


        return max_height

                

