# Problema 4 – Stivă (20p)

class Stack:
    def __init__(self):
        self._data = []

    def push(self, x):
        self._data.append(x)

    def pop(self):
        #o sa presupun ca nu e goala, daca ar fi as implementa un raise
        return self._data.pop()
    def peek(self):
        #ca mai inainte, presupun ca nu e goala
        return self._data[-1]

    def __repr__(self):
        return f"Stack({self._data})"

if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(7)
    print(s)
    s.pop()
    print(s)
    s.push(9)
    print(s.peek())  # 9
    print(s)
