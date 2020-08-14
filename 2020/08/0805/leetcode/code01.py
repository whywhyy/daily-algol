# Design HashSet

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [False]*1000000
        

    def add(self, key: int) -> None:
        self.arr[key] = True

    def remove(self, key: int) -> None:
        self.arr[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.arr[key]

# set 자료형도 쓰더라~       
# class MyHashSet:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.ss = set()
        

#     def add(self, key: int) -> None:
#         self.ss.add(key)

#     def remove(self, key: int) -> None:
#         self.ss.discard(key)

#     def contains(self, key: int) -> bool:
#         """
#         Returns true if this set contains the specified element
#         """
#         return key in self.ss

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)