class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for s in strs:
            w = ''.join(sorted(s))
            if w in words:
                words[w].append(s)
            else:
                words[w] = [s]
        return list(words.values())
        