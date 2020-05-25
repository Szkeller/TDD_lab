import pytest

from FizzBuzz import FizzBuzz


class TestFizzBuzz():
    @pytest.mark.parametrize(
        "a, excepted",
        [
            (1, '1'),
            (2, '2'),
            (3, 'Fizz'),
            (4, '4'),
            (5, 'Buzz'),
            (15, 'FizzBuzz'),
        ],
    )
    def test_batch_test(self, a, excepted):
        fizzbuzz = FizzBuzz()
        assert fizzbuzz.fizz_buzz(a) == excepted


    def test_fizz_case(self):
        fizzbuzz = FizzBuzz()
        result = fizzbuzz.fizz_buzz(3)
        expected_result = 'Fizz'
        assert result == expected_result


    def test_buzz_case(self):
        fizzbuzz = FizzBuzz()
        result = fizzbuzz.fizz_buzz(5)
        expected_result = 'Buzz'
        assert result == expected_result  

    def test_fizzbuzz_case(self):
        fizzbuzz = FizzBuzz()
        result = fizzbuzz.fizz_buzz(15)
        expected_result = 'FizzBuzz'
        assert result == expected_result
        
if __name__ == '__main__':
    pytest.main()
    