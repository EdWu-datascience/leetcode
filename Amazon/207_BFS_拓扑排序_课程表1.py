class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #先初始化每个课程的入度
        #numCourses = 4
        #prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        in_degree = [0 for _ in range(numCourses)]
        print(in_degree)
        for a,b in prerequisites:
            in_degree[a] += 1
        print(in_degree)
        #初始化关系图
        adj = [set() for _ in range(numCourses)]
        print(adj)
        for value in prerequisites:
            adj[value[1]].add(value[0])
        print(adj)
        #创建队列和存放结果的空数组
        queue = []
        re = []
        #将入度为零的点先存入队列
        for index,value in enumerate(in_degree):
            if value == 0:
                queue.append(index)
        #先判断下queue是否仍然为空，如果为空说明不存在任何线性关系
        if len(queue) == 0:
            return False
        while queue:
            temp = queue.pop(0)
            re.append(temp)
            for value in adj[temp]:
                in_degree[value] -= 1
                if in_degree[value] == 0:
                    queue.append(value)
        if len(re) == numCourses:
            return True
        else:
            return False