
// Return true of common substring is present in both strings.
func twoStrings(s1: String, s2: String) -> Bool{
    
    for char in s1 {
        if (s2.contains(char)){ 
            return true
        } 
    }

    return false

}