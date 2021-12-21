# Dynamic programming
Dynamic programming starts by solving subproblems and builds up to solving the big problem.
Dynamic programming finds the optimal solution.

Dynamic programming is useful when you are trying to optimize something given a constraint.
Dynamic programming can be used when the problem can be broken into discrete subproblems which do not depend on each other.


* Every dynamic programming algorithm starts with a grid.
* The value in the cells are usually what we are trying to optimize.
* Each cell is a subproblem. The axes are about how we you can divide the problem into subproblems.
* The row represents the current best guess for the max.
    - The estimate can never get worse than it was before.
* At every row, you can put the item at that row or the items in the rows above it.
* There is no single formula for calculating a dynamic programming solution.


More about dynamic programing:
* If you fill in the grid column-wise instead of row-wise, it could make a difference.
* If you add a smaller item, the grid has to change to account for finer granularity.
* With dynamic programming, you either take the item or not. You cannot take a fraction of an item.
    - Use a greedy algorithm in that case. 
    For example, take as much as you can of the most valuable item, and the next most valuable item, and so on.
* Dynamic programming only works when each subproblem is discrete - when it does not depend on other subproblems.
* It is possible to have up to two subproblems as the problem. 
Also, it is possible for those subproblems to have their own subproblems.


## Examples
### The knapsack problem
With a knapsack that can carry a certain weight of goods, e.g. 4, what items should you put in the knapsack so that it can have the maximum money's worth of good?


The simplest algorithm is to try every possible set of goods and find the set that gives you the most value.
In this case, the algorithm takes **O(2^n)** time because there are *2^n* possible sets for *n* items.
It will become very slow if you have a large number *n*.


With dynamic programming, start by solving the problem for smaller knapsacks, sub-knapsacks, and then work up to solving the original problem.
Create a grid with columns for knapsack sizes, e.g., from 1 to 4, and rows for each item to choose from. 
The the columns help you calculate the values of the sub-knapsacks. The grid starts out empty.

At each cell, you need to decide whether you will take the item or not - *can you make the most value?*
When you have space left over, you can use the answers to those subproblems to figure out what will fit in that space.
Each cell in the grid will contain a list of all the items that fit into the knapsack at that point.

```
CELL[i][j] = MAX of { 1. the previous MAX, value at CELL[i-1][j]
                    {         vs.
                    { 2. value of current item + value of the remaining space, CELL[i-1][j-(item's weight)]
```

* If you have a new item, add a new row at the bottom of the grid.
    - Dynamic programming keeps progressively building on the estimate.
* The order of the rows does not matter. The answer does not change.


*Note*: It is possible that the best solution does not fill the knapsack completely.


### Longest common substring
We want to guess a word when that is misspelled.

The goal is to find the longest substring that two words have in common.

1. Making the grid
    - What are the values of the cells?
        - The length of the longest substring that the two strings have in common.
    - How do you divide this problem into subproblems?
        - Find the longest substring that two words have in common
    - What are the axes of the grid?
        - The two words
    
2. Filling in each cell
    1. If the letters do not match, the value is 0.
    2. If they match, this value is *value of top-left neighbor + 1*.

```python
if word_a[i] == word_b[j]:
    cell[i][j] = cell[i - 1][j - 1] + 1
else:
    cell[i][j] = 0
```

*Note*: The final solution may not be in the last cell. The solution is the largest number in the grid.


### Longest common subsequence
For example, the words "fosh" and "fort" get the same largest number, 2, as the words "fosh" and "fish" using the longest-common-substring formula.

The *longest common subsequence*: comparing the number of letters in a sequence that the two words have in common.

1. Making the grid
    - What are the values of the cells?
        - The length of the longest subsequence that the two strings have in common.
    - How do you divide this problem into subproblems?
        - Find the longest subsequence that two words have in common
    - What are the axes of the grid?
        - The two words
    
2. Filling in each cell
    1. If the letters do not match, pick the larger value between the top and left neighbors. 
    2. If they match, this value is *value of top-left neighbor + 1*.

```python
if word_a[i] == word_b[j]:
    cell[i][j] = cell[i - 1][j - 1] + 1
else:
    cell[i][j] = max(cell[i - 1][j], cell[i][j - 1])
```


## Use cases
* To find similarities in DNA strands, the longest common subsequence is being used.
* `git diff`
* *Levenshtein distance* measures how similar two strings are. 
It is used for everything from spell-check to figuring out whether a user is uploading copyrighted data.


## References
* Grokking Algorithms
