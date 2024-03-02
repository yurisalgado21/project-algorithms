from collections import Counter


def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums) // 2]
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def conditions(nums):
    if len(nums) == 0 or len(nums) == 1:
        return False
    for num in nums:
        if isinstance(num, str) or num < 0:
            return False


def find_duplicate(nums):
    if conditions(nums) is False:
        return False
    result = quick_sort(nums)
    result = Counter(result)
    for key, value in result.items():
        if value > 1:
            return key
    return False


print(find_duplicate([3, 1, 2, 4, 6, 5, 7, 7, 7, 8]))
