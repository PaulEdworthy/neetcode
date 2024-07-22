# return the index of the target, else return -1

from typing import List


def search(nums: List[int], target: int):
    start = 0
    end = len(nums) - 1
    while start <= end:
        # this improves efficiency over start + end // 2 somehow
        mid = start + (end - start) // 2

        if target == nums[mid]:
            # print(f'Found it at index: {mid}')
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    # print('Not found')
    return -1


nums_1 = [-1, 0, 3, 5, 9, 12]
target_1 = 9
# Output: index 4

nums_2 = [-1, 0, 3, 5, 9, 12]
target_2 = 2
# Output: -1

search(nums_1, target_1)
search(nums_2, target_2)
