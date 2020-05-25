class FizzBuzz:
    '''
        This is for TDD sample 
        Author: Keller Zhang
        create date: 04/27
        description: FizzBuzz Quiz
              When given number just can be divided by 3, then return 'Fizz';
              When given number just can be divided by 5, then return 'Buzz';
              When given number just can be divided by 3 and 5, then return 'FizzBuzz';
              otherwise return given number itself.
    '''

    def fizz_buzz(self, number):
        result = ''
        if number % 15 == 0:
            result = 'FizzBuzz'
        elif number % 5 == 0:
            result = 'Buzz'
        elif number % 3 == 0:
            result = 'Fizz'
        else:
            result = str(number)
        return result
    
if __name__ == '__main__':
    fizzbuzz = FizzBuzz()
    for i in range (1,101):
        print(fizzbuzz.fizz_buzz(i))