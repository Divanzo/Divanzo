word=input("문장 입력: ")
alist=[]
o=0
print('#'*25)
print(word)
print("대문자입력:", word.upper())
print("소문자입력:", word.lower())

print("문자 길이:", len(word))
for i in word:
    alist.append(i)

if o in word:
    o+=1
    print("o의 개수:",o)
print(alist)