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
                else: #Has to add this in case stack starts with a non opening bracket or has an odd number of elements
                    return False
        return True if not res else False
