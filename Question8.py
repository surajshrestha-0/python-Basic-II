"""
Write a function, is_prime, that takes an integer and returns True if the number is prime
and False if the number is not prime.
"""


def test_prime(input_number):
    if input_number == 1:
        return False
    elif input_number == 2:
        return True
    else:
        for i in range(2, input_number):
            if input_number % i == 0:
                return False
        return True


if __name__ == "__main__":
    number = int(input("Please Enter an Integer: "))
    print(test_prime(number))
