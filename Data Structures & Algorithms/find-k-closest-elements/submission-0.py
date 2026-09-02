class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []

        l, r = 0, len(arr) - 1
        window_size = r - l + 1

        while window_size > k:
            if abs(arr[l] - x) < abs(arr[r] - x):
                r -= 1
            elif abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            else:
                if arr[l] < arr[r]:
                    r -= 1
                else:
                    l += 1
            window_size = r - l + 1
        
        while l <= r:
            res.append(arr[l])
            l += 1

        return res


