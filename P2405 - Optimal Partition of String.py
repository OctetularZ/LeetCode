def partitionString(self, s: str) -> int:
    substr = ""
    partitions_lst = []
    for letter in s:
        if letter not in substr:
            substr += letter
        else:
            partitions_lst.append(substr)
            substr = ""
            substr += letter
    partitions_lst.append(substr)
    return len(partitions_lst)
