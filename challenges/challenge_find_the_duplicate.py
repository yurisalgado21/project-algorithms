from collections import Counter


"""def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums) // 2]
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

"""


def conditions(nums):
    if len(nums) == 0 or len(nums) == 1:
        return False
    for num in nums:
        if isinstance(num, str) or num < 0:
            return False


def find_duplicate(nums):
    try:
        if conditions(nums) is False:
            return False
        result = Counter(nums)
        if result.most_common(1)[0][1] == 1:
            return False
        return result.most_common(1)[0][0]
    except AssertionError:
        raise AssertionError
