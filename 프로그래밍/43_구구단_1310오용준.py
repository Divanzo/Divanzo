# 43-1
for i in range(2,10):
    print(f"== {i}단 ==")
    for j in range(1,10):
        print(f"{i}*{j}={i*j}")
    print()

# 43-2
n=int(input("몇 단? "))

print(f"== {n}단 ==")

for i in range(1,10):
    print(f"{n}*{i}={n*i}")
print()