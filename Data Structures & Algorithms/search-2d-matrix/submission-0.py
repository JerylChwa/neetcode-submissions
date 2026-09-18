class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1

        length = len(matrix[0])

        target_row = None

        while start <= end:
            mid = start + (end-start) // 2

            if target <= matrix[mid][length-1] and target >= matrix[mid][0]:
                # conduct binary search on the 'mid' row
                target_row = mid
                break
            elif target < matrix[mid][0]:
                end = mid -1
            elif target > matrix[mid][length-1]:
                start = mid + 1
        
        

        if target_row == None:
            return False
        else:
            left = 0
            right = length - 1

            while left <= right:
                mid = left + (right-left)//2

                if matrix[target_row][mid] == target:
                    return True
                elif matrix[target_row][mid] < target:
                    left = mid + 1
                elif matrix[target_row][mid] > target:
                    right = mid -1 
            return False