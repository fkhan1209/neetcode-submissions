class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Hashs = {}
        Hasht = {}
        for char in s:
            Hashs[char] = Hashs.get(char,0) + 1
        for char in t:
            Hasht[char] = Hasht.get(char, 0) + 1 
        return (Hasht == Hashs)     
        