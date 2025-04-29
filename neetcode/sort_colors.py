from typing import DefaultDict


def sort_colors(nums):
    colors = DefaultDict(int)
    for num in nums:
        colors[num]+=1

    res = []
    for key in sorted(colors.keys()):
        res = res + [key for i in range(0,colors[key])]

    return res

def sort_colors_ext(nums):
    i, j, k = -1, len(nums), 0
    while k < j:
        if nums[k] == 0:
            i += 1
            nums[i], nums[k] = nums[k], nums[i]
            print("i",i,k)
            k += 1
        elif nums[k] == 2:
            j -= 1
            nums[j], nums[k] = nums[k], nums[j]
            print("j",j,k)
        else:
            k += 1
    return nums

if __name__ == "__main__":
    print(sort_colors_ext([2,0,2,1,1,0]))
