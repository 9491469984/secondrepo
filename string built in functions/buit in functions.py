#upper()

# x="Ramakrishna"
# print(x.upper())
# output:
# RAMAKRISHNA

# x="aman"
# print(x.upper())
# output:
# AMAN

# x="Mega star"
# print(x.upper())
# output:
# MEGA STAR

# x="ram is a good boy"
# print(x.upper())
# output:
# RAM IS A GOOD BOY

# x="lord sriram"
# print(x.upper())
# output:
# LORD SRIRAM

#isupper():

# x="Vasanth"
# for i in x:
#     print(i.isupper())
# output:
# True
# False
# False
# False
# False
# False
# False

# x="MAHATMA GANDHI"
# print(x.isupper())
# output:
# True

# x="Lavanya"
# print(x.isupper())
# output:
# False

# X="HYDERBAD"
# print(X.isupper())
# # output:
# True

# x="Chiranjeevi"
# print(x.isupper())
# output:
# False

#split():
#syntax: str_var.split(separtor)

# x="I am good boy"
# y=x.split()
# print(y)
# output:
# ['I', 'am', 'good', 'boy']


# x="python is a programming language"
# y=x.split(",")
# print(y)
# output:
# output:
# ['python is a programming language']

# x="Manoj is my best friend"
# print(x.split(" "))
# output:
# ['Manoj', 'is', 'my', 'best', 'friend']

# x="Aman,is,,our ,TL"
# y=x.split(",")
# print(y)
# output:
# ['Aman', 'is', '', 'our ', 'TL']

# x="1   2  3 4 5 "
# print(x.split(" "))
# output:
# ['1', '', '', '2', '', '3', '4', '5', '']

# x="1-03-2023"
# print(x.split("-"))
# output:
# ['1', '03', '2023']


# x="Learning python is easy easy"
# print(x.split("a",3))
# output:
# ['Le', 'rning python is e', 'sy e', 'sy']


# x="Marolix"
# print(x.rsplit("a"))
#  output:
#  ['M', 'rolix']

# x="Farmer is the backbone of India"
# print(x.rsplit("e",3))
# output:
# ['Farm', 'r is th', ' backbon', ' of India']

# x="I had learnt python"
# y=x.rsplit("i")
# print(y)
# output:
# ['I had learnt python']

# x="silley fellows"
# print(x.rsplit("e",-1))
# output:
# ['sill', 'y f', 'llows']

# x="Lord Sri Rama is my favourite god"
# print(x.rsplit("o",4))
# output:
# ['L', 'rd Sri Rama is my fav', 'urite g', 'd']



# join():
# syntax:"separtor".join(variable name)

# x=["1","03","2023"]
# print("-".join(x))
# output:
# 1-03-2023

# x=['L', 'rd Sri Rama is my fav', 'urite g', 'd']
# print("o".join(x))
# output:
# Lord Sri Rama is my favourite god

# x="Lord h","numan"
# print("a".join(x))
# output:
# Lord hanuman


# x="A","an is our TL"
# print("M".join(x))
# output:
# AMan is our TL


# x="J","van R","ddy"
# print("ee".join(x))
# output:
# Jeevan Reeddy


# lower()
# sytax: x.lower()

# x="NARASHIMA SWAMY"
# print(x.lower())
# output:
# narashima swamy

# x="MY dad Is A Farmer"
# print(x.lower())
# output:
# my dad is a farmer

# x="POTHULA JEEVANREDDY"
# print(x.lower())
# output:
# pothula jeevanreddy

# x="#$%23@JEEVAN"
# print(x.lower())
# output:
# #$%23@jeevan

# x="POTHULA narayanareddy"
# print(x.lower())
# output:
# pothula narayanareddy


# islower():
# syntax: x.islower()

# x="@!$%^ABC*&123"
# print(x.isupper())# It will ignore the special charectors and numbers
# output:
# True

# x="@!$%^abcABC*&123"
# print(x.islower()) It doesn't ignore letters
# output:
# False


# x="RAMARAO"
# print(x.islower())
# output:
# False


# x="chinnari"
# print(x.islower())
# output:
# True


# x="aman"
# print(x.islower())
# output:
# True


# x="RamaSethu"
# print(x.islower())
# output:
# False



# count():
# syntax: x.count("substring")
# statement:How many times a particular substring present in the given string
# syntax: x.count("substring",starindex,endindex)
# statement:If we want to know the particular substring count in the given range

# x="Jeevan is a very very nice guy"
# print(x.count("very"))
# output:
# 2


# x="Iskan is the famous temple in Anantapur"
# print(x.count("A",14,len(x)))
# output:
# 1

# x="Mahanandhi"
# print(x.count("n"))
# output:
# 2

# x="abcdeh%$#%$$"
# print(x.count("$",4,-1))
# output:
# 2

# x="abababababcscwggfshgcscsvctcsfshvxcc"
# print(x.count("c"))
# output:
# 8


# Replace:
# syntax: x.replace("OLd","New")

# x="JEEvanreddy"
# print(x.replace("E","e"))
# output:
# Jeevanreddy

# x="sum rises in the east"
# print(x.replace("m","n"))
# output:
# sun rises in the east

