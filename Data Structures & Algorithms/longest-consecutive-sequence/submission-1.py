class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        seq = 0
        for num in numset:
            i = 1
            if num - 1 not in numset:
                while num + i in numset:
                    i += 1 
                if i > seq:
                    seq = i

        return seq


                
            
        
                

            


            