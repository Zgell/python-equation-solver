# -----------------------------------------------------------------------------
import math


def solve(eq):
    if (eq.count('(') > 0):  # IF there's more than one "level"...
    # Find the location of the first left bracket
    lbracket = eq.find('(')
    rbracket = eq[::-1].find(')')
    # Find the location of the last right bracket
    # Recursively solve the equation inside the brackets
    pass


equation = input("Enter an equation:")
answer = solve(equation)
print("Answer:", answer)