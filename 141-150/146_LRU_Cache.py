class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.list = {}

    def get(self, key: int) -> int:

        value = -1
        if(key in self.list): 
            value = self.list[key]
            self.list.pop(key)
            self.list[key] = value
        return value

    def put(self, key: int, value: int) -> None:

        if(key in self.list):
            self.list.pop(key)

        elif(len(self.list) == self.capacity):
            for i in self.list:
                self.list.pop(i)
                break
        self.list[key] = value
        
    

capacity = ["LRUCache","put","put","get","put","get","put","get","get","get"]
obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)