 
# Functions to test
def happy_new_year():
    for num in range(10, 0, -1):
        print(num)
    print("Happy New Year!")

def square_integers(nums):
    return [num ** 2 for num in nums]

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)