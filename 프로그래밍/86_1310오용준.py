# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# numbers[5]=80
# print(numbers)  

# numbers[2:6]='hello'
# print(numbers)

# numbers[2]=['a', 'b', 'c']    
# print(numbers)

# del numbers[4]
# print(numbers)

N=int(input())

alist=list(map(int, input().split()))

for i in range(len(alist)):
    alist[i]=ali