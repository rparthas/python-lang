from typing import List
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        q = len(queries)
        def can_be_zeroed(k: int) -> bool:
            if k == 0:
                return all(x == 0 for x in nums)
            diff = [0] * (n+1)
            for i in range(k):
                l, r, val = queries[i]
                diff[l]+=val
                if n >= r+1:
                    diff[r+1] -= val

            current_decrement = 0
            for i in range(n):
                current_decrement += diff[i]
                if current_decrement < nums[i]:
                    return False
            return True

        low = 0
        high = q
        ans = -1

        while low <= high:
            mid = low + (high - low) // 2
            if can_be_zeroed(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Given example
    result = sol.minZeroArray(nums=[2, 0, 2], queries=[[0, 2, 1], [0, 2, 1], [1, 1, 3]])
    assert result == 2, f"{result} was returned instead of 2"

    # Test Case 2: Simple case - can make zero in 1 query
    result = sol.minZeroArray(nums=[1, 1, 1], queries=[[0, 2, 1]])
    assert result == 1, f"{result} was returned instead of 1"

    # Test Case 3: Impossible to make zero
    result = sol.minZeroArray(nums=[3, 3, 3], queries=[[0, 1, 1], [1, 2, 1]])
    assert result == -1, f"{result} was returned instead of -1"

    # Test Case 4: Already zero
    result = sol.minZeroArray(nums=[0, 0, 0], queries=[[0, 2, 1]])
    assert result == 0, f"{result} was returned instead of 0"

    # Test Case 5: Need all queries
    result = sol.minZeroArray(nums=[3, 2, 4], queries=[[0, 0, 3], [1, 1, 2], [2, 2, 4]])
    assert result == 3, f"{result} was returned instead of 3"

    # Test Case 6: Overlapping queries
    result = sol.minZeroArray(nums=[5, 5, 5], queries=[[0, 1, 2], [1, 2, 2], [0, 2, 3]])
    assert result == 3, f"{result} was returned instead of 3"

    # Test Case 7: Single element
    result = sol.minZeroArray(nums=[10], queries=[[0, 0, 5], [0, 0, 4], [0, 0, 2]])
    assert result == 3, f"{result} was returned instead of 3"

    # Test Case 8: Larger array
    result = sol.minZeroArray(nums=[1, 2, 3, 4, 5],
                                queries=[[0, 4, 1], [0, 2, 1], [2, 4, 2], [0, 1, 1]])
    assert result == -1, f"{result} was returned instead of 3"

    # Test Case 9: Complex pattern requiring specific query sequence
    result = sol.minZeroArray(nums=[3, 3, 2, 2],
                                queries=[[0, 1, 2], [2, 3, 1], [0, 3, 1], [1, 2, 2]])
    assert result == 3, f"{result} was returned instead of 3"

    # Test Case 10: Exactly enough queries
    result = sol.minZeroArray(nums=[10, 20, 30],
                                queries=[[0, 0, 10], [1, 1, 20], [2, 2, 30]])
    assert result == 3, f"{result} was returned instead of 3"

    # Test Case 11: Require partial use of query values
    result = sol.minZeroArray(nums=[1, 2, 3],
                                queries=[[0, 2, 5], [0, 2, 10]])
    assert result == 1, f"{result} was returned instead of 1"

    print("All test cases passed!")
