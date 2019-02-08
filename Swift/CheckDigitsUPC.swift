

/*
* Convert int to UPC number.
*/
func upc(num: Int) -> String {

    var upcString = String(num)

    if(upcString.count > 11) {
        return "Enter a number 11 digits or less in length.";
    }

    let zero = "0"
    let difference = 11 - upcString.count

    // prepend zeroes to make an 11 digit number.
    for _ in 0..<difference {
        upcString = zero + upcString
    }
    var sumOddPositions = 0
    var sumEvenPositions = 0
    for i in 0..<upcString.count {
        if i % 2 == 0 {
            sumOddPositions += Int(String(upcString[upcString.index(upcString.startIndex, offsetBy:i)])) ?? 0
            
        } else {
            sumEvenPositions += Int(String(upcString[upcString.index(upcString.startIndex, offsetBy:i)])) ?? 0
        }
    }
    let totalResult = (sumOddPositions*3) + sumEvenPositions
    var M = totalResult % 10
    if(M == 0) {
        M = 0
    } else {
        M = 10 - M
    }
    
    let finalUpcString = upcString + String(M)
    // returns the final UPC number including the check digit.
    return finalUpcString

}

print(upc(num: 4210000526))
print(upc(num: 3600029145))
print(upc(num: 12345678910))
print(upc(num: 1234567))