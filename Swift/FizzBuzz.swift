/*
* FizzBuzz Swift implementation
*/

func FizzBuzz(n: Int) -> Void {
    for i in 1...n {
        if i % 3 == 0 && i % 5 == 0 {
            print("FizzBuzz")
        } else if i % 5 == 0 {
            print("Buzz")
        } else if i % 3 == 0 {
            print("Fizz")
        } else {
            print(i)
        }

    }
}

FizzBuzz(n: 30)