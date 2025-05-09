from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        max_cnt,cnt = 0,1
        for idx in range(1,len(nums)):
            if nums[idx] == nums[idx-1]:
                idx+=1
                continue
            if nums[idx] == nums[idx-1]+1:
                cnt+=1
            else:
                max_cnt = max(cnt,max_cnt)
                cnt =0
            idx+=1

        max_cnt = max(cnt,max_cnt)

        return max_cnt

if __name__ == "__main__":
    print(Solution().longestConsecutive(nums = [0,3,2,5,4,6,1,1]))
