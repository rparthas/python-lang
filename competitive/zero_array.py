from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n+1)
        for l,r in queries:
            diff[l]+=1
            if r + 1 < n + 1:
                diff[r + 1] -= 1

        current_increment_count = 0
        for i in range(n):
            current_increment_count += diff[i]
            if current_increment_count < nums[i]:
                return False

        return True

if __name__ == "__main__":
   assert Solution().isZeroArray(nums =[1,0,1], queries = [[0,2]]) == True
   assert Solution().isZeroArray(nums = [4,3,2,1], queries = [[1,3],[0,2]]) == False
