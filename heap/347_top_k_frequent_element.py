class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        result = []
        for n in nums:
            count = counter.get(n, 0) + 1
            counter[n] = count
        
        heap = []
        for num, count in counter.items():
            ele = (count, num)
            heapq.heappush(heap, ele)
            if len(heap) > k:
                heapq.heappop(heap)
        result = [x[1] for x in heap]
        return result