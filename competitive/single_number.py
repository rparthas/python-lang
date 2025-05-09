from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # res= list(sorted(nums))
        # n = len(nums)
        # for idx in range(0,n,2):
        #     if idx == n-1:
        #         return res[idx]
        #     if res[idx] != res[idx+1]:
        #         return res[idx]
        res = 0
        for num in nums:
            print(num,res,num ^ res)
            res = num ^ res

        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.singleNumber([7,6,6,7,8]))
