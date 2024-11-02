class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Too many cookies!")
        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Too few cookies!")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Not a non-negative integer!")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError()
        self._size = size


def main():
    jar = Jar()
    jar.diposit(1)
    print(jar)
    jar.withdraw(2)
    print(jar)

if __name__ == "__main__":
    main()