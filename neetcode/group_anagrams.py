from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        print("res", res)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
    
# Test the function
if __name__ == "__main__":
    solution = Solution()
    test_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = solution.groupAnagrams(test_strs)
    print(result)  # Expected output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]