def lengthOfLastWord(s: str) -> int:
    string_no_spaces = s.strip()
    string_list = string_no_spaces.split(" ")
    last_word_length = len(string_list[-1])
    return last_word_length
