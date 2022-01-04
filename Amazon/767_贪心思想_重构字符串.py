class Solution:
    def reorganizeString(self, s: str) -> str:
        #s = 'aabb'
        #s = 'aaab'
        #s = "aaacccbbb"
        freq = {}
        for L in s:
            if L not in freq.keys():
                freq[L] = 1
            else:
                freq[L] += 1
        print(freq)
        import math
        freq_sorted = dict(sorted(freq.items(),key = lambda item:(-item[1],item[0])))
        key = [value[0] for value in freq_sorted.items()]
        freq = [value[1] for value in freq_sorted.items()]
        re = []
        
        if freq[0] > math.ceil(len(s)/2):
            return ""
        else:
            #每次插入两个频率最高的字母。每次插入完成后要将对应的频率减一然后重新排序
            while len(freq_sorted) >= 2:
                re.append(key[0])
                re.append(key[1])
                freq_sorted[key[0]] -= 1
                freq_sorted[key[1]] -= 1
                freq_sorted = dict(sorted(freq_sorted.items(),key = lambda item:(-item[1],item[0])))
                key = [value[0] for value in freq_sorted.items()]
                freq = [value[1] for value in freq_sorted.items()]
                print(freq_sorted)
                while 0 in freq:
                    freq_sorted.pop(key[-1])
                    freq.pop()
                    key.pop()
        print(freq_sorted)
        if len(freq_sorted) == 1:
            key = [value[0] for value in freq_sorted.items()][0]
            re.append(key)
        print(re)
        return ''.join(re)