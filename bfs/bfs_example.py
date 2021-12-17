from collections import deque

GRAPH = {}


def __item_matches_target(item, target):
    """
    Placeholder for checking if item matches target.
    """
    return item == target


def bfs_search(starting_point, target):
    """
    This function uses the shared resource GRAPH.
    The algorithm will keep going until either we find a matching item, or the queue becomes empty.
    """
    search_queue = deque()
    search_queue += GRAPH[starting_point]
    searched = set()
    while search_queue:  # while the queue is not empty
        item = search_queue.popleft()
        if not item in searched:
            if __item_matches_target(item, target):
                print("Found the target '{}'.".format(target))
                return True
            else:
                search_queue += GRAPH[item]
                searched.add(item)
    return False


if __name__ == '__main__':
    # GRAPH init - a quick solution
    GRAPH["narae"] = ["asim", "tom", "yongdi"]
    GRAPH["asim"] = ["sachin", "shin"]
    GRAPH["yongdi"] = ["yash"]
    GRAPH["tom"] = ["sachin", "yash"]
    GRAPH["dermot"] = []
    GRAPH["shin"] = []
    GRAPH["yash"] = []
    GRAPH["sachin"] = []

    # Test
    success_test = bfs_search("narae", "shin")
    print(success_test)

    failure_test = bfs_search("narae", "jennifer")
    print(failure_test)
