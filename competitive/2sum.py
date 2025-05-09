def two_sum(nums,target):
    n = len(nums)
    for idx in range(0,n):
        search = target - nums[idx]
        l,r =0,n-1
        while l < r:
            m = (l+r)//2
            if nums[m] == search:
                return [idx+1,m+1]
            if nums[m] > search:
                r=m-1
            else:
                l=m+1

    return []



if __name__ == "__main__":
    print(two_sum([2,7,11,15],18))
