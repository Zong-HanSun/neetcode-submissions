class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left: List[int], right: List[int]) -> List[int]:
            l,r, = 0,0
            merged_array = []
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    merged_array.append(left[l])
                    l += 1
                else:
                    merged_array.append(right[r])
                    r += 1
            
            while l < len(left):
                merged_array.append(left[l])
                l += 1
            while r < len(right):
                merged_array.append(right[r])
                r += 1

            return merged_array

        def divide(arr: List[int]) -> List[int]:
            if len(arr) == 1:
                return arr

            mid = len(arr) // 2
            left_subarray = arr[:mid]
            right_subarray = arr[mid:] 

            sorted_left_half = divide(left_subarray)   
            sorted_right_half = divide(right_subarray)
            return merge(sorted_left_half, sorted_right_half)

        return divide(nums)





        

                
                

            


        