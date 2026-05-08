class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort = {}

        for i in range(len(strs)):
            temp = "".join(sorted(strs[i]))
            if temp not in sort:
                sort[temp] = []
            sort[temp].append(strs[i])

        return list(sort.values())
            

        print(sort)


      

