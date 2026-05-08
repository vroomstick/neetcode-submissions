class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            temp ="".join(sorted(s))
            anagrams[temp].append(s)
        return list(anagrams.values())

      

