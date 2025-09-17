from ArrayStack import ArrayStack

def evalPostfix(expr):
    s = ArrayStack(100)
    for token in expr:
        if token in '+-*/':
            right = s.pop()
            left = s.pop()
            if token == '+':
                s.push(left + right)
            elif token == '-':
                s.push(left - right)
            elif token == '*':
                s.push(left * right)
            elif token == '/':
                s.push(left / right)
        else:
            s.push(float(token))
    return s.pop()



if __name__ == "__main__":
    expr1 = [ '8', '2', '/', '3', '-', '3', '2', '*', '+']  
    # expr1 = input('연산자와 피연산자를 공백을 구분하여 입력하시오.').split()

    expr2 = [ '1', '2', '/', '4', '*', '1', '4', '/', '*']
    # expr2 = input('연산자와 피연산자를 공백을 구분하여 입력하시오.').split()

    print(expr1, ' --> ', evalPostfix(expr1))
    print(expr2, ' --> ', evalPostfix(expr2))