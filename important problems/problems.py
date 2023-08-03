# 10:Write a program to display all prime numbers within a range.


# for i in range(1,20):
#     fact=0
#     for j in range(1,i+1):
#         if i%j==0:
#             fact+=1
#     if fact==2:
#         print(i)
# output:
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19


# 11: Display Fibonacci series up to 10 terms.

# x=0
# y=1
# for i in range(2,10+1):
#     sum=x+y
#     x=y
#     y=sum
#     print(sum,end=" ")
# output:
# 1 2 3 5 8 13 21 34 55


# 12: Find the factorial of a given number.

# x=int(input("Enter the number:"))5
# count=1
# for i in range(1,x+1):
#     count=count*i
# print(count)

# output:
# 120


# 13: Reverse a given integer number.
# res=0
# x=1234567
# while x!=0:
#     quotient=x//10
#     remainder=x%10
#     res=(res*10)+remainder
#     x=quotient
# print(res)
# output:321


# 14: Use a loop to display elements from a given list present at odd index positions.

# x=[1,4,5,7,9,2]
# y=len(x)
# z=[i for i in range(y) if i%2!=0]
# for j in z:
#     print(x[j])
# output:
# 4
# 7
# 2


# 15: Calculate the cube of all numbers from 1 to a given number.


# x=3
# y=[i**3 for i in range(1,x+1)]
# print(y)

# output:
# [1, 8, 27]


# 6: Find the sum of the series upto n terms.

# sum=0
# for i in range(1,11):
#     sum+=i
#     print(sum,end=" ")
# output:
# 1 3 6 10 15 21 28 36 45 55


# 17: Append new string in the middle of a given string.

# x="Jeevanreddy"
# y="pothula"
# z=len(x)//2
# a=x[:z]+y+x[5:]
# print(a)
# output:
# Jeevapothulanreddy

# pro to take a tuple of numbers from keyboard and print Sum,average
# x=int(input("Enter the number:"))4
# z=[]
# for i in range(x):
#     y=input("Enter the vales:")
#     if y.isdigit():
#         z.append(y)
# a=tuple(z)
# sum=0
# for i in a:
#     sum+=int(i)
#     avg=sum//len(a)
# print(sum)
# print(avg)
# output:
# Enter the number:4
# Enter the vales:a
# Enter the vales:1
# Enter the vales:b
# Enter the vales:2
# 3
# 1


# set:
# x=set()
# print(type(x))
# output:
# <class 'set'>

# x={}
# print(type(x))
# output:
# <class 'dict'>

# x={1,2,3,4}
# print(type(x))
# output:
# <class 'set'>

# x={1,2,3,4}
# print(x.add(1,2))
# output:
# TypeError: set.add() takes exactly one argument (2 given)


# x={1,2,3,4}
# print(x.add(5))
# output:
# None

# x={1,2,3,4}
# x.add(5)
# print(x)
# output:
# {1, 2, 3, 4, 5}

# x={1,2,3,4}
# x.add("Jeevan")
# print(x)
# output:
# {1, 2, 3, 4, 'Jeevan'}

# x={"Aman","Jeevan","Ramu","sai"}
# x.add("seetha")
# print(x)
# output:
# {'Jeevan', 'seetha', 'Ramu', 'Aman', 'sai'}

# x=set([1,2,3])
# print(x)
# output:
# {1, 2, 3}


# x={"Ram sai","Jeevan"}
# y=x.add("Hanuma")
# print(y)
# output:
# None


# x={[1,2,3],"Jeevan"}
# x.add("ramu")
# print(y)
# output:
# TypeError: unhashable type: 'list'


# x={1,22,3,6,7,2,3}
# print(x)
# output:
# {1, 2, 3, 6, 7, 22}


# update:
# syntax:
# x.update(element)

# x={1,2,3,4}
# x.update("aman")
# print(x)
# output:
# {1, 2, 3, 4, 'm', 'a', 'n'}


# x={[1,2,3,4]}
# y={1,2,3,4}
# print(x.update(y))
# output:
# TypeError: unhashable type: 'list'

# x={(1,2,3,4)}
# y={456}
# x.update(y)
# print(x)
# output:
# {456, (1, 2, 3, 4)}

# x=[1,2,3,4]
# y=("aman","Jeevan")
# z=set([123,321])
# z.update(x,y)
# print(z)
# output:
# {321, 2, 3, 1, 4, 'aman', 'Jeevan', 123}

# x=set(1,2,3,4)
# x.update("aman")
# print(x)
# output:
# TypeError: set expected at most 1 argument, got 4


# x={1,2,3,4}
# y=x.copy()
# del(x)
# print(y)
# output:
# {1, 2, 3, 4}

# x={1,2,3,4}
# y=x
# print(id(x))
# print(id(y))
# output:
# 2512019232576
# 2512019232576

# x={1,2,3,4}
# y=x.copy()
# print(id(x))
# print(id(y))
# output:
# 2334245623616
# 2334245622496