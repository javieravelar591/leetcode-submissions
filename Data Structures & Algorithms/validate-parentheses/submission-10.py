class Solution:
    def isValid(self, s: str) -> bool:
        parens =  {
            ')': '(',
            '}': '{',
            ']': '['
        }

        if len(s) < 2:
            return False

        stack = []
        for p in s:
            if p in parens:
                if stack and stack.pop() == parens[p]:
                    continue
                else:
                    return False
            else:
                stack.append(p)
        return len(stack) == 0 