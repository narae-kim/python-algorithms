# NP Complete
*NP-completeness*: some problems are famously hard to solve.

The NP-complete problems are where you calculate every possible solution and pick the shortest one.
It is impossible to compute the correct solution for the NP complete problems if you have a large number of items.

*Note*: For NP-complete problems, try the greedy algorithm (approximation algorithm) instead of trying to solve the problem perfectly.


## How do you tell if a problem is NP-complete?
For example, finding the shortest path that connects several points is NP-complete 
opposed to Breadth-first search or Dijkstra's algorithm where there are only the start and the finish.

- When the algorithm runs quickly with a handful of items but really slows down with more items.
- "All combinations of X" usually point to an NP-complete problem.
- If you have to calculate "every possible version" of X because you cannot break it down into smaller sub-problems, it might be NP-complete.
- If the problem involves a sequence, and it is hard to solve, it might be NP-complete.
- If the problem involves a set and it is hard to solve, it might be NP-complete.
- If you restate the problem as the set-covering problem or the traveling-salesperson problem, then the problem is definitely NP-complete.


## Examples
### The traveling salesperson problem
A salesperson needs to visit *n* number of cities. The aim is to minimize the traveling distance. 

One approach is to look at every possible order in which the person could travel to the cities.

***Running time***
* Factorial time: **O(n!)**
* It is impossible to compute the correct solution for the NP complete problems if you have a large number of cities.


### The set-covering problem
To cover all 50 states with the minimum number of radio stations where a radio station can cover more than one state.

To find the optimal solution with the exact algorithm,
1. List every possible subset of stations (NP-complete).
This is called the *power set*. There are *2^n* possible subsets.
2. From these, pick the set with the smallest number of stations that covers all 50 states.

***Running time***
* To calculate every possible subset of stations, it takes **O(2^n)** time because there are *2^n* stations.
* It is impossible to compute the correct solution for the NP complete problems if you have a large number *n*.


## References
* Grokking Algorithms