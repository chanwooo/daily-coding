from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        print(strs)
        anagram = defaultdict(list)
        for s in strs:
            k = list(s)
            k.sort()
            k = ''.join(k)
            anagram[k].append(s)

        print(anagram)

        return list(anagram.values())

print(Solution.groupAnagrams(Solution,["eat","tea","tan","ate","nat","bat"]))

