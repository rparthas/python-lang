class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r =0,0
        cm = {}
        max_cnt = 0
        for r in range(len(s)):
            if s[r] in cm:
                l = max(l,cm[s[r]]+1)
            cm[s[r]] = r
            max_cnt= max(r-l+1,max_cnt)

        return max_cnt




if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("pwwkew"))  # Output: 3
