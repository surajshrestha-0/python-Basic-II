"""
Write an if statement to determine whether a variable holding a year is a leap year.
"""


def leapYearCheck(input_year):
    if (input_year % 400 == 0) or ((input_year % 4 == 0) and (input_year % 100 != 0)):
        print("%d is a Leap Year" % input_year)
    else:
        print("%d is Not the Leap Year" % input_year)


if __name__ == "__main__":
    year = int(input("Please Enter a Year: "))
    leapYearCheck(year)
