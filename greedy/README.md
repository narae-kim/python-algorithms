# Greedy Algorithm
*Greedy algorithm* is for the occasions that you need to solve the problem pretty well, but not necessarily perfect, in a simple way. 
Greedy algorithm is also called an *approximation algorithm*.
When calculating the exact solution will take too much time, an approximation algorithm will work.

The aim for the greedy algorithm is that 
*at each step you pick the locally optimal solution, and in the end you are left with the globally optimal solution*.


Approximation algorithms are judged by
* How fast they are
* How close they are to the optimal solution

Approximation algorithms are useful for the NP-complete problems where you calculate every possible solution and pick the shortest one, e.g., in *O(n!)* time.

*Note*: Breadth-first search and Dijkstra's algorithm are greedy algorithms.


## Examples
### The knapsack problem
By the approximation algorithm,
1. Pick the most expensive thing that will fit in the knapsack.
2. Pick the next most expensive thing that will fit in the knapsack, and so on.

Not always guaranteed to maximize the value of the items you put in the knapsack.
The greedy strategy does not give you the optimal solution, but it gets you pretty close.


### The set-covering problem
To cover all 50 states with the minimum number of radio stations where a radio station can cover more than one state.

To find the optimal solution with the exact algorithm,
1. List every possible subset of stations (NP-complete).
This is called the *power set*. There are *2^n* possible subsets.
2. From these, pick the set with the smallest number of stations that covers all 50 states.

To calculate every possible subset of stations, it takes **O(2^n)** time because there are *2^n* stations.
It is impossible to compute the correct solution for the NP complete problems if you have a large number *n*.


With the greedy algorithm, we can solve the question simply for the answer pretty close to the optimal answer.
1. Pick the station that covers the most states that haven't been covered yet.
It is okay if the station covers some states that have been covered already.
2. Repeat until all the states are covered.

With the greedy algorithm, it takes **O(n^2)** time, where *n* is the number of radio stations.


### The traveling salesperson problem
A salesperson needs to visit *n* number of cities. The aim is to minimize the traveling distance. 

One approach is to look at every possible order in which the person could travel to the cities (NP-complete).
This NP-complete problem takes factorial time, **O(n!)**.
So, it is impossible to compute the correct solution if you have a large number cities.

By the approximation algorithm, firstly, arbitrarily pick a start city.
Then, each time the salesperson has to pick the next city to visit by picking the closest unvisited city.


## References
* Grokking Algorithms
