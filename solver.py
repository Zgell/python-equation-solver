# -----------------------------------------------------------------------------
import math


def split_keep(string, delim):
    tokens = string.split(delim)
    for d in range(len(tokens) - 1):
    	tokens.insert(2*d+1, delim)
    return tokens

'''
def tokenize(string):
	symbols = "/*+-"
	tokens = split_keep(string, '^')
	for op in symbols:
		for i in range(0, len(tokens)):
			if op in tokens[i]:
				t = split_keep(tokens[i], op)
				tokens.remove(tokens[i])
				tokens[i:i] = t
'''
'''
	for i in range(0, len(tokens)):
		if '/' in tokens[i]:
			t = split_keep(tokens[i], '/')
			tokens.remove(tokens[i])
			tokens[i:i] = t
'''
'''
	for j in range(0, len(tokens)):
		if (len(tokens[i]) == 0):
			tokens.pop(i)
	return tokens
'''

def split_x(string, delim):
    stringlist = list(string)
    tokens = []  # The result which will be built up over time
    j = 0  # An iterator/placeholder variable
    for i in range(0, len(stringlist)):
        if stringlist[i] in delim:
            tokens.append(''.join(stringlist[j:i]))
            tokens.append(stringlist[i])
            j = i + 1
        elif (i == len(stringlist)-1):  # If you're at the end of the line
            tokens.append(''.join(stringlist[j:i+1]))

    # Remove unnecessary space characters
    for k in range(0, tokens.count('')):
    	tokens.remove('')

    # Return the result
    return tokens


def compute(eq):
    # Perform an EDMAS (BEDMAS without the brackets) operation
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

if __name__ == "__main__":
    equation = input("Enter an equation: ")
    answer = solve(equation)
    print("Answer:", answer)
