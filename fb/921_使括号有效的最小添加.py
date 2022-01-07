class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        #s = "()))(("
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1 
        #栈先进后出
        #如果当前字符与栈顶字符匹配：即栈顶+cur == "()"
        stack = [s[0]]
        for value in s[1:]:
            if len(stack) == 0:
                stack.append(value)
                continue
            if stack[-1] + value == '()':
                stack.pop()
            else:
                stack.append(value)
        print(stack)
        return len(stack)