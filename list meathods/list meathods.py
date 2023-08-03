#take a list of values and check weather given number is present the list or not , if present 
#expected output should be 10 is available and first occurence is at : index


# user_input=int(input("Enter the number:"))
# x=[10,20,30,40,10,50,60,70]
# for i in range(len(x)):
    
#     if user_input in x:
#         find_index=x.index(user_input)
# print("The number "+str(user_input)+" is available and first occurence is at :",find_index)



#take a list of elements from 1 to 50 when ever user enter the value from 1- 50 particular elements needs to removed 



# new_list=[]
# user_input=int(input("Enter the number:"))
# for i in range(1,51):
#     new_list.append(i)
# if user_input > len((new_list)):
#     print("Index out of range")
# elif user_input in new_list:
#     new_list.remove(user_input)
#     print(new_list)
#     user_input_1=int(input("Enter the number:"))
#     if user_input_1 not in new_list:
#         print("The  number is already removed")
#     elif user_input_1 in new_list:
#         new_list.remove(user_input_1)
#         print(new_list)



# append():
# list.append(element)


# x=["RAMU","RAVI","RAJU","RAMESH"]
# new_list=[]
# for i in x:
#     if len(i)==4:
#         new_list.append(i)
# print(new_list)
# output:
# ['RAMU', 'RAVI', 'RAJU']


# x=list(range(11))
# new_list=[]
# for i in x:
#     new_list.append(i)
# print(new_list)
# output:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# x=["Ramu","SEETHA","!@#","1234"]
# new_list=[]
# for i in x:
#     if i.isalnum():
#         new_list.append(i)
# print(new_list)
# output:
# ['Ramu', 'SEETHA', '1234']

# new_list=[]
# for i in range(11):
#     fact=0
#     for j in range(1,i+1):
#         if i%j==0:
#             fact+=1
#     if fact==2:
#         new_list.append(i)
# print(sum(new_list))
# output:
# 17



# x="MADAM"
# z=[]
# for i in x:
#     z.append(i[::-1])
# print("".join(z))

# output:
# MADAM


# extend:
# syntax:
# list.extend(iterable)


# x=["MADAM","SIR","RAM","SEETHA"]
# y=["JEEVAN"]
# x.extend(y)
# print(x)
# output():
# ['MADAM', 'SIR', 'RAM', 'SEETHA', 'JEEVAN']


# x=["!@#"]
# y=["RAM","123","SEETHA"]
# x.extend(y)
# z=",".join(x)
# print(z)
# output:
# !@#,RAM,123,SEETHA

# x="MADAM"
# y="123456"
# z=x[::-1]
# a=y[::-1]
# b=list(a)
# c=list(z)
# b.extend(c)
# print(b)

# output:
# ['6', '5', '4', '3', '2', '1', 'M', 'A', 'D', 'A', 'M']

# x=10
# for i in range(x):
#     if i%2==0:
#         y=list(str(x))
#         z=list(str(i))
#         y.extend(z)
#         print(y)
#         output:
#         ['1', '0', '0']
#         ['1', '0', '2']
#         ['1', '0', '4']
#         ['1', '0', '6']
#         ['1', '0', '8']


# x=10
# for i in range(x):
#     if i%2!=0:
#         y=list(str(x))
#         z=list(str(i))
#         y.extend(z)
#         print(y)
#         output:
#         ['1', '0', '1']
#         ['1', '0', '3']
#         ['1', '0', '5']
#         ['1', '0', '7']
#         ['1', '0', '9']

   

# remove:
# syntax:
# list.remove(elmnt)


# x=[1,2,3,4,5]
# x.remove(x[4])
# print(x)
# output:
# [1, 2, 3, 4]


# x=[1,2,3,4,5,6]
# user_input=int(input("Enter the number:"))
# for i in x:
#     if i==user_input:
#         x.remove(user_input)
#         print(x)
#         output:
#         [1, 2, 4, 5, 6]


# x=[1,2,3,4,5,6]
# for i in x:
#     x.remove(i)
#     print(x)
#     output:
#     [2, 3, 4, 5, 6]
#     [2, 4, 5, 6]
#     [2, 4, 6]

# x=[1,2,3,4,5,6]
# for i in x:
#     x.remove(i)
#     print(sum(x))
#     output:
#     20
#     17
#     12


# count:
# syntax:
# list.count(value)


# x=["A","b","a","B","c"]
# for i in x:
#     print(x.count(i))
# output:
# 1
# 1
# 1
# 1
# 1


# x=["123","56","1234","122","123"]
# for i in x:
#     if i=="123":
#         y=x.count(i)
#         print(y)
#         output:
#         2
#         2


# x=["RAMU","124","RAmu","seetha"]
# for i in x:
#     if i.isalnum():
#        z = x.count(i)
#        print(z)
#        output:
#         1
#         1
#         1
#         1

