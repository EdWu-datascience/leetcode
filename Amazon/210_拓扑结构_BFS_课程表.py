class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        #需要完成n门课程，在顺序选择时先选择在[ai,bi]中bi位置出现频率最大
        #上面贪心的思想：每一步最优，则全局最优(并不是真的全局最优)
        #先计算每门课的入度
        #numCourses = 4
        #prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        in_degree = [0 for _ in range(numCourses)]  
        #存放入度的值(入度指的是选择该课要完成的先修课数量)
        for value in prerequisites:
            in_degree[value[0]] += 1
        print(in_degree)#index代表课程号，index对应的value代表该课程的入度
        adj = [set() for _ in range(numCourses)]
        #adj存放关系图,index代表的是课程号，value(set)代表的是该课程指向的其他课程序号
        for second,first in prerequisites:
            adj[first].add(second)
        print(adj) 
        queue = []
        re = []
        #先把入度为零的课程号存入queue中(先进先出)
        for index,value in enumerate(in_degree):
            if value == 0:
                queue.append(index)
        while queue:
            #先进先出
            temp1 = queue.pop(0)#temp1为入度为0的课程号的值
            re.append(temp1)
            for value in adj[temp1]:#value 现在存放的是temp1指向的其他课程序号
                #先对其他的课程需要的入度减一操作
                print(value)
                in_degree[value] -= 1
                if in_degree[value] == 0:
                    queue.append(value)
        print(re)
        if len(re) != numCourses:
            return []
        else:
            return re 