# Some examples with D&C algorithms.


def sum_element_in_array(array):
    """
    Add up all the element in the array.
    """
    if len(array) == 0:
        return 0
    else:
        return array[0] + sum_element_in_array(array[1:])


def count_element_in_array(array):
    """
    A recursive function to count the number of elements in an array.
    """
    if not array:  # array == []
        return 0
    return 1 + count_element_in_array(array[1:])


def max_in_array(array):
    """
    Find the maximum number in an array.
    """
    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    sub_max = max_in_array(array[1:])
    return array[0] if array[0] > sub_max else sub_max


if __name__ == '__main__':
    test_array = [1, 2, 3, 4]
    print(sum_element_in_array(test_array))
    print(count_element_in_array(test_array))
    print(max_in_array(test_array))
