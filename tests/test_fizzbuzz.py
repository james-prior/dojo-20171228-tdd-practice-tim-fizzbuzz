import pytest

from fizzbuzz import fizzbuzz

number_to_expected_string = {
    1: '1',
    2: '2',
    3: 'Fizz',
    4: '4',
    5: 'Buzz',
    6: 'Fizz',
    10: 'Buzz',
    15: 'FizzBuzz',
    30: 'FizzBuzz',
}
@pytest.mark.parametrize('number, expected_string', number_to_expected_string.items())
def test_known_number_returns_expected(number, expected_string):
    assert expected_string == fizzbuzz(number) 
