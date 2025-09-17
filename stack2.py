from ArrayStack import ArrayStack

s=ArrayStack(100)

msg = input("Enter a string: ")
for ch in msg:
    s.push(ch)

print("문자열 출력: ", end="")
while not s.is_empty():
    print(s.pop(), end="")
print()