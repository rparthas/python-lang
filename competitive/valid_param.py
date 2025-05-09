class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(',  '{', '[']:
                stack.append(c)
            if not stack:
                return False
            if c==']' and  stack.pop() !='[':
                return False
            if c=='}' and stack.pop() !='{':
                return False
            if c==')' and stack.pop() !='(':
                return False

        return not stack

if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("([{}])"))
