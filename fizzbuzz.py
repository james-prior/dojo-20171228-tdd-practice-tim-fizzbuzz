def fizzbuzz(x):
    words = ''
    if x % 3 == 0:
        words = 'Fizz'
    if x % 5 == 0:
        words += 'Buzz'
    if not words:
        words = str(x)
    return words
