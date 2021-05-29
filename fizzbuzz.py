def fizzbuzz(int):
    if (int % 5 == 0 and int % 3 == 0):
        return "FizzBuzz"
    if (int % 5 == 0):
        return "Buzz"
    if (int % 3 == 0):
        return "Fizz"
    return int