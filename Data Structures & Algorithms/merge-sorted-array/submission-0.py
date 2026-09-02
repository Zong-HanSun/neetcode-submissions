class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l, r = len(nums1) - 1, len(nums2) - 1

        while r >= 0:
            nums1[l] = nums2[r]
            l -= 1
            r -= 1
        
        nums1.sort()
        

        
        
        