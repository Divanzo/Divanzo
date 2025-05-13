with open("attendance.txt", "w") as f:
    for i in range(1, 6):
        name=input(f"{i}번: ")
        f.write(f'{i}번: {name}\n')
