class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        result = r

        while l <= r:
            k = (l + r) // 2
            total_weight = 0
            day_taken = 1
            for w in weights:
                if total_weight + w <= k:
                    total_weight += w
                else:
                    total_weight = w
                    day_taken += 1

            if day_taken <= days:
                result = min(result, k)
                r = k - 1
            else:
                l = k + 1

        return result


        