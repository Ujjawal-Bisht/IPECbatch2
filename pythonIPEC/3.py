'''
* * * *
  * * *
    * *
      *
'''

n=4
# for i in range(n):
#     for j in range(i):
#         print(' ',end=' ')
#     for k in range(n-i):
#         print('*',end=' ')
#     print()


'''
      *
    * *
  * * *
* * * *
'''

# for i in range(n):
#     for j in range(n-i-1):
#         print(' ',end=' ')
#     for k in range(i+1):
#         print('*',end=' ')
#     print()


'''
*           *
* *       * *
* * *   * * *
* * * * * * *
'''

# for i in range(n):
#     for j in range(i+1):
#         print('*',end=' ')
#     for m in range(2*(n-i-1)):
#         print(' ',end=' ')
#     for l in range(i+1):
#         print('*',end=' ')
#     print()


'''
for i in range(1,n+1):
    for j in range(1,2*n):
        if j>=i+1 and j<=(2*n)-row-1:
            print(' ',end=' ')          #More logical
        else:
            print("*",end=' ')
    print()
'''



'''
* * * * * * *
* * *   * * *
* *       * *
*           *
'''

# for i in range(n):
#     for j in range(n-i):
#         print('*',end=' ')
#     for k in range(2*i):
#         print(' ',end=' ')
#     for i in range(n-i):
#         print('*',end=' ')
#     print()


# for row in range(1,n+1):
#     for col in range(1,2*n):
#         if (col >= n-row+2 and col <= n+row-2):
#             print(' ',end=' ')
#         else:
#             print('*',end=' ')
#     print()

'''
* * * * * * *
* * *   * * *
* *       * *
*           *
* *       * *
* * *   * * *
* * * * * * *
'''

# for i in range(n):
#     for j in range(n-i):
#         print('*',end=' ')
#     for k in range(2*i):
#         print(' ',end=' ')
#     for i in range(n-i):
#         print('*',end=' ')
#     print()

# for i in range(n-1):
#     for j in range(i+2):
#         print('*',end=' ')
#     for m in range(2*(n-i-2)):
#         print(' ',end=' ')
#     for l in range(i+2):
#         print('*',end=' ')
#     print()

'''
* * * *
    *
  *
* * * *
'''

for i in range(n):
    if (i == 0 or i == n-1):
        print('* ' * n,end=' ')
    else:
        print(' ' * (n-i)+ ('*'),end=' ')
    print()