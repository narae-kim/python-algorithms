def binary_search(sorted_list, data):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = sorted_list[mid]
        if guess == data:
            return mid
        elif guess < data:
            low = mid + 1
        else:
            high = mid - 1
    return None


def binary_search_recursion(sorted_list, data, index=0):
    if len(sorted_list) == 1:
        if sorted_list[0] == data:
            return index
        else:
            return None
    else:
        mid = (len(sorted_list) - 1) // 2
        guess = sorted_list[mid]
        if guess == data:
            return index + mid
        elif guess < data:
            return binary_search_recursion(sorted_list[mid + 1:], data, index + mid + 1)
        else:
            return binary_search_recursion(sorted_list[:mid], data, index)


if __name__ == '__main__':
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(test_list, 3))
    print(binary_search(test_list, 9))
    print(binary_search(test_list, 11))

    print(binary_search_recursion(test_list, 3))
    print(binary_search_recursion(test_list, 9))
    print(binary_search_recursion(test_list, 11))
