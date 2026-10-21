class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        num_frequency = defaultdict(list)
        for num in nums:
            if num in num_frequency:
                num_frequency[num] +=1
            else:
                num_frequency[num] = 1
        import heapq
        heap = []
        for key, value in num_frequency.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [value for key, value in heap]
              
