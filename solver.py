# -----------------------------------------------------------------------------
import math


def solve(eq):
    if (eq.count('(') > 0):  # IF there's more than one "level"...
    # Find the location of the first left bracket
    lbracket = eq.find('(')

    # Find the location of the last right bracket
    '''
    NOTE: eq[::-1] is just eq but in reverse order.
    This is because Python has no built-in method to get the last of a certain
    character.
    '''
    rbracket = eq[::-1].find(')')
    new_eq = eq[lbracket:rbracket]

    # Recursively solve the equation inside the brackets
    pass


equation = input("Enter an equation:")
answer = solve(equation)
print("Answer:", answer)