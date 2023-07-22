
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
    except:
        return True

def solverEquation(equation):
    
    parts = [item.equation.split('=') for item in equation]
    expression = equation[1]
    validOperators = ['+', '-', '*', '/']

    for op in validOperators:
        value = expression.split(op)
        if len(value) > 1:
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
    elif checkIncognito(value[1]):
        if op == '-' or op == '/':
            A = float(values[0])
            B == float(leftValue)
        elif op == '+' or op == '*':
            A = float(leftValue)
            B = float(values[0])

    if op == '+':
        result = A - B 
        return result
    elif op == '-':
        result = A + B
        return result
    elif op == '*':
        result = A / B 
        return result
    else: 
        result = A * B
        return result

    resultText.set(result)
    print(result)

expression = ['12', '=', 'x', '+', '6']
solverEquation(expression)
