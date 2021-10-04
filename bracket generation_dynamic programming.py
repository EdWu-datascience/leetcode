class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
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
