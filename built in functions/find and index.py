# x="Ram is a good boy".split()
# for i in x:
#     if i=="good":
#         print(x.index(i))
#     else:
#         print("good is not found in sequence")
# output:
# good is not found in sequence
# good is not found in sequence
# good is not found in sequence
# 3
# good is not found in sequence


# x="Mango is a fruit"
# if "Mango" in x:
#     b=x.index("Mango")
#     print("The first occurance of the sub string is:",b)
# else:
#     print("Mango is not found in the Given string")
# output:
# The first occurance of the sub string is: 0


# x=["1","3","e","7","33"]
# if "e" not in x:
#     print("e is not present in the given string")
# else:
#     print(x.index("e"))
# output:
# 2


# x=["Aman", "is", "my", "TL"]
# length=len(x)
# s=0
# while s<length:
#     if x[-length]  in x:
#         print(x.index("TL"))
#     else:
#         print("Values present in the given list")
#     s=s+1
# output:
# 3
# 3
# 3
# 3

# x=["1","2","3","^","*","@","7","8","9","10"]
# for i in x:
#     if i.isdigit():
#         print(x.index(i))
#     else:
#         print("print i values are charectors")
# output:
# 0
# 1
# 2
# print i values are charectors
# print i values are charectors
# print i values are charectors
# 6
# 7
# 8
# 9


# x=["1","2","3","5","66","77","88","99","100"]
# for i in x:

#     string_num=x.index(i)
#     if string_num%2==0:
#         print("Even values",string_num)
#     else:
#         print("Odd values are:",string_num)
# output:
# Even values 0
# Odd values are: 1
# Even values 2
# Odd values are: 3
# Even values 4
# Odd values are: 5
# Even values 6
# Odd values are: 7
# Even values 8

# x="a,b,c,d,@,#,%,1,2,3,4,5"
# for i in x:
#     if i.islower():
#         print(x.find("!"))
#     else:
#         print("Remaing charectors")

# output:
# -1
# Remaing charectors
# -1
# Remaing charectors
# -1
# Remaing charectors
# -1
# Remaing charectors
# Remaing charectors
# Remaing charectors
# Remaing charectors
# Remaing charectors
# Remaing charectors
# Remaing charectors
# Remaing charectors
# Remaing charectors
# Remaing charectors
# Remaing charectors
# Remaing charectors
# Remaing charectors
# Remaing charectors
# Remaing charectors
# Remaing charectors


# x="a b C 4 5"
# y=x.split()
# sum=0
# for i in y:
#     if i.isalpha():
#         b=x.find(i)
#         sum+=b
#         print(sum)
# output:
# 0
# 2
# 6


# x="a b c d e f 9"
# y=x.split()
# for k in y:
#     if k.isdigit():
#         b=x.find(k)       
# b=k
# for i in range(1,int(b)+1):
#     factor=0
#     for j in range(1,i+1):
#         if i%j==0:
#             factor+=1
#     if factor == 2:
#         print("prime numbers are:",i)
# output:
# prime numbers are: 2
# prime numbers are: 3
# prime numbers are: 5
# prime numbers are: 7


# x="a b c 5 e f 9"
# y=x.split()
# for k in y:
#     if k.isdigit():
#         b=x.find(k)      
# b=k
# for i in range(1,int(b)+1):
#     factor=0
#     for j in range(1,i+1):
#         if i%j==0:
#             factor+=1
#     if factor > 2:
#         print(" non-prime numbers are:",i)

# output:
# non-prime numbers are: 4
#  non-prime numbers are: 6
#  non-prime numbers are: 8
#  non-prime numbers are: 9


# x=["Anantapur","Tirupathi","Kurnool","kalyanadurgam"]
# string=(input("Enter the number:")) Kurnool
# if string.strip() in x:
#     print("Network is available at",string)
# else:
#     print("Network is not available at",string)
# output:
# Network is available at  Kurnool



# x="#######Aman******"
# print(x.strip("#,*"))

# output:
# Aman


# x="#$%&*Jeevanreddy!?"
# print(x.lstrip("#,$,%"))

# output:
# &*Jeevanreddy!?


# x="   123 &    "
# print(x.rstrip(" "))

# output:
#   123 &



# x="Ramakrishnareddya"
# print(x.rindex("a"))

# output:
# 16


# x="Jeevan reddy"
# print(x.rindex(" "))
#  output:
# 6


# x="Vasanth"
# print(x.rindex("p"))

# output:
# ValueError: substring not found


# x="Ramarao"
# print(x.rfind("a"))

# output:
# 5


# x="chongala Chinnari "
# print(x.rfind(" "))

# output:
# 17


# x="Megastar"
# print(x.rfind("K"))

# output:
# -1


# x="My name is Jeevan"
# y=x.find("jeevan")

# if y==-1:
#     pass
# print("Tankyou")

# x=["A","B","C"]
# y=["A","B","c"]
# print(x==y)

# print(id(x))
# print(id(y))

# output:
# False
# 2942513480832
# 2942513499136

# x=10
# y=11
# print(x==y)
# print(id(x))
# print(id(y))
# output:
# False
# 2521217788496
# 2521217788528


# x="Python is easy language"
# print(x.rfind(" ",6,len(x)))

# output:
# 14