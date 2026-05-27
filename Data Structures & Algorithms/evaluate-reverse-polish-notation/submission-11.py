class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []

        for t in tokens:
            if t not in {"+","-","*","/"}:
                res.append(int(t))
            else:
                b = res.pop()
                a = res.pop()
                if t == "+":
                    res.append(a + b)
                elif t == "-":
                    res.append(a - b)
                elif t == "*":
                    res.append(a * b)
                elif t == "/":
                    res.append(int(a / b))
        return res[0]
