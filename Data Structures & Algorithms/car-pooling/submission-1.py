"""
Convert trips to 2 different events

Start : (timestamp, positive_count)
End : (timestamp, negative_count)

Sorting naturally prioritises end events

Can just sweep through and keep track of a rolling count
"""

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        parsed_trips = []

        for count, start, end in trips:
            parsed_trips.append((start, count))
            parsed_trips.append((end, -count))

        parsed_trips.sort()

        global_count = 0

        for _, cur_count in parsed_trips:
            global_count += cur_count
            if global_count > capacity:
                return False
        
        return True