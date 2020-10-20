# ============================================================================
# Python Equation Solver
#
# By: Zgell
# ============================================================================


def get_level_map(raw_eq):
    level_map = []
    level = 0
    for char in raw_eq:
        if char is "(":
            level += 1
        elif char is ")":
            level -= 1

        level_map.append(level)

    return level_map

'''
def child_analysis(eq):
    # Set up variables
    children = [""]
    lbracket, rbracket = [0, 0]  # Used to count levels of the equation
    index_l, index_r = [0, 0]

    # Loop through equation, save anything inside parentheses to "children"
    for i in range(0, len(eq)):
        if eq[i] == "(":
            lbracket += 1
            index_l = i
        elif eq[i] == ")":
            rbracket += 1
            index_r = i

        # If we find a whole child unit
        if (lbracket == rbracket) and (lbracket*rbracket > 0):
'''


class Equation:
    def __init__(self, raw_equation):
        self.raw = raw_equation

        # ONLY WORKS FOR ONE CHILD EQUATION
        # EQS OF THE FORM A+(B*C)+D*(E+F) will NOT work!
        if '(' in self.raw:
            # Define indices of outermost parentheses
            ind_start = self.raw.find('(')
            ind_end = self.raw[::-1].find(')')
            # Do this calculation before calling "Equation"
            endcap = len(self.raw) - ind_end - 1
            self.child = Equation(self.raw[ind_start+1:endcap])
            self.hasChild = True
        else:
            self.hasChild = False

    def __str__(self):
        return "Equation: " + self.raw

    def get_raw(self):
        return self.raw


if __name__ == "__main__":
    # Get user input
    userinput = input('Enter an algebraic expression to be simplified here: ')
    eq = Equation(userinput)
    print(eq)
    print(get_level_map(eq.get_raw()))
    '''
    try:
        print(eq.child)
        print(eq.child.get_raw())
    except:
        pass
    print(eq.hasChild)
    '''
    pass