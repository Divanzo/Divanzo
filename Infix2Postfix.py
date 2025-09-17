from ArrayStack import ArrayStack

def precedence(op):
    if op=='(' or op==')':
        return 0
    elif op=='+' or op=='-':
        return 1
    elif op=='*' or op=='/':
        return 2
    else:
        return -1

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

def Infix2Postfix(expr):
    s=ArrayStack(100)
    output=[]

    for term in expr:
        if term =='(':
            s.push(term)
        
        elif term ==')':
            while not s.is_empty():
                op=s.pop()
                if op=='(':
                    break
                else:
                    output.append(op)
        
        elif term in '+-*/':
            while not s.is_empty():
                op=s.peek()
                if precedence(op)>=precedence(term):
                    output.append(s.pop())
                else:
                    break
            s.push(term)
        else:
            output.append(term)

    while not s.is_empty():
        output.append(s.pop())
    
    return output


if __name__=='__main__':
    print("Infix to Postfix")

    infix1 = ['3', '+', '5', '*', '2', '-', '8', '/', '4']
    infix2 = ['(', '5', '+', '3', ')', '*', '(', '2', '-', '8', ')', '/', '2']

    postfix1 = Infix2Postfix(infix1)
    postfix2 = Infix2Postfix(infix2)

    result1 = evalPostfix(postfix1)
    result2 = evalPostfix(postfix2)

    print("Infix: ", infix1)
    print("Postfix: ", postfix1)
    print("Result: ", result1)
    print()
    print("Infix: ", infix2)
    print("Postfix: ", postfix2)
    print("Result: ", result2)