# x=[1,2,3,4,5,1,2,2,3,3,3]
# y=x.count(3)
# print(y)
# output:
# 4

# x=["RAMU"]
# y=["1","@@","22","##","333"]
# x=y
# print(x.count("@@"))
# output:
# 1


# index:
# syntax:
# x.index(element)


# list_num = [4, 55, 64, 32, 16, 32]
# x = list_num.index(32)
# print(x)
# output:
# 3


# list_num=["RAMU","raju","123","!@#"]
# for i in list_num:
#     if i.isupper():
#         y=list_num.index(i)
#         print(y)
#         output:
#         0


# x=[2,4,6,8]
# for i in range(1,10):
#     if i%2==0:
#         print(x.index(i))
#         output:
#         0
#         1
#         2
#         3

# x=[1,2,3,4,5,6,7,8,9]
# for i in range(1,10):
#     if i%2!=0:
#         print(x.index(i))
#         output:
#         0
#         2
#         4
#         6
#         8


# fruits = ['apple', 'banana', 'cherry']
# x = fruits.index("cherry")
# print(x)
# output:
# 2


# pop
# syntax:
# list.pop(pos)

# x=["AMAN","JEEVAN","RAMU","SEETHA"]
# x.pop(-1)
# print(x)
# output:
# ['AMAN', 'JEEVAN', 'RAMU']

# x=["1234",'123','12','1']
# x.pop()
# print(x)
# output:
# ['1234', '123', '12']

# x=[1,2,3,4,5]
# x.pop(0)
# print(x)
# output:
# [2, 3, 4, 5]

# x=["344","Aman",456,60]
# x.pop()
# x.pop()
# print(x)
# output:
# ['344', 'Aman']

# x=["Mango","30","30","03"]
# x.pop(1,2)
# print(x)
# output:
# TypeError: pop expected at most 1 argument, got 2



# insert:
# syntax:
# list.insert(pos, elmnt)


# fruits = ['apple', 'banana', 'cherry']
# fruits.insert(1, "orange")
# print(fruits)
# output:
# ['apple', 'orange', 'banana', 'cherry']


# x=["123","12","Aman"]
# x.insert(1,"Jeevan")
# print(x)
# output:
# ['123', 'Jeevan', '12', 'Aman']


# x=["123","12",1,4]
# x.insert(3,12)
# print(x)
# output:
# ['123', '12', 1, 12, 4]


# x=["king","ramu","chinna"]
# y=x.insert(1,"ramu")
# print(y)
# output:
# None


# x=["Mango","Ramesh","Vasanth"]
# x.insert(2,"Karthik")
# print(x)
# output:
# ['Mango', 'Ramesh', 'Karthik', 'Vasanth']


# sort:
# syntax:
# x.sort()


# x=[1,5,7,3,4,5]
# x.sort()
# print(x)
# output:
# [1, 3, 4, 5, 5, 7]


# x=[1,5,7,3,4,5]
# x.sort(reverse=True)
# print(x)
# output:
# [7, 5, 5, 4, 3, 1]


# x=[1,5,7,3,4,5]
# x.sort(reverse=False)
# print(x)
# output:
# [1, 3, 4, 5, 5, 7]


# x=["RAMU","SEETHA","Ramu","seetha"]
# x.sort()
# print(x)
# output:
# ['RAMU', 'Ramu', 'SEETHA', 'seetha']

# x=["RAMU","SEETHA","Ramu","seetha"]
# x.sort(reverse=True)
# print(x)
# output:
# ['seetha', 'SEETHA', 'Ramu', 'RAMU']

#pro to take a tuple of numbers from keyboard and print Sum,average
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

# sort and sorted

# x=[1,6,2,7,3]
# print(sorted(x))
# print(x)

# output:
# [1, 2, 3, 6, 7]
# [1, 6, 2, 7, 3]


# x=(1,9,2,8,7)
# y=sorted(x)
# print(y)
# print(x)

# output:
# [1, 2, 7, 8, 9]
# (1, 9, 2, 8, 7)


# x="1","2","9","7","8"
# y=sorted(x)
# print(x)
# print(y)
# print(type(y))
# print(type(x))

# output:
# ('1', '2', '9', '7', '8')
# ['1', '2', '7', '8', '9']
# <class 'list'>
# <class 'tuple'>


# x={1,2,2,4,3,9,7}
# y=sorted(x)
# print(y)
# output:
# [1, 2, 3, 4, 7, 9]


# x=(1,3,5,2,4)
# x.sort()
# print(x)
# output:
# AttributeError: 'tuple' object has no attribute 'sort'


# x=[1,4,3,6,2]
# y=x.sort()
# print(y)
# print(x)
# output:
# None
# [1, 2, 3, 4, 6]

