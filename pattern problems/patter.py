# x=5
# for i in range(1,x+1,1):
#     for j  in range(x-i+1):
#         print(i,end=" ")
#     print()
# output:
# 1 1 1 1 1 
# 2 2 2 2
# 3 3 3
# 4 4
# 5

# x=5
# for i in range(x,0,-1):
#     for  j in range(x-i+1):
#         print(i,end=" ")
#     print()
# output:
# 5 
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1

# x=5
# for i in range(x,0,-1):
#     for j in range(i):
#         print(i,end=" ")
#     print()
# output:
# 5 5 5 5 5 
# 4 4 4 4
# 3 3 3
# 2 2
# 1

# x=5
# for i in range(1,x+1,1):
#     for j in range(i):
#         print(i,end=" ")
#     print()
# output:
# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5


# x=5
# for i in range(x,0,-1):
#     pat=""
#     for j in range(i):
#         pat=pat+str(i-j)+" "
#     print(pat)
# output:
# 5 4 3 2 1 
# 4 3 2 1
# 3 2 1
# 2 1
# 1
        
# x=int(input("Enter the number:"))5
# for i in range(1,x+1,1):
#     pat=""
#     for j  in range(i):
#         pat=pat+str(i-j)+" "
#     print(pat)
# output:
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

# x=int(input("Enter the number:"))10
# for i in range(x,0,-1):
#     pat=""
#     for j in range(i):
#         pat=pat+str(i-j)+" "
#     print(pat)
# for i in range(2,x+1,1):
#     pat=""
#     for j in range(i):
#         pat=pat+str(i-j)+" "
#     print(pat)
# output:
# 10 9 8 7 6 5 4 3 2 1
# 9 8 7 6 5 4 3 2 1
# 8 7 6 5 4 3 2 1
# 7 6 5 4 3 2 1
# 6 5 4 3 2 1
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
# 6 5 4 3 2 1
# 7 6 5 4 3 2 1
# 8 7 6 5 4 3 2 1
# 9 8 7 6 5 4 3 2 1
# 10 9 8 7 6 5 4 3 2 1

# x=int(input("Enter the number:"))5
# for i in range(x):
#     print(str(chr(65+i)+" ")*(x-i))
# output:
# A A A A A 
# B B B B
# C C C
# D D
# E

# x=int(input("Enter the number:")):5
# for i in range(x):
#     print((str(chr(65+(x-i-1))+" ")*(i+1)))
# output:
# E 
# D D
# C C C
# B B B B
# A A A A A

# x=int(input("enterthe  number:"))5
# for  i  in range(x):
#     print(((str(chr(65+(x-i-1)))+" ")*(x-i)))
# for j in range(x):
#     print(str(chr(65+j)+" ")*(j+1))
#  output:
# E E E E E
# D D D D
# C C C
# B B
# A
# A
# B B
# C C C
# D D D D
# E E E E E


# x=int(input("Enter the number:"))
# for  i in range(x):
#     if i==0:
#         print("* "*x)
#     elif i==(x-1):
#         print("* "*x)
#     else:
#         hollow="  "*(x-2)
#         print("* "+hollow+"* ")
# output:
# * * * * *
# *       *
# *       *
# *       *
# * * * * *


# x=int(input("Enter the number:"))5
# for  i in range(x):
#     if i==0:
#         print("* "*x)
#     elif i==(x-1):
#         print("* "*x)
#     else:
#         hollow="  "*(x-2)
#         print("* "+hollow+"* ")
# for i in range(x-1):
#     if i==0:
#         print("* "+"  "*(x-2)+"* ")
#     elif i==(x-2):
#         print("* "*x)
#     else:
#         print("* "+"  "*(x-2)+"* ")
# output:
# * * * * * 
# *       *
# *       *
# *       *
# * * * * *
# *       *
# *       *
# *       *
# * * * * *

   
# x=5
# for i in range(x):
#     if i==0:
#         print("  "*(x-1)+"* ")
#     elif i==(x-1):
#         print("  "*(x-i-1)+"* "*x)
#     else:
#         hollow="  "*(i-1)
#         left_spaces="  "*(x-(i+1))
#         print(left_spaces+"* "+hollow+"* ")
# output:
#         * 
#       * *
#     *   *
#   *     *
# * * * * *

# x=5
# count=0
# for i in range(x,0,-1):
#     for j in range(i):
#         count+=1
#         print(count,end=" ")
#     print()
# output:
# 1 2 3 4 5 
# 6 7 8 9
# 10 11 12
# 13 14
# 15

# x=5
# sum=0
# for i in range(x,0,-1):
#     sum=sum+i
# b=sum
# for j  in range(x+1):
#     for k in range(j):
#         b=b-1
#         print(b+1,end=" ")
#     print()
# output:
# 15
# 14 13
# 12 11 10
# 9 8 7 6
# 5 4 3 2 1
        

    