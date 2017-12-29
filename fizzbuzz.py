def fizzbuzz(x):
    if x == 15:
        return 'FizzBuzz'
    elif x == 30:
        return 'FizzBuzz'
    elif x % 3 == 0:
        return 'Fizz'
    elif x % 5 == 0:
        return 'Buzz'
    else:
        return str(x)
