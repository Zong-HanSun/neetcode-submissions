class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_map = {}

        for task in tasks:
            if task in freq_map:
                freq_map[task] += 1
            else:
                freq_map[task] = 1
        
        max_heap = []
        
        for freq in freq_map.values():
            max_heap.append(freq)
        
        heapq.heapify_max(max_heap)

        time = 0
        queue = deque()
        
        while max_heap or queue:
            time += 1
            if max_heap:
                freq = heapq.heappop_max(max_heap) - 1
                if freq != 0:
                    queue.append([freq, time + n])
                
            if queue:
                if queue[0][1] <= time:
                    heapq.heappush_max(max_heap, queue.popleft()[0])
                
        
        return time




        