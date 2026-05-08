class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for i in range(len(strs)):
            temp = "".join(sorted(strs[i]))
            if temp not in anagram:
                anagram[temp] = []
            anagram[temp].append(strs[i])
        return list(anagram.values())
            


      

