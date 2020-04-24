'''
   the functinon is for TDD propuse
   the logic is that:
   when given number can be divided by 3 with no remainder, then return 'Fizz'
   when given number can be divided by 5 with no remainder, then return 'Buzz'
   when given number can be divided by 3 and 5 with no remainder, then return 'FizzBuzz'
   otherwise return the given number itself
'''
def fizz_buzz(number):

    if number % 15 ==0:
       result = "FizzBuzz"
    elif number % 5 == 0:
        result = "Buzz"
    elif number % 3 == 0:
        result = "Fizz"
    else:
        result = str(number)
    return result