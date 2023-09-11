#tag:frequency
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter =  collections.Counter(nums)
        freqList = [[] for i in range(len(nums)+1)]
        for key, freq in counter.items():
            freqList[freq].append(key)
        
        result = []
        for i in range(len(freqList)-1, -1,-1):
            elemList = freqList[i]
            if len(result) + len(elemList) < k:
                result+=elemList
            else:
                result +=elemList[:k-len(result)]
            
        return result