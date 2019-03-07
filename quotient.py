
PROMPT_DIVIDEND = "Please enter a dividend: "
PROMPT_DIVISOR = "Please enter a divisor: "

RESULT_MESSAGE = "The quotient is {0} with a remainder of {1}"

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

quotientFloor = dividend // divisor
quotientRemainder = dividend % divisor

print(RESULT_MESSAGE.format(format(quotientFloor, '.0f'), '{0:.5g}'.format(quotientRemainder)))

