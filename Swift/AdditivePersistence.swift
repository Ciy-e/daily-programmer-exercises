/*
* Finds the additive peristence of an integer
* 
*/

func sumOfDigits(_ n: inout Int) -> Int {
    var sum = 0
    while n > 0 {
        sum += n % 10
        n /= 10
    }
    return sum
}

func additivePeristence(_ n: inout Int) -> Int {
    var iterations = 0
    if n <= 9 {
        return iterations
    } else {
        iterations = 0
        while n > 9 {
            n = sumOfDigits(&n)
            iterations += 1
        }
        return iterations
    }
}


// expecting an additive persistence of 2
var test =  9876

print(additivePeristence(&test))