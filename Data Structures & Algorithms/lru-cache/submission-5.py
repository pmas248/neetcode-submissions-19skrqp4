class LRUCache:

    def __init__(self, capacity: int):
        self.cache = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        #checks if value exists in cache, if yes, move it to the head
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                tmp = self.cache.pop(i)
                self.cache.append(tmp)
                return tmp[1]
        return -1

    def put(self, key: int, value: int) -> None:
        #checks if value exists in cache, if yes, move it to the head and update value
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                tmp = self.cache.pop(i)
                tmp[1] = value
                self.cache.append(tmp)
                return 

        #if doesn't exist, check if cache is full or not, if yes, pop the oldest element
        if self.capacity == len(self.cache):
            self.cache.pop(0)
        self.cache.append([key, value])
