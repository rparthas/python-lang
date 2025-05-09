import heapq
from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        mod_stones = [-x for x in stones]
        heapq.heapify(mod_stones)
        while len(mod_stones) > 1 :
            num1 = heapq.heappop(mod_stones)
            num2 = heapq.heappop(mod_stones)
            if num1 != num2:
                heapq.heappush(mod_stones,-abs(num1-num2))

        if mod_stones:
            return -mod_stones[0]

        return 0

if __name__ == "__main__":
    stones=[2,3,6,2,4]
    solution = Solution()
    print(solution.lastStoneWeight(stones))
