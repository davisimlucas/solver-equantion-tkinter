
oppositeOperators = {
    '+': '-',
    '-': '+',
    '*': '/',
    '/': '*'
}

def checkIncognito(valor):
    try:
        float(valor)
        return False
    except ValueError:
        return True

def solverEquation(equation):
    parts = equation.split('=') 
    expression = parts[1]
    validOperators = ['+', '-', '*', '/']

    for op in validOperators:
        values = expression.split(op)
        if len(values) > 1:
            operators = op
            break
        
    values = [v.strip() for v in values]
    leftValue = parts[0].strip()

    if checkIncognito(leftValue):
        A = float(values[0])
        B = float(values[1])
    elif checkIncognito(values[0]):
        A = float(leftValue)
        B = float(values[1])
        op = oppositeOperators[op]
    elif checkIncognito(values[1]):
        if op == '-' or op == '/':
            A = float(values[0])
            B = float(leftValue)
        elif op == '+' or op == '*':
            op = oppositeOperators[op]
            A = float(leftValue)
            B = float(values[0])

    if op == '+':
        result = A + B 
    elif op == '-':
        result = A - B
    elif op == '*':
        result = A * B 
    else: 
        result = A / B

    return result
