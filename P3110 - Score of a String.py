def scoreOfString(s: str) -> int:
    n = len(s)
    total = 0

    for i in range(0, n - 1):
        total += abs((ord(s[i]) - ord(s[i + 1])))

    return total
