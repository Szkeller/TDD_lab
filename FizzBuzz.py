
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