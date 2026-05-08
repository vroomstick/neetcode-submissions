class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort = {}
        output = []
        for i in range(len(strs)):
            temp = sorted(strs[i])
            secondtemp = "".join(temp)
            if secondtemp not in sort:
                sort[secondtemp] = []
            sort[secondtemp].append(strs[i])
        return list(sort.values())


      

