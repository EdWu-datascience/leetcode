class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if "(" not in s and ")" not in s:
            return s 
        elif "(" in s and ")" not in s:
            s = s.replace("(",'',len(s))
            return s 
        elif ")" in s and "(" not in s:
            s = s.replace(')','',len(s))
            return s 
        #s = "a)b(c)d"
        #有效括号的两个条件
        #1 字符串中 “(” 的数量和 “)”的数量相等
        #2 从左至右遍历字符串，统计当前 “(” 和 “)” 的数量，永远不可能存在 “)” 的数量
        #大于 “(”的情况
        #栈：先进后出
        #如果在当前栈为空的时候遇到了当前字符为“)”，则删除“)”,防止余量为负数
        #如果在结尾时遇到字符“(”，则删除它，防止余量不为0
        stack = []#用来存储需要删除的字符的index
        S = s
        delete = []
        count = 0
        for index,value in enumerate(s):
            if value in ['(',')']:
                count += 1  
                if len(stack) == 0 and value == ")":
                    delete.append(index)
                elif value == "(":
                    #print(stack)
                    stack.append(index)
                elif s[stack[-1]] + value == "()":
                    stack.pop()
        if len(stack)!=0:
            for value in stack:
                delete.append(value)
        print(delete)
        print(count)
        if len(delete) == count:
            return ""
        re = []
        for index,value in enumerate(s):
            if len(delete)!=0:
                if index == delete[0]:
                    re.append(0)
                    delete.pop(0)
                else:
                    re.append(value)
            else:
                re.append(value)
        print(re)
        final = ''
        for value in re:
            if value !=0:
                final += value 
        return final