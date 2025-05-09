class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}
        num = n
        if num == 1:
            return True

        def sum_of_squares(num):
            acc = 0
            r = num
            for i in range(3,-1,-1):
                q = r//(10**i)
                r = r%(10**i)
                acc= acc+ (q**2)
            return acc

        while num > 1:
            num = sum_of_squares(num)
            if num == 1:
                return True
            if seen.get(num,0) != 0:
                return False
            seen[num] = 1

        return False

if __name__=="__main__":
    print(Solution().isHappy(19))
    print(Solution().isHappy(100))
    print(Solution().isHappy(101))
