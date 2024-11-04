def getMinIterations(arr):
    # Write your code here

    if sorted(arr) == arr:
        return 0


print(getMinIterations([6, 5, 4, 3, 1, 2]))
print(getMinIterations([1, 2, 3, 4]))


# 두 수를 골라내서 더해서 임의의 장소에 삽입했을 때 최소가 되는 수
#

class MyClass:
    def __init__(self):
        self.__private = "private"
        self._protected = "protected"
        self.public = "public"

    @property
    def protected(self):
        return self._protected


a = MyClass()
# print(a.__private)
print(a.protected)
print(a.public)
