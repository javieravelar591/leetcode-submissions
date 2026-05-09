class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {"+", "-", "*", "/"}
        num_stack = []
        i = 0
        while tokens:
            t = tokens.pop(0)
            if t in operands:
                cur_num = 0 if t in {"+", "-"} else 1
                a = int(num_stack.pop())
                b = int(num_stack.pop())
                if t == "+":
                    cur_num = a + b
                elif t == "-":
                    cur_num = b - a
                elif t == "*":
                    cur_num = a * b
                else:
                    cur_num = int(float(b) / a)
                num_stack.append(cur_num)
                print(num_stack)
            else:
                num_stack.append(t)
                print(num_stack)
        return int(num_stack[0])