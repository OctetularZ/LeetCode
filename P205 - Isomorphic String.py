def isIsomorphic(s: str, t: str) -> bool:
    counter = 0
    iso = {}
    for letter in s:
        if t[counter] not in list(iso.values()) and letter not in list(iso.keys()):
            iso[letter] = t[counter]
            print(letter, t[counter])
        else:
            if iso.get(letter) != t[counter]:
                return False
        counter += 1
    return True
