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

    def lcs(self, nums: List[int]) -> int:
        hm = {}
        for num in nums:
            hm[num] = False

        max_len = 1

        for num in nums:
            curr_len = 1
            if hm[num] == True:
                continue

            search = num +1
            while search in hm and hm[search] == False:
                curr_len+=1
                search+=1

            search = num -1
            while search in hm and hm[search] == False:
                curr_len+=1
                search-=1

            max_len = max(max_len,curr_len)

        return max_len
if __name__ == "__main__":
    print(Solution().longestConsecutive(nums = [0,3,2,5,4,6,1,1]))
    print(Solution().lcs(nums = [0,3,2,5,4,6,1,1]))
