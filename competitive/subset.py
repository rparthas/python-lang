from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [subset + [num] for subset in res]

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.subsets([1,2,3,4]))
