def fizzbuzz(x):
    words = ''
    if x % 3 == 0:
        words += 'Fizz'
    if x % 5 == 0:
        words += 'Buzz'
    return words or str(x)
