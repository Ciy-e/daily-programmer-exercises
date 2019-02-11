
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
    if n == 0 {
        return 1
    } else if n == 1 {
        return 0
    } else {
        return (n-1) * (subfactorial(n:n-1) + subfactorial(n:n-2))
    }
}

print(factorial(n:4)) // 24
print(factorial(n:0)) // 1

print(subfactorial(n:5)) // 44
print(subfactorial(n:6)) // 265