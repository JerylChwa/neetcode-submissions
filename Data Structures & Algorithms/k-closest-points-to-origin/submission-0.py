class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
            minHeap.append([x**2 + y**2, x, y])
        
        heapq.heapify(minHeap)
        output = []

        while len(output) < k:
            distance, x, y = heapq.heappop(minHeap)
            output.append([x, y])

        return output
