
/*
* Returns the minimum number of removals required to make all the elements of the array the same.
*/
func equalizeArray(arr: [Int]) -> Int {
    var hashTable = [Int : Int]()
    for i in arr {
        hashTable[i] = (hashTable[i] ?? 0) + 1
    }
    var maxValue = 0
    for (_ , count) in hashTable {
        if count > maxValue {
            maxValue = count
        }
    }
    return  arr.count - maxValue

}