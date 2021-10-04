

'''
description of proble: number n represent the number of pairs for generated brackeds
we need to generate all possible result for i == n and we need valid bracket pair 
core ideal:
the final result for i == n is 
"("+ the result when i == p + ")" + the result when i == q 
and p + q == n-1
'''






class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #递归(recursion)暴力解法，number==n,生成长度为2n，因此生成长度为2n的括号等价于生成长度为
        #第一个字符加上生成长度为2n-1个字符，而生成长度2n-1个字符是和原问题具有相同结构的子问题
        #递归的跳出条件：当生成的长度等于2n时，判断是否符合条件，如果符合则加入最终的结果
        def valid(re):
            #balance == 0,如果遇到左括号balance+1,else balance-1
            #如果balance<0,则表示括号是invalid的
            balance = 0
            for i in re:
                if i == '(':
                    balance = balance+1
                else:
                    balance = balance-1
                if balance < 0:
                    return False
            if balance != 0:
                return False
            else:
                return True
        def generateall(current):
            if len(current)==2*n:
                if valid(current) == True:
                    #result.append(current)
                    #current是类似['(', '(', '(', ')', ')', ')']
                    result.append("".join(current))
            else:
                current.append('(')
                generateall(current)
                current.pop()
                current.append(')')
                generateall(current)
                current.pop()
        result = []
        generateall([])
        return result



        #动态规划思想解法
        
        if n == 0:
            return []
        total = []
        #对应于n==0
        total.append([None])
        #对应于n==1
        total.append(['()'])
        for L in range(2,n+1):
            #存储最终结果的list
            Lth_result = []
            #分别得到 p q时的结果
            for J in range(0,L):
                #得到i=p时的括号排列组合
                p_result = total[J]
                #得到i=q时的括号排列组合
                q_result = total[L-1-J]
                for P in p_result:
                    for Q in q_result:
                        if P == None:
                            P = ''
                        if Q == None:
                            Q = ''
                        m = '(' + P + ')' + Q 
                        Lth_result.append(m)
            total.append(Lth_result)
        print(total[-1])
        return total[-1]
        
