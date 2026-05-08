class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1

        counts = sorted(freq.items(), key = lambda x: x[1], reverse = True)

        result = []
        for i in range(k):
            num, frequency = counts[i]
            result.append(num)


        return result


    
            



        

        
                

        