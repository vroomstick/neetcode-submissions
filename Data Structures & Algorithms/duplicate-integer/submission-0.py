class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashNums = {}
        for i in range(len(nums)):
            if nums[i] not in hashNums:
                hashNums[nums[i]] = 1
            else:
                hashNums[nums[i]] += 1
        ##print(hashNums)

        for num in hashNums:
            if hashNums[num] > 1:
                return True
        return False
            
                


