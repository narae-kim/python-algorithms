# Dijkstra's algorithm
*Dijkstra's algorithm* is used to calculate the shortest path for a weighted graph, i.e.,
minimizing the total weights it takes. 
Dijkstra's algorithm works when all the weights are positive.

* With Dijkstra's algorithm, each edge in the graph has a number associated with it. These are called *weights*.
* A graph with weights is called a *weighted graph*. A graph without weights is called an *unweighted graph*.
  - To calculate the shortest path in an unweighted graph, use *breadth-first search*. 
* The key idea behind Dijkstra's algorithm is 
"*Look at the cheapest node on your graph. There is no cheaper way to get to that node!*"
* Negative-weighted edges break Dijkstra's algorithm.
  - It is against the assumption of Dijkstra's algorithm that once you process a node, it means there is no cheaper way to get to that node.
  - The *Bellman-Ford algorithm* is for finding the shortest path in a graph that has negative-weight edges.
  

*Steps*:

Before you start, make a table of the cost for each node. 
(The *cost* of a node is how much it takes to get to that node from the start.)
To calculate the final path, you also need a *parent* column on this table.
1. Find the (next) "cheapest" node. This is the node you can get to in the least amount of weight.
   - Put down the amount of the weight taking to each node from the node.
   - When you don't know how long it takes to get to the node yet, put down infinity.
2. Check whether there is a cheaper path to the neighbors of this node. 
If so, update the costs of the neighbors of this node.
   - Calculate how long it takes to get to all of the node's neighbors by following an edge from the node.
   - When you find a shorter path for a neighbor of the node, update its cost and its parent node.
3. Repeat until you have done this for every node in the graph.
4. Calculate the final path.

To find the final path, follow the parents backward to have the complete path, i.e.,
start from the parent of the finish, and the parent of that node, and so on, until you reach the start.


*Note*: For implementation, store the neighbors and the cost for getting to that neighbor in a hash table.


## Graph
Graphs can have *cycles*. It means you can start at a node, travel around, and end up at the same node.
However, following the cycle will never give you the shortest path.

An undirected graph means that both nodes point to each other, i.e., a cycle.
With an undirected graph, each edge adds another cycle.
Dijkstra's algorithm only works with *directed acyclic graphs* (DAG).


## References
* Grokking Algorithms
