class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stck = []
        res = 0 
        for op in operations:
            if op == '+':
                stck.append(stck[-2] + stck[-1])
                res += stck[-1]
            elif op == 'D':
                stck.append(2 * stck[-1])
                res += stck[-1]
            elif op == 'C':
                res -= stck[-1]
                stck.pop()
            else: 
                stck.append(int(op))
                res += stck[-1]
        return res