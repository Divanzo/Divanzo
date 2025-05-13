# bucket=[]

# while True:
#     if len(bucket)==5:
#         print(bucket,end=" ");print('end')
#         break
    
#     else:
#         n=input()
        
#         if n in bucket:
#             print('이미 있습니다.')
#             bucket.remove(n)

#         else:
#             bucket.append(n)
#             print(bucket)
bucket=[]

while len(bucket)<5:
    a=input()

    if a in bucket:
        print('이미 있다.')
    else:
        bucket.append(a)
        print(bucket)
        