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


# Returns true if s can be re-arranged into a palindrome.
def canBeRearrangedIntoPalindrome(s):
    character_dictionary = {}
    unique_character_found = False

    for char in s:
        if char in character_dictionary.keys():
            character_dictionary[char] += 1
        else:
            character_dictionary[char] = 1
    
    for char in character_dictionary.keys():
        if character_dictionary[char] % 2 == 1 and unique_character_found:
            return False
        elif character_dictionary[char] % 2 == 1 and not unique_character_found:
            unique_character_found = True

    return True