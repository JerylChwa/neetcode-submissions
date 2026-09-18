"""
a = 3, b = 4, c = 2

b, b, a, a, b, a, b, c, c

b, a, b, a, b, c, a, b, c

"""

import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        min_heap = []
        
        heapq.heappush(min_heap, (-a, "a"))
        heapq.heappush(min_heap, (-b, "b"))
        heapq.heappush(min_heap, (-c, "c"))

        output_list = []
        prev_letter = None       
        
        while min_heap:
            count, letter = heapq.heappop(min_heap)
            count = abs(count)

            if len(output_list) >= 2 and letter == output_list[-1] and letter == output_list[-2]:
                old_count, old_letter = count, letter
                if len(min_heap) == 0:
                    return "".join(output_list)
                count, letter = heapq.heappop(min_heap)
                count = abs(count)
                heapq.heappush(min_heap, (-old_count, old_letter))

            if count > 0:
                output_list.append(letter)                
                count -= 1
                if count > 0:
                    heapq.heappush(min_heap, (-count, letter))

        if len(output_list) > 0:
            return "".join(output_list)
        
        return ""

        