# for i in range(10):
#     print(i)
#     break
#output:0

# for i in range(1,10+1):
#     if i==5:
#         break
#     else:
#         print("6 * ",i,"=",6*i)
# output:
# 6 *  1 = 6
# 6 *  2 = 12
# 6 *  3 = 18
# 6 *  4 = 24

# a=["apple","banana","Mango","Grapes"]
# new_list=[]
# for i in a:
#     new_list.append(i)
#     if "Mango" in new_list:

#         break
#     print(i)
#output:
# apple
# banana

# x=input("Enter the string:")Jeevan is nice guy
# length=len(x)
# i=0
# while i<length:
#     if x[i]=="i" or x[i]=="c":
#         print(x[i])
#         break
#     print("It exit from the if condition block")
#     i+=1
# output:
# It exit from the if condition block
# It exit from the if condition block
# It exit from the if condition block
# It exit from the if condition block
# It exit from the if condition block
# It exit from the if condition block
# It exit from the if condition block
# i

# x=[1,2,3,4,5,6,7,8,9]
# for element in x:
#     if int(element)%2==0:
#         print(element)
#         break
#     print("It is not Even Number")
# output:
# It is not Even Number
# 2

# for i in range(5):
#     for j in range(5):
#         if j==2 or j==4:
#             continue
#         print("the number is",i,j)
# output:
# the number is 0 0
# the number is 0 1
# the number is 0 3
# the number is 1 0
# the number is 1 1
# the number is 1 3
# the number is 2 0
# the number is 2 1
# the number is 2 3
# the number is 3 0
# the number is 3 1
# the number is 3 3
# the number is 4 0
# the number is 4 1
# the number is 4 3


# count=0
# while count<=10:
#     count+=1
#     if count==7:
#         print("hi")  
# print("out from the loop")
# output:
# hi
# out from the loop


# x=["Hyderabad","Chenai","Anantapur","Goa","Vishakapatnam"]
# for i in x:
#     if "Banglore" not in x:
#         continue
#     print(i)
# output:
# no output

# x="jeevan@1234jeevan"
# for i in x:
#     if i.isdigit():
#         print(i)
#         continue 
# print("It is a charector")
# output:
# 1
# 2
# 3
# 4
# It is a charector


# count=1
# while count<10:
#     if count%2==0:
#         count+=1
#         continue
#     else:
#         print(count)
#         count+=1
# output:
# 1
# 3
# 5
# 7
# 9

# write a program to divided 100 with a list of elements.
# sample Input : 10,20,30,0,50,00,30
# expected output: 10.0
# 5.0
# sample_input=[10,20,30,0,50,00,30]
# for  i in sample_input:
#     if i==0:
#         print("Sorry it  is not divisible by 0")
#         continue
#     b=100/int(i)
#     print("100 is divisible by i values:",b)

#
# output:
# 
# 100 is divisible by i values: 10.0
# 100 is divisible by i values: 5.0
# 100 is divisible by i values: 3.3333333333333335
# Sorry it  is not divisible by 0
# 100 is divisible by i values: 2.0
# Sorry it  is not divisible by 0
# 100 is divisible by i values: 3.3333333333333335




