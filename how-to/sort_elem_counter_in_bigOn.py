class Solution:
      def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter =  collections.Counter(nums)
        freqList = [[] for i in range(len(nums)+1)]
        for key, freq in counter.items():
            freqList[freq].append(key)


see problem: 347