# from my_package import mymath
# print(mymath.add(5, 3))  # Output: 8


# from my_package.mymath import add
# print(add(5, 4))  # Output: 9

import my_package.mymath
print(my_package.mymath.multiply(6, 7))  # Output: 42