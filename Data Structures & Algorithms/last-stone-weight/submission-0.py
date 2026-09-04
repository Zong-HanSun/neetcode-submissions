class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = stones
        heapq.heapify_max(max_heap)

        while len(max_heap) > 1:
            a = heapq.heappop_max(max_heap)
            b = heapq.heappop_max(max_heap)
            result = a - b
            if result != 0:
                heapq.heappush_max(max_heap, result)
            
        if max_heap:
            return max_heap[0]
        else:
            return 0
