class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = nums
        self.k = k
        

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort()
        
        n = 0
        
        for i in range(len(self.arr) -1, -1, -1):
            n += 1
            if n == self.k:
                return self.arr[i]

