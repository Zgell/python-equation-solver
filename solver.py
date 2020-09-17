# -----------------------------------------------------------------------------
import math


def compute(eq):

    return eq


def solve(eq):
    if (eq.count('(') > 1):  # IF there's more than one "level"...
        # Find the location of the first left bracket
        lbracket = eq.find('(')

        # Find the location of the last right bracket
        '''
        NOTE: eq[::-1] is just eq but in reverse order.
        This is because Python has no built-in method to get the last of a 
        certain character.
        "new_eq" will be the equation inside the outermost set of parentheses.
        '''
        rbracket = eq[::-1].find(')')
        new_eq = eq[lbracket + 1:len(eq) - rbracket - 1]

        # Recursively solve the equation inside the brackets
        return new_eq

    # If only one level remains...
    elif (eq.count('(') == 1) and (eq.count(')') == 1):
        lbracket = eq.find('(')
        rbracket = eq.find(')')
        new_eq = eq[lbracket + 1:rbracket]
        return new_eq

    # If you're at the innermost level with no brackets
    elif (eq.count('(') == 0) and (eq.count(')') == 0):
        return compute(eq)


equation = input("Enter an equation: ")
answer = solve(equation)
print("Answer:", answer)