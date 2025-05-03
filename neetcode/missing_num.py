def missingNumber(nums):
    xor = len(nums)
    for i in range(len(nums)):
        xor  = xor ^ i ^ nums[i]
    return xor

if __name__ == "__main__":
    print(missingNumber([0,1,5,2,3]))