# x="ABC company"
# print(x.replace("BC","bc"))
# output:
# Abc company

# x="Druga soft Durga soft"
# print(x.replace("soft","Sir"))
# output:
# Druga Sir Durga Sir


# x="Merolix"
# print(x.replace("e","a"))
# output:
# Marolix


# startswith():
# syntax:x.startswith("sumstring")


# x="@#$ramu"
# print(x.startswith("@"))
# output:
# True

# x="https://www.google.com/"
# print(x.startswith("https"))
# output:
# True

# x="Megastar"
# print(x.startswith("m"))
# output:
# False

# x="  venky"
# print(x.startswith(" "))
# output:
# True

# x="Lord Hanuman"
# print(x.startswith("Lord"))
# output:
# True


# endswith():
# syntax: x.enswith("substring")

# x="Jeevanreddy "
# print(x.endswith(" "))
# output:
# True

# x="https://www.google.com"
# print(x.endswith("com"))
# output:
# True

# x="Python if"
# print(x.endswith("is"))
# output:
# False


# x="Tom and Leery"
# print(x.endswith("L"))
# output:
# False

# x="@#$%^&*"
# print(x.endswith("*"))
# output:
# True


# swapcase():
# syntax: x.swapcase()

# x="JeevanReddy"
# print(x.swapcase())
# output:
# jEEVANrEDDY


# x="manjunath"
# print(x.swapcase())
# output:
# MANJUNATH

# x="$%%#@@$RAMU"
# print(x.swapcase())
# output:
# $%%#@@$ramu

# x="Marolix@123"
# print(x.swapcase())
# output:
# mAROLIX@123

# x="FarmeR"
# print(x.swapcase())
# output:
# fARMEr


# isdigit()
# syntax: x.isdigit()

# x="1234"
# print(x.isdigit())
# output:
# True

# x="!@#$1 3 45"
# print(x.isdigit())
# output:
# False

# x="1 2 3 4"
# print(x.isdigit())
# output:
# False

# x="Jeevan%234"
# print(x.isdigit())
# output:
# False

# x="power star"
# print(x.title())
# output:
# Power Star


# title()
# syntax: x.tittle()


# x="the best fruit"
# print(x.title())
# output:
# The Best Fruit

# x="Jeevan is a good boy"
# print(x.title())
# output:
# Jeevan Is A Good Boy

# x="ma ro lix"
# print(x.title())
# output:
# Ma Ro Lix

# x="Mango is my favourite fruit"
# print(x.title())
# output:
# Mango Is My Favourite Fruit

# x="Aman is my TL"
# print(x.title())
# output:
# Aman Is My Tl


# istitle():
# syntax: x.istitle()


# x="I Am In The Office"
# print(x.istitle())
# output:
# True


# x="i am a good boy"
# print(x.istitle())
# output:
# False

# x="TempleS are thE peaceful places"
# print(x.istitle())
# output:
# False

# x="Peaceful PLaces"
# print(x.istitle())
# output:
# False


# x="Computer is a electronic device"
# print(x.istitle())
# output:
# False




#  capitalize()
#  syntax: x.capitalize()


# x="i am jeevan"
# print(x.capitalize())
# output:
# I am jeevan


# x="ravan is a Demaon"
# print(x.capitalize())
# output:
# Ravan is a demaon

# x="JEEVAN IS A SOFTWARE ENGINEER"
# print(x.capitalize())
# output:
# Jeevan is a software engineer

# x="Pincky Tincky Donkey"
# print(x.capitalize())
# output:
# Pincky tincky donkey


# x="Humans has best Benfits as compared to Birds"
# print(x.capitalize())
# output:
# Humans has best benfits as compared to birds



# isalpha():
# syntax: x.isalpha()

# x="ABCabc"
# print(x.isalpha())
# output:
# True

# x="123ABc"
# print(x.isalpha())
# output:
# False

# x="ABC"
# print(x.isalpha())
# output:
# True

# x="a b c"
# print(x.isalpha())
# output:
# False

# x="123"
# print(x.isalpha())
# output:
# False




# isalnum():
# syntax: x.isalnum()


# x="ACDacd123"
# print(x.isalnum())
# output:
# True

# x="aB$%12"
# print(x.isalnum())
# output:
# False

# x="Jeevan Reddy 123"
# print(x.isalnum)
# output:
# False

# x="Pothula"
# print(x.isalnum())
# output:
# True

# x="123"
# print(x.isalnum())
# output:
# True

# isspace():
# syntax: x.isspace()

# x=" J E V A N"
# print(x.isspace())
# output:
# False

# x="t/"
# print(x.isspace())
# output:
# False

# x="  "
# print(x.isspace())
# output:
# True



# 1. input: ram is good boy
# expected output: boy good is ram 

# x="Ram is good boy".split()
# y=(x[::-1])
# print(" ".join(y))
# output:
# boy good is Ram


# 2.input: ABCDAABBCCDDEEFFGGHI
# OUTPUT:ABCDEFGHI


# x="ABCDAABBCCDDEEFFGGHI"
# append_list=[]
# for i in x:
#     if i not in append_list:
#         append_list.append(i)
# print(*append_list)
# output:
# A B C D E F G H I





