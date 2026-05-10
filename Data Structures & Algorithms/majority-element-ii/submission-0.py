class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        elements = Counter(nums)

        for num, count, in elements.items():
            if count > len(nums) // 3:
                res.append(num)
        return res
        