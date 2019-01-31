


// check if the number of x characters and y characters are equal
func balanced(s: String) -> Bool {
    var xyHashTable = [Character : Int]()
    xyHashTable = ["x": 0, "y": 0]
    
    if s == "" {
        return true
    }
    for char in s {
        if char != "x" && char != "y" {
            print("Error: Please only call balanced() with strings of only x and y.")
            return false
        }
        xyHashTable[char] = (xyHashTable[char] ?? 0) + 1
    }

    if xyHashTable["x"] == xyHashTable["y"] {
        return true
    } else {
        return false
    }

}

// check if all the characters in this string are repeated the same number of times.
func balanced_bonus(s: String) -> Bool {
    if s == "" {
        return true
    }
    var charDictionary = [Character: Int]()
    for char in s {
        charDictionary[char] = (charDictionary[char] ?? 0 ) + 1
    }

    let firstCount = charDictionary[Array(charDictionary.keys)[0]]
    for (_ , count) in charDictionary {
        if firstCount != count {
        return false
        }
    }
    return true
}

print(balanced(s: "xxxyyy")) // true
print(balanced(s: "yyyxxx")) // true
print(balanced(s: "xxxyyyy")) // false
print(balanced(s: "yyxyxxyxxyyyyxxxyxyx")) // true
print(balanced(s: "xyxxxxyyyxyxxyxxyy")) // false
print(balanced(s: "")) // true
print(balanced(s: "x")) // false

print(balanced_bonus(s: "xxxyyyzzz")) // true
print(balanced_bonus(s: "abccbaabccba")) // true
print(balanced_bonus(s: "xxxyyyzzzz")) // false
print(balanced_bonus(s: "abcdefghijklmnopqrstuvwxyz")) // true
print(balanced_bonus(s: "pqq")) // false
print(balanced_bonus(s: "fdedfdeffeddefeeeefddf")) // false
print(balanced_bonus(s: "www")) // true
print(balanced_bonus(s: "x")) // true
print(balanced_bonus(s: "")) // true