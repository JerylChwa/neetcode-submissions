import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x : x[1])
        min_heap = [] # Stores departure times (time, count)
        global_count = 0

        for count, start_time, end_time in trips:

            while min_heap and start_time >= min_heap[0][0]:
                global_count -= min_heap[0][1]
                heapq.heappop(min_heap)

            global_count += count
            heapq.heappush(min_heap, (end_time, count))

            if global_count > capacity:
                return False

        return True



        
        