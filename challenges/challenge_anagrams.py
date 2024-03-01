def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def is_anagram(first_string, second_string):

    list_first_string = quick_sort(list(first_string.lower()))
    list_second_string = quick_sort(list(second_string.lower()))

    result_first = "".join(list_first_string)
    result_second = "".join(list_second_string)

    if len(result_first) == 0 and len(result_second) > 0:
        return ("", result_second, False)
    if len(result_second) == 0 and len(result_first) > 0:
        return (result_first, "", False)
    if len(result_first) == 0 and len(result_second) == 0:
        return ("", "", False)
    is_anagramm = result_first == result_second
    return (result_first, result_second, is_anagramm)
