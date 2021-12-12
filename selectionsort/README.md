# Selection sort
To sort a list in a certain order, we can read all the elements and create a new list in order.
For example, sorting a list of playlists from most to least played can start from reading the list to find the most played, and then remove the element from the list and insert it to the new list, and so on.

***Running time***:

Firstly, reading the whole array takes *O(n)*. Similarly, remove an element or add it to a new array takes *O(n)*.
Then, the operation needs to repeat *n* times.

Selection sort takes **O(n^2)** time for any array of *n*.

*Note*: Quicksort is a faster sorting algorithm that only takes *O(n log n)*.


## Examples
- Sorting names in a phone book.
- Sorting travel dates.
- Sorting emails from newest to oldest.


## References
* Grokking Algorithms
