class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        """
        in a hashmap, store a sorted version of the current
        word as the key, and make the value a list of the non-sorted 
        strings. return a list of the values (which are lists).

        strs = ["act","pots","tops","cat","stop","hat"]

        temp = sorted version of strs[i]

        if temp isn't in the hashmap, add it as a key and 
        initialize an empty list as the value

        else hashmap[temp].append(strs[i])

        """

        anagrams = {}

        for i in range(len(strs)):
            temp = "".join(sorted(strs[i]))
            if temp not in anagrams:
                anagrams[temp] = []
            anagrams[temp].append(strs[i])
        
        return list(anagrams.values())


      

