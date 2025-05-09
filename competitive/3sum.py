from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        n= len(nums)
        for idx in range(0,n):
            search = 0 - nums[idx]
            res = self.twoSum(nums,search)
            for r in res:
                if idx in r:
                    continue
                tmp = [nums[i] for i in r]
                tmp.append(nums[idx])
                tmp.sort()
                result.add(tuple(tmp))

        return [list(item) for item in result]

    def twoSum(self,nums:List[int],target) -> List[List[int]]:
        result = set()
        nums.sort()
        n= len(nums)
        for idx in range(0,n):
            search = target - nums[idx]
            l,r,middle = 0,n-1,n//2
            while l<r:
                if search  == nums[middle]:
                    if idx!=middle:
                        res = [idx,middle]
                        res.sort()
                        result.add(tuple(res))
                if search > nums[middle]:
                    l = middle+1
                else:
                    r = middle-1
                middle = (r+l)//2

        return list(result)

if __name__ =="__main__":
    print(Solution().threeSum( nums=[3,0,-2,-1,1,2]))
    # print(Solution().twoSum(nums=[3,0,-2,-1,1,2],target=2))
