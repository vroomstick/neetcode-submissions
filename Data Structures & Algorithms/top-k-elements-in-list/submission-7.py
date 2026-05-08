import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        heap = []
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1

        for num, count in freq.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        for count, val in heap:
            result.append(val)

        return result

        

        
            
        


    
            



        

        
                

        