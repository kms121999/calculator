
PROMPT_FIRST_NUMBER = "Please enter a number: "
PROMPT_SECOND_NUMBER = "Please enter another number: "

RESULT_MESSAGE_DIVISION = "The quotient is {0} with a remainder of {1}"
RESULT_MESSAGE_MULTIPLICATION = "The product of the numbers is {0:.5g}"

SET_OF_NUMBERS = 2 #Set of numbers to get from user and run operations on

def main():
    for i in range(SET_OF_NUMBERS):
        number1, number2 = get_two_numbers()

        print()
        print_quotient_and_remainder(number1, number2)
        print()
        print_product(number1, number2)
        print()
        print()


def get_float(prompt):
    user_input = None

    while user_input == None:
        try:
            user_input = float(input(prompt))
        except ValueError:
            pass

    return user_input

def get_two_numbers():
    number1 = get_float(PROMPT_FIRST_NUMBER)
    number2 = get_float(PROMPT_SECOND_NUMBER)
    return number1, number2

def print_quotient_and_remainder(dividend, divisor):
    quotientFloor = dividend // divisor
    quotientRemainder = dividend % divisor
    print(RESULT_MESSAGE_DIVISION.format(format(quotientFloor, '.0f'), '{0:.5g}'.format(quotientRemainder)))

def print_product(multiplicand, multiplier):
    product = multiplicand * multiplier
    print(RESULT_MESSAGE_MULTIPLICATION.format(product))
    

#Call main function
main()

