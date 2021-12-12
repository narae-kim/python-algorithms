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


if __name__ == '__main__':
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(test_list, 3))
    print(binary_search(test_list, 11))
