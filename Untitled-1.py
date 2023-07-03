# name=""
# password=""
# while name!="JEEVAN" or password!="123":
#     name=input("Enter the name:")
#     password=input("Enter the password:")
    
# print("you are a autherised person" )

#pattern problems:

# x=int(input("Enter the value:"))10
# for i in range(x):
#     if i==0:
#         print("* "*x)
#     elif i==(x-1):
#         print("* "*x)
#     else:
#         hallow_spaces="  "*(x-2)
#         print("* "+hallow_spaces+"* ")
#     output:
# * * * * * * * * * *
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# * * * * * * * * * *


# x=int(input("Enter the value:"))10
# for i in range(x):
#     for j in range(x):
#         print(chr(65+j),end=" ")
#     print()
# # output:
# A B C D E F G H I J
# A B C D E F G H I J
# A B C D E F G H I J
# A B C D E F G H I J
# A B C D E F G H I J
# A B C D E F G H I J
# A B C D E F G H I J
# A B C D E F G H I J
# A B C D E F G H I J
# A B C D E F G H I J  

# x=int(input("Enter the value:"))5
# for i in range(x):
#     print((chr(65+i)+" ")*x,end=" ")
#     print()
# output:
# A A A A A
# B B B B B
# C C C C C
# D D D D D
# E E E E E


# x=int(input("Enter the value:"))5
# for i in range(x):
#     print((chr(65+i)+" ")*(i+1),end=" ")
#     print()
# output:
# A
# B B
# C C C
# D D D D
# E E E E E

# x=int(input("enter the number:"))5
# for i in range(x):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# output:

# 1
# 1 2
# 1 2 3
# 1 2 3 4 

# x=int(input("Enter the value:"))
# for i in range(1,x+1):
#     print((str(i)+" ")*i,end=" ")
#     print()
# output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5


# x=int(input("Enter the value:"))
# for i in range(x):
#     print((str(x-i)+" ")*(x-i),end=" ")
#     print()
# output:
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

# x=int(input("Enter the number:"))6
# for i in range(x):
#     if i==0:
#         left_spaces="  "*(x-1)
#         print(left_spaces+"* ")
#     elif i==(x-1):
#         print("* "*x)
#     else:
#         left_spaces="  "*(x-i-1)
#         hallow="  "*(i-1)
#         print(left_spaces+"* "+hallow+"* ")
# output:
#           *
#         * *
#       *   *
#     *     *
#   *       *
# * * * * * *

# x=int(input("Enter the number:"))5
# for i in range(x):
#     if i==0:
#         print("* "*x)
#     elif i==(x-1):
#         print("  "*(x-1)+"* ")
#     else:
#         left_spaces="  "*(i)
                          
#         hallow="  "*(x-i-2)
#         print(left_spaces+"* "+hallow+"* ")
# output:
# * * * * *
#   *     *
#     *   *
#       * *
#         *