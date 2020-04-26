# hash table
class MyHashMap(object):
    def __init__(self, size=1024):
        self.size = size
        self.hash = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        for item in self.hash[key]:
            if item[0] == key:
                item[1] = value
                return
        self.hash[key].append([key, value])

    def get(self, key: int) -> int:
        for item in self.hash[key]:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        delete = []
        for item in self.hash[key]:
            if item[0] == key:
                delete = item
        if delete:
            self.hash[key].remove(delete)
