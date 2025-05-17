from typing import List


def combination_sum(candidates:List[int], target:int) -> List[List[int]]:
    all_combinations = []

    def dfs(index,current_combination,current_sum):
        print(index,current_combination,current_sum)

        if current_sum == target:
            all_combinations.append(current_combination)
            return

        if index >= len(candidates) or current_sum > target:
            return

        dfs(index,current_combination+[candidates[index]],current_sum+candidates[index])
        dfs(index+1,current_combination, current_sum)

    dfs(0,[],0)
    return all_combinations

if __name__ == "__main__":
   print("Answer:",combination_sum([2,3,5],5))
