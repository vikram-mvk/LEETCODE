#https://leetcode.com/problems/lru-cache/

#using an ordered dict
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache: del self.cache[key]
        self.cache[key] = value
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)

#Using dict and doubly linked list
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache:
    # create dict, head and tail dummy's and wire them
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def put(self, key, value):
        # existing node
        if key in self.dic:
            # get the node using dict and remove it from linked list
            self._remove(self.dic[key])

        n = Node(key, value)
        # insert at the tail
        self._add(n)
        # add node to dict
        self.dic[key] = n

        # The head's next element will be removed if it has reached the capacity
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]

    def _remove(self, node):
        # modify Forward link. Make previous node point to this node's next instead of this node
        node.prev.next = node.next
        # modify Backward link. Make this node's next's pre to point this node's previous, instead of this node
        node.next.prev = node.prev

    # insert at tail
    def _add(self, node):
        # connect this node inbetween tail and its previous node
        node.next = self.tail
        node.prev = self.tail.prev
        # Forward link: make tail's previous node's next point to this node
        self.tail.prev.next = node
        # backward link: make tail's pre point to this node
        self.tail.prev = node

    def get(self, key):
        if key not in self.dic:
            return -1
        n = self.dic[key]
        self._remove(n)
        self._add(n)
        return n.val