class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for word in words:
            if word not in freq.keys():
                freq[word] = 1
            else:
                freq[word] += 1
        freq = sorted(freq.items(),key = lambda item:item[1],reverse=True)
        count = 0
        re = []
        print(freq)
        freq = sorted( freq, key = lambda x : (-x[1],x[0]))
        print(freq)
        for key in freq:
            re.append(key[0])
            count += 1 
            if count == k:
                break
        return re 