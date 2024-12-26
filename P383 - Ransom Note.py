from collections import Counter


def canConstruct(ransomNote: str, magazine: str) -> bool:
    return Counter(ransomNote) <= Counter(magazine)