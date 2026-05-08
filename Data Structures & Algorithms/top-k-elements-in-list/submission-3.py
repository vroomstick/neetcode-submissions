class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result = []

        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1

        counts = list(freq.items())
        counts.sort(key = lambda x: x[1], reverse = True)

        for i in range(k):
            num, count = counts[i]
            result.append(num)

        return result

            
        


    
            



        

        
                

        