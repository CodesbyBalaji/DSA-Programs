def evaluate_postfix(expression):
    stack = []
    operators = {'+', '-', '*', '/'}

    def apply_operator(op, operand2, operand1):
        if op == '+':
            return operand1 + operand2
        elif op == '-':
            return operand1 - operand2
        elif op == '*':
            return operand1 * operand2
        elif op == '/':
            return operand1 / operand2

    for character in expression.split():
        if character not in operators:
            stack.append(float(character))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = apply_operator(character, operand2, operand1)
            stack.append(result)

    return stack[0] if stack else None

if __name__ == "__main__":
    expression = input("Enter the postfix expression: ")
    result = evaluate_postfix(expression)
    print("Result:", result)  

