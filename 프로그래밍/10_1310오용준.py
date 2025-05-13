# stu1=['hong',165.0,53.2,'A',2]

# stu2={"kor":1,"usa":2}

# stu3=(1,2,3,'ab',5)

# print(stu1[1:4], stu2['kor'], stu3[4])

# print('*'*20)

# aa=[10,20,30,40]
# print(aa[0:3])
# print(aa[2:4])
# print(aa[2:])
# print(aa[:2])

# print('*'*20)

# bb=[10,20,30]
# cc=[40,50,60]

# print(bb+cc)
# print(bb*2)

# print('*'*20)

# arr1=list(range(10))
# arr2=list(range(5,12))
# arr3=list(range(-3,5,2))
# arr4=list(range(10,0,-1))

# print(arr1)
# print(arr2)
# print(arr3)
# print(arr4)

# a=list(range(0,1001,100))
# print(a)

# student = {'name':'홍길동','birth':1128,'age':17}
# print(student{})

print('*'*25)

data=[30,10,20]
print(f"햔재의 리스트: {data}")
print(f"리스트데이터의 개수: {len(data)}")
print(f"40추가 후의 리스트: {data.append(40)}")

last=data[-1]

print(f"리스트의 마지막 데이터: {last}")
print(f"추출 후 리스트: {data.pop(-1)}")

data.sort()

print(f"sorting: {data}")

data.reverse()

print(f"리스트뒤집기: {data}")
print(f"20의 위치: {data.index(20)}")

data.insert(2,222)

print(f"20자리에 222삽입: {data}")

data.remove(data[data.index(222)])

print(f"222삭제후의 리스트: {data}")

print('*'*25)

data2=[77,88,77]

data.extend(data2)

print(f"data extend to data2: {data}")
print(f"77 값의 개수: {data.count(77)}")

del data[2]

print(f"데이터중 2자리의 숫자 삭제 후 리스트: {data}")

print('*'*25)