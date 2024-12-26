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


# Optimal solution

# def isIsomorphic(self, s: str, t: str) -> bool:
#     char_index_s = {}
#     char_index_t = {}
#
#     for i in range(len(s)):
#         if s[i] not in char_index_s:
#             char_index_s[s[i]] = i
#
#         if t[i] not in char_index_t:
#             char_index_t[t[i]] = i
#
#         if char_index_s[s[i]] != char_index_t[t[i]]:
#             return False
#
#     return True
