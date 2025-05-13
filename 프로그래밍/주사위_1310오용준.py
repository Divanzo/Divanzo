#original
for i in range(1,7):
    for j in range(1,7):
        print(f"({i},{j})",end=" ")
    print()


#ver1
for i in range(1,7):
    for j in range(1,7):
        if i==j:
            print("     ",end=" ")

        else:
            print(f"({i},{j})",end=" ")
    print()


#ver2
for i in range(1,7):
    for j in range(1,7):
        if i!=j:
            print("     ",end=" ")
            continue
        else:
            print(f"({i},{j})",end=" ")
    print()