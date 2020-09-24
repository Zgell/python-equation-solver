# -----------------------------------------------------------------------------
import math


def split_keep(string, delim):
    tokens = string.split(delim)
    for d in range(len(tokens) - 1):
    	tokens.insert(2*d+1, delim)
    return tokens


def frac_to_float(fraction):
	try:
		return float(fraction)
	except ValueError:
		num, denom = fraction.split('/')
		num = float(num)
		denom = float(denom)
		try:
			frac = num / denom
		except ZeroDivisionError:
			frac = 0
			pass
	return frac


def split_x(string, delim="+-*/^()"):
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


def calculate(num1, operator, num2):
	if (operator == "^"):
		return (float(num1) ** float(num2))
	elif (operator == "*"):
		return (frac_to_float(num1) * frac_to_float(num2))
	elif (operator == "/"):
		return (float(num1) / float(num2))
	elif (operator == "+"):
		return (float(num1) + float(num2))
	elif (operator == "-"):
		return (float(num1) - float(num2))
	else:
		return 0


def compute(eq):
    # Perform an EDMAS (BEDMAS without the brackets) operation
    operations = "^*/+-"
    eqa = eq

    for divide in range(0, eqa.count('/')):
    	divide_index = eqa.index('/')
    	eqa[divide_index] = '*'
    	oldnum = eqa[divide_index+1]
    	eqa[divide_index+1] = '1/' + oldnum

    for minus in range(0, eqa.count('-')):
        minus_index = eqa.index('-')
        eqa[minus_index] = '+'
        oldnum = eqa[minus_index+1]
        eqa[minus_index+1] = '-' + oldnum


    for op in operations:
    	opcount = eqa.count(op)
    	for i in range(0, opcount):
    		opindex = eqa.index(op)
    		calclist = eqa[opindex-1:opindex+2]
    		eqa[opindex-1:opindex+2] = [calculate(calclist[0], calclist[1], calclist[2])]
    return eq


def solve(eq):
    if (eq.count('(') > 1):  # IF there's more than one "level"...
        # Find the location of the first left bracket
        if (type(eq) is list):
            lbracket = eq.index('(')
        else:
            lbracket = eq.find('(')

        # Find the location of the last right bracket
        '''
        NOTE: eq[::-1] is just eq but in reverse order.
        This is because Python has no built-in method to get the last of a 
        certain character.
        "new_eq" will be the equation inside the outermost set of parentheses.
        '''
        if (type(eq) is list):
        	rbracket = eq[::-1].index(')')
        else:
        	rbracket = eq[::-1].find(')')
        new_eq = eq[lbracket + 1:len(eq) - rbracket - 1]

        # Recursively solve the equation inside the brackets
        next_eq = solve(new_eq)
        return new_eq

    # If only one level remains...
    elif (eq.count('(') == 1) and (eq.count(')') == 1):
        if (type(eq) is list):
            lbracket = eq.index('(')
            rbracket = eq.index(')')
        else:
            lbracket = eq.find('(')
            rbracket = eq.find(')')

        new_eq = eq[lbracket + 1:rbracket]
        next_eq = solve(new_eq)
        return new_eq

    # If you're at the innermost level with no brackets
    elif (eq.count('(') == 0) and (eq.count(')') == 0):
        return compute(eq)


if __name__ == "__main__":
    equation = input("Enter an equation: ")
    answer = solve(equation)
    print("Answer:", answer)
