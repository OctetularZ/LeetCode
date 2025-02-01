def kthFactor(self, n: int, k: int) -> int:
    ls = []
    for i in range(1, n + 1):
        if n % i == 0:
            ls.append(i)
    print(ls)
    try:
        return ls[k - 1]
    except IndexError:
        return -1
