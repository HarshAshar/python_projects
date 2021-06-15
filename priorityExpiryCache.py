
# You can use any language.

# Your task is to implement a PriorityExpiryCache cache with a max capacity.  Specifically please fill out the data structures on the PriorityExpiryCache object and implement the entry eviction method.

# You do NOT need to implement the get or set methods.

# It should support these operations:
#   Get: Get the value of the key if the key exists in the cache and is not expired.
#   Set: Update or insert the value of the key with a priority value and expiretime.
#     Set should never ever allow more items than maxItems to be in the cache.
#     When evicting we need to evict the lowest priority item(s) which are least recently used.

# Example:
# p5 => priority 5
# e10 => expires at 10 seconds since epoch

# c = NewCache(5)
# c.Set("A", value=1, priority=5,  expireTime=100)
# c.Set("B", value=2, priority=15, expireTime=3)
# c.Set("C", value=3, priority=5,  expireTime=10)
# c.Set("D", value=4, priority=1,  expireTime=15)
# c.Set("E", value=5, priority=5,  expireTime=150)
# c.Get("C")


# // Current time = 0
# c.SetMaxItems(5)
# c.Keys() = ["A", "B", "C", "D", "E"]
# // space for 5 keys, all 5 items are included

# time.Sleep(5)

# // Current time = 5
# c.SetMaxItems(4)
# c.Keys() = ["A", "C", "D", "E"]
# // "B" is removed because it is expired.  e3 < e5

# c.SetMaxItems(3)
# c.Keys() = ["A", "C", "E"]
# // "D" is removed because it the lowest priority
# // D's expire time is irrelevant.

# c.SetMaxItems(2)
# c.Keys() = ["C", "E"]
# // "A" is removed because it is least recently used."
# // A's expire time is irrelevant.

# c.SetMaxItems(1)
# c.Keys() = ["C"]
# // "E" is removed because C is more recently used (due to the Get("C") event).

# */

# type PriorityExpiryCache struct {
#   maxItems int
#   // TODO(interviewee): implement this
# }

# func NewCache(maxItems int) *PriorityExpiryCache {
#   return &PriorityExpiryCache{
#     maxItems: maxItems,
#   }
# }

# func (c *PriorityExpiryCache) Get(key string) interface{} {
#   // ... the interviewee does not need to implement this.

#   return nil
# }

# func (c *PriorityExpiryCache) Set(key string, value interface{}, priority int, expire time.Time) {
#   // ... the interviewee does not need to implement this.

#   c.evictItems()
# }

# func (c *PriorityExpiryCache) SetMaxItems(maxItems int) {
#   c.maxItems = maxItems

#   c.evictItems()
# }

# // evictItems will evict items from the cache to make room for new ones.
# func (c *PriorityExpiryCache) evictItems() {
#   // TODO(interviewee): implement this
# }

import datetime

# This will be one node of our doubly linked list, which we will use in step 3. below
# to determine the least recently used key
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class PriorityExpiryCache:

    def __init__(self, maxItems):
        # eg. self.cache[key] = [value, priority, expire_time]
        self.cache = {}
        self.maxItems = maxItems
        self.creationTime = datetime.datetime.now()

        # sorted list of keys in the descending order 
        # list of tuples (key, priority), sorted in ascending order of priority
        self.priorityOrder = []
        # list of tuples (key, expiry), sorted in ascending order of expiration time
        self.expiryOrder = []

        # For least recently used doubly linked list
        self.head = None
        self.tail = None

    def setMaxItems(self, maxItems):
        self.maxItems = maxItems
        self.evictItems()

    def evictItems(self):
        # Only evict if elements in the current cache exceed maxItems
        if len(self.cache) > self.maxItems:
            now = datetime.datetime.now()
            # Assuming maxItems will always be > 0
            # Evict n number of times, where n is the excess number of elements
            for _ in range(self.maxItems - len(self.cache)):
                # using expired, priority or least recently used logic, evict element

                # 1. Check if an expired key is available
                # Compare current time with key's expiration time
                if now > self.cache[self.expiryOrder[0]][2]:
                    self.removeKeyFromOrderLists(self.expiryOrder[0])
                    continue

                # 2. if no expired keys exists, check least priority item
                # Skip to step 3. if more than one least priority keys exist
                if len(self.priorityOrder) > 1 and self.cache[self.priorityOrder[0]][1] != self.cache[self.priorityOrder[1]][1]:
                    self.removeKeyFromOrderLists(self.priorityOrder[0])
                    continue

                # 3. if more than one items with same least priority exist, use LRU
                # Build a list of least priority keys
                leastPriorityKeys = []
                leastPriority = self.cache[self.priorityOrder[0]][1]
                leastPriorityKeys.append(self.priorityOrder[0])
                for x in range(1, len(self.priorityOrder)):
                    if self.cache[self.priorityOrder[x]][1] == leastPriority:
                        leastPriorityKeys.append(self.priorityOrder[x])
                    else:
                        break
                # Invoke the least recently used method, passing the keys with the same least priority
                lruKey = self.leastRecentlyUsed(leastPriorityKeys)
                self.removeKeyFromOrderLists(lruKey)

    def leastRecentlyUsed(self, leastPriorityKeys):
        # Parse doubly linked list from head to tail to find first key present in leastPriorityKeys
        currentNode = self.head
        while currentNode.key not in leastPriorityKeys:
            currentNode = currentNode.next
        # Node with required key found
        # If least recently used element is found at head, update new head
        if currentNode == self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        # if least recently used element is after head, update previous & next elements pointers
        else:
            currentNode.prev.next = currentNode.next
            # if least priority key node is not the last node
            if currentNode.next:
                currentNode.next.prev = currentNode.prev
        lru_key = currentNode.key
        # Deleting soon to be evicted key's node
        del currentNode
        # return least priority key which was least recently used
        return lru_key

    def removeKeyFromOrderLists(self, key):
        # update all ordered lists
        del self.cache[key]
        # retaining all list items except for the evicted key
        self.expiryOrder = list(filter(lambda x: x[0] != key, self.expiryOrder))
        self.priorityOrder = list(filter(lambda x: x[0] != key, self.priorityOrder))

    def get(self, key):
        pass

    def set(self, key, value, priority, expire_time):
        # some implementation details
        # add key => [value, priority, expire_time] to cache
        # add (key, priority) tuple to priorityOrder list, sort by x[1] i.e. priority
        # add (key, expire_time) tuple to expiryOrder list, sort by x[1] i.e. expire_time where expiry_time = self.creationTime + datetime.timedelta(0, expire_time)
        # append new key to doubly linked list

        # if key already present, updating node and list values
        pass


    
def newCache(maxItems):
    return PriorityExpiryCache(maxItems)

c = newCache(5)