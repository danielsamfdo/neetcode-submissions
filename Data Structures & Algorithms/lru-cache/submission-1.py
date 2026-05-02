class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
        self.currCapacity = 0


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Key is in Cache.
        value = self.cache[key]
        self.cache.move_to_end(key)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
            return None
        if self.currCapacity == self.capacity:
            self.cache.popitem(last=False)
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            self.cache[key] = value
            self.cache.move_to_end(key)
            self.currCapacity += 1



