import heapq
from collections import defaultdict, Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        
        freq = Counter(s)
                
        max_heap = [
            (-cnt, letter)
            for letter, cnt in freq.items()
        ]
        heapq.heapify(max_heap) # O(N) operation

        letter = []
        prev = None # (-count, letter)

        while max_heap or prev:
            if not max_heap:
                return ""
            
            cur_count, cur_letter = heapq.heappop(max_heap)
            cur_count = abs(cur_count)

            letter.append(cur_letter)

            cur_count -= 1

            if prev is not None:
                heapq.heappush(
                    max_heap,
                    prev
                )
                prev = None

            if cur_count > 0:
                prev = (-cur_count, cur_letter)
            

        return "".join(letter)


        
        