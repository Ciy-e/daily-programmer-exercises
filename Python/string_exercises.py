# Complete the alternatingCharacters function below.
# Returns the number of deletions required to change string of only A and B into strings of alternating A's and B's
def alternatingCharacters(s):
    last_char = ""
    removals = 0
    for char in s:
        if char == last_char:
            removals += 1
        last_char = char
    return removals