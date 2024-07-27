class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}
        freq =[[] for i in range(len(nums)+1)]
        for n in nums:
            count[n] =1+count.get(n,0)
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
    

        # O(n)

        # dic = {}

        # for n in nums:
        #     if n in dic:
        #         dic[n] += 1
        #     else:
        #         dic[n] = 1

        # minHeap = []

        # for val, freq in dic.items():
        #     heappush(minHeap, (freq, -1*val))
        
        # ans = []
        # while minHeap:
        #     freq, val = heappop(minHeap)

        #     for i in range(freq):
        #         ans.append(-1*val)
        
        # return ans