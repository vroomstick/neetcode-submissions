class MyHashSet:

    def __init__(self):
        self.item = []
        

    def add(self, key: int) -> None:
        if key not in self.item:
            self.item.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.item:
            self.item.remove(key)
        

    def contains(self, key: int) -> bool:
        return key in self.item
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)