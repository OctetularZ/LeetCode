from collections import deque


class MyStack:
    def __init__(self):
        self.queue = deque([])

    def push(self, x: int) -> None:
        self.queue.appendleft(x)

    def pop(self) -> int:
        temp = []
        while len(self.queue) > 1:
            temp.append(self.queue.pop())

        res = self.queue.pop()

        for i in temp:
            self.queue.appendleft(i)

        return res

    def top(self) -> int:
        if self.queue:
            return self.queue[0]

    def empty(self) -> bool:
        if self.queue:
            return False
        else:
            return True

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()