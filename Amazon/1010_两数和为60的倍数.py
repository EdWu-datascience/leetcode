class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        #如果两个数的模相加为60，则这两个数相加是60的倍数
        re = []
        freq = {}
        for i in range(len(time)):
            #如果数字本身可以被60整除的话，余数结果是零，因此我们人为的赋值该状态为30
            time[i] = time[i]%60
            if time[i] in freq.keys():
                freq[time[i]] += 1
            else:
                freq[time[i]] = 1
            '''
            if time[i]%60 == 0:
                time[i] = 60
                if 60 in freq.keys():
                    freq[60] += 1
                else:
                    freq[60] = 1
            else:
                time[i] = time[i]%60
                if time[i] in freq.keys():
                    freq[time[i]] += 1
                else:
                    freq[time[i]] = 1
            '''
        print(time)
        print(freq)
        seen = []
        cnt = 0
        #key == 30 和 key == 0的要单独拿出来
        for key,value in freq.items():
            if key == 30:
                seen.append(key)
                #ant += freq[key] - 1，这个不对
                if freq[key] == 1:
                    continue
                else:
                    cnt += freq[key]*(freq[key]-1)/2#这里用排列组合
            elif key == 0:
                seen.append(key)
                if freq[key] == 1:
                    continue
                else:
                    cnt += freq[key]*(freq[key]-1)/2#这里用排列组合
            elif 60-key in freq.keys() and key not in seen and 60-key not in seen:
                seen.append(key)
                seen.append(60-key)
                print(key)
                
                cnt = cnt + freq[key] * freq[60-key]#这里是乘，不是相加
        return int(cnt)  