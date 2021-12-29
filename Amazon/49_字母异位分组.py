class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #用ASCII码表示每个字符，然后对每个单词排序，排序结果相同的即为同一个结果
        asc = []
        for word in strs:
            temp = []
            for L in word:
                temp.append(int(ord(L)))
            temp = sorted(temp)
            t = ''
            for i in temp:
                t += str(i) 
            asc.append(t)
        print(asc)
        cla = {}
        for index,value in enumerate(asc):
            if value not in cla.keys():
                cla[value] = [index]
            else:
                cla[value].append(index)
        re = []
        for key,value in cla.items():
            temp = []
            for index in value:
                temp.append(strs[index])
            re.append(temp)
        print(re)
        return re 