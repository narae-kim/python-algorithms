# Quick Sort
Quicksort is a sorting algorithm, and a much faster one than selection sort. It is frequently used in real life.

Quicksort uses *Divide and Conquer* (D&C) technique which is a well-known recursive technique for solving problems.

Base case: 
- Empty arrays or arrays with one element.

Recursive case:
- Pick a *pivot* element from the array.
- *Partitioning*
  - A sub-array of all the numbers less than the pivot.
  - The pivot.
  - A sub-array of all the numbers greater than the pivot.
  
A sorted array: Combination of the left array + pivot + right array.


***Running time***:

The speed of quicksort depends on the pivot you choose.

On average (or in the best case), quicksort takes **O(n log n)**.

In the worst case, quicksort takes **O(n^2)**.

If you always choose a random element in the array as the pivot, quicksort will complete in *O(n log n)* time on average.
Quicksort is one of the fastest sorting algorithms, and it is a very good example of D&C.


*Note*: *Merge sort* also takes *O(n log n)*.


## Divide and conquer (D&C) algorithm
D&C algorithms are recursive algorithms.

Approaches:
1. Figure out the base case. This should be the simplest possible case.
2. Divide and decrease your problem until it becomes the base case.

According to D&C, with every recursive call you have to reduce your problem.

*Code example* - A common approach to sum all the numbers and return the total:
```python
def sum(array):
    total = 0
    for x in array:
        total += x
    return  total
```

*Code example* - A D&C approach to sum all the numbers and return the total:
```python
def sum(array):
    if len(array) == 0:
        return 0
    else:
        return array[0] + sum(array[1:])
```

- When you are writing a recursive function involving an array, the base case is often an empty array or an array with one element.


### Binary search
Binary search is a D&C algorithm. 

The base case for binary search is an array with one item.
If the item you are looking for matches the item in the array, you found it. Otherwise, it is not in the array.

In the recursive case for binary search, split the array in half, throw away one half, and call binary search on the other half.


## References
* Grokking Algorithms
