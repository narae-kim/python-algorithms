# Hash Table
A *hash table* is a data structure that puts a hash function and an array together.

Hash tables are known as hashmaps, maps, dictionaries (Python), and associative arrays.

Hashes are good for
* Modeling relationship from one thing to another thing.
* Filtering out duplicates.
* Caching/memorizing data instead of making your server do work.


***Running time***:

- The average cases (fast)
  - Search: **O(1)** (constant time)
  - Insert: **O(1)** (constant time) 
  - Delete: **O(1)** (constant time) 

- The worst cases (slow)
  - Search: **O(n)** (linear time)
  - Insert: **O(n)** (linear time) 
  - Delete: **O(n)** (linear time) 

Avoid collisions to not get worst-case performance with hash tables.


## Hash function
**Requirements**:
- It needs to be consistent. The hash function consistently maps a key to the same index.
- The hash function maps different keys to different indexes.
- The hash function knows how big your array is and only returns valid indexes.

Ideally, a hash function would map keys evenly all over the hash.
A good hash function will give you very few collisions.

The *SHA function* is one of the greatest hash function.


## Collision
Collision is that two keys have been assigned the same slot.
If multiple keys map to the same slot, start a linked list at that slot.

Approaches to avoid collisions:
- A low load factor
- A good hash function


### Load factor
Load factor measures how many empty slots remain in the hash table.
With a lower load factor, you will have fewer collisions, and your table will perform better.

> Load factor = number of items in hash table / total number of slots

***Resizing***: once the load factor starts to grow, you need to add more slots to your hash table.
(Resize when the load factor is greater than 0.7.)
1. Create a new array, e.g., in double the size.
2. Re-insert all the items into the new hash table using the hash function.

On average, hash tables take *O(1)* even with resizing.


## Use cases
Hash tables are great when you want to 
* Create a mapping from one thing to another thing.
* Look something up.

- DNS resolution: mapping a web address to an IP address.

- Preventing duplicate entries.
  - If you store these names in a list, this function would eventually become really slow because it would have to run a simple search over the entire list.
  - A hash table instantly tells you whether this key is in the hash table or not.
  - Checking for duplicates is very fast with a hash table.
  
*Code example*
```python
voted = {}

def check_voter(name):
    if voted.get(name):
        print("This person already voted.")
    else:
        voted[name] = True
        print("Give a chance for vote!")
```


- Using hash tables as a cache.
  - Websites remember the data in a hash instead of recalculating it over and over again.

*Code example*
```python
cache = {}
def get_data_from_server(url):
    pass

def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data
```


## References
* Grokking Algorithms
