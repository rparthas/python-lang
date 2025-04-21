from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        res =[0] * (n+1)
        res[0] = 1
        carry = 1
        for i in range(n-1,-1,-1):
            result = digits[i]+carry
            res[i+1] = result%10
            carry = result//10
        if carry == 0:
            return res[1:]
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne([1,2,3]))  # Output: [1,2,4]
    print(solution.plusOne([4,3,2,1]))  # Output: [4,3,2,2]
    print(solution.plusOne([9]))  # Output: [1,0]
