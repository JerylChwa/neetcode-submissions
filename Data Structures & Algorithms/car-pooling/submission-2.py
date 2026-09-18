class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        start = end = 0

        for count, s, e in trips:
            start = min(start, s)
            end = max(end, e)

        cover = end - start + 1

        delta = [0 for _ in range(cover + 1)]

        for count, s, e in trips:
            delta[s-start] += count
            delta[e-start] -= count

        
        global_count = 0
        for d in delta:
            global_count += d
            if global_count > capacity:
                return False
        
        return True

