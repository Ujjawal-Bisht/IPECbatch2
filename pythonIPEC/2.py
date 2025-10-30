# n = int(input("Enter num:- "))
# for i in range(1,11):
#     # print(f'{n}*{i}={n*i}')
#     print(n,"*",i,'=',n*i)
n=4
for  i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(n-i-1):
        print("*",end=' ')
    for k in range(n-i-2):
        print("*",end=' ')
    print()