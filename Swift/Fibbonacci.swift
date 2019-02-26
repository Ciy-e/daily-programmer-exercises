
// Recursive fibbonacci implementation.
func fibbonacci(n: Int) -> Int {
    if n < 2 {
        return n
    } else {
        return fibbonacci(n:n-1) + fibbonacci(n:n-2)
    }
}

print(fibbonacci(n:0))
print(fibbonacci(n:15))