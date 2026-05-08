class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1

                elif total > 0:
                    k -= 1

                elif total == 0:
                    trip = [nums[i], nums[j], nums[k]]
                    if trip not in res:
                        res.append(trip)
                    j += 1
                    k -= 1

        return res

