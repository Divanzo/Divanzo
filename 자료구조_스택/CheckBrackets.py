from ArrayStack import ArrayStack

def check_brackets(statement):
    stack = ArrayStack(100)
    for ch in statement:
        if ch == '(' or ch=='[' or ch=='{':
            stack.push(ch)
        elif ch == ')' or ch==']' or ch=='}':
            if stack.is_empty():
                return False
            else:
                left=stack.pop()
                if (ch==')' and left!='(') or \
                    (ch==']' and left!='[') or \
                    (ch=='}' and left!='{'):
                        return False
                
    return stack.is_empty()
# Test code

print(check_brackets(""))