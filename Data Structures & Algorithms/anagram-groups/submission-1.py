class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort = {}
        for word in strs:
            temp = "".join(sorted(word))
            if temp not in sort:
                sort[temp] = []
            sort[temp].append(word)

        return list(sort.values())


      

