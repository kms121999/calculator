
PROMPT_DIVIDEND = "Please enter a dividend: "
PROMPT_DIVISOR = "Please enter a divisor: "

RESULT_MESSAGE_QUOTIENT = "The quotient is {0:.0f} with a remainder of {1:.5g}"
RESULT_MESSAGE_SUM = "The sum of the numbers is {0:.5g}"

def get_float(prompt):
    user_input = None

    while user_input == None:
        try:
            user_input = float(input(prompt))
        except ValueError:
            pass

    return user_input
    
dividend = get_float(PROMPT_DIVIDEND)
divisor = get_float(PROMPT_DIVISOR)

numberSum = dividend + divisor

quotientFloor = dividend // divisor
quotientRemainder = dividend % divisor

print(RESULT_MESSAGE_QUOTIENT.format(quotientFloor, quotientRemainder))
print()
print(RESULT_MESSAGE_SUM.format(numberSum))
