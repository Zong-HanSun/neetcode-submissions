class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r, count = 0, len(people) - 1, 0
        while l <= r:
            space_left = limit - people[r]
            if space_left - people[l] < 0:
                count += 1
                r -= 1
            else:
                count += 1
                r -= 1
                l += 1
                
        return count
        