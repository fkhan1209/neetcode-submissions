class Solution:
    def isValid(self, s: str) -> bool:
        chars = {'[': ']', '{': '}', '(': ')'}
        res = []
        for elem in s: 
            if elem in chars.keys():
                res.append(elem)
            else:
                if res and elem == chars[res[-1]]:
                    res.pop()
                else:
                    return False
        return True if not res else False
