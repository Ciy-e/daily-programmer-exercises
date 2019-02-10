
/**
* Recursive factorial implementation
*/
func factorial(n: Int) -> Int {
    if n <= 1 {
        return 1
    } else {
        return n*factorial(n:n-1)
    }
}

func subfactorial(n: Int) -> Int {
    //@TODO finish writing this exercise.
    return 0
}

print(factorial(n:4)) // 24
print(factorial(n:0)) // 1