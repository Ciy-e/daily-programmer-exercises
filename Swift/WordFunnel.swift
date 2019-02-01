/*
* WordFunnel
* Determines if removing any one character from the second string will result the two strings being equal
*/ 
func funnel(s1: String, s2: String) -> Bool {
    if s2.count >= s1.count || (s1.count - s2.count) != 1 {
        return false
    }

    for i in 0..<s1.count {
        if s1[s1.index(s1.startIndex, offsetBy:i)] == s2[s2.index(s2.startIndex, offsetBy:i)] {
            continue
        } else if s2.suffix(from:s2.index(s2.startIndex, offsetBy:i)) == s1.suffix(from:s1.index(s1.startIndex, offsetBy:i+1)) {
            return true
        } else {
            return false
        }
    }
    return false
}

print(funnel(s1:"leave", s2:"eave")) // true
print(funnel(s1:"reset", s2:"rest")) // true
print(funnel(s1:"dragoon", s2:"dragon")) // true
print(funnel(s1:"eave", s2:"leave")) // false
print(funnel(s1:"sleet", s2:"lets")) // false
print(funnel(s1:"skiff", s2:"ski")) // false

