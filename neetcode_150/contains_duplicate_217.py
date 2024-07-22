# Return true if any value appears at least twice
from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))


# Leetcode tests
input_1 = [1, 2, 3, 1]
input_2 = [1, 2, 3, 4]
input_3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
contains_duplicate(input_1)  # True
contains_duplicate(input_2)  # False
contains_duplicate(input_3)  # True
