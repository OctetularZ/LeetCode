class StockSpanner:

    def __init__(self):
        self.stock = []

    def next(self, price: int) -> int:
        span = 1
        new_stock = [price, span]
        n = len(self.stock)

        while self.stock and self.stock[-1][0] <= new_stock[0]:
            top = self.stock.pop()
            new_stock[1] += top[1]

        self.stock.append(new_stock)

        return new_stock[1]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# Monotonic Stack much faster than brute force
# Push [price, span] to stack
# Span starts at 1
# Pop from stack while the top price is less than or equal to price
# This way everything below the top price collapses into a single span
# To you only need to calculate span once rather than performing repeat calculations
