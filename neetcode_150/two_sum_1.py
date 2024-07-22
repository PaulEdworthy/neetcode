# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    h_map = {}
    
    for i, num in enumerate(nums):
        diff = target - num
        if diff in h_map:
            return [h_map[diff], i]
        else:
            h_map[num] = i
             

input_num = [15, 11, 7, 2]
target_num = 9

two_sum(input_num, target_num)
