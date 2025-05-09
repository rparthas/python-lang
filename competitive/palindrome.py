class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = list(filter(str.isalnum, s.lower()))
        return filtered_chars == list(reversed(filtered_chars))


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(solution.isPalindrome("race a car"))  # False
