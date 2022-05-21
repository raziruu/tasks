# #1. Write a python program to reverse a given list using while loop.
# # a=[1,2,3,4]
# a=[1,2,3,4]
# output=[ ]
# i=len(a)-1
# while i>=0:
#     output=a.reverse()
#     i=i-1
# print(a)



#2.Write a python program to reverse a string using while loop.
# a="python"

# a="python"
# output=" "
# i=len(a)-1
# while i>=0:
#     output=output+a[i]
#     i=i-1
# print(output)
# 3.Write a python program to print a multiplication table of any number using while loop.

# n=int(input("Enter a number for multiplication:"))
# i=1
# while i<=10:
#     print(n,"*",i,"=",n*i)
#     i=i+1

# 5.Write a program to print the following using while loop
# a. first 10 even numbers
# b.first 10 odd numbers
# c.first 10 natural numbers

# i=0
# while i<=8:
#     i=i+2
#     print(i)
# i=1
# while i<=20:
#     i=i+2
#     print(i)
# i=0
# while i<=9:
#     i=i+1
#     print(i)
#6.Write for loop statement to print the following series:
# 10 20 30 --------300
# a=10
# while a<300:
#
#     a=a+10
#     print(a,end=" ")

#7. Write a while loop statement to print the following series:
# 105 98 -------7
# a=112
# while a>=7:
#     a=a-7
#     print(a,end=" ")

#8. Write a program to print the factorial of a number accepted from user.

# n=int(input("Enter a number to calculate factorial:"))
# fact=1
# while n>0:
#     fact=fact*n
#     n=n-1
# print(fact)


# y=10
# def outer():
#     z=4
#     def inner():
#         x=4
#         print(x)
#         print("inside the function y",y)
#     inner()
#     print("z:",z)
# outer()


# y=10
# def outer():
#     z=4
#     def inner():
#         x=4
#         z=z+1
#         print(x)
#         print("inside the function y",y)
#     inner()
#     print("z:",z)
# outer()


# y=10
# def outer():
#     z=4
#     global y
#     y=6
#     def inner():
#         x=4
#         z=z+1
#         print(x)
#         print(z)
#         print("inside the function y",y)
#     inner()
#     print("z:",z)
# outer()

# def outer():
#     x="local"
#     def inner():
#         x="non local"
#         print("inner:",x)  
#         x="local"
#     inner()
#     print()

# from unittest import result


# result= lambda n1,n2,n3 : n2+n3+n1 
# print("sum of three values :", result(10,20,25))

# c=lambda a,b,c:((a/b/c),(a+b+c),(a-b-c),(a*b*c))
# d,e,f,g=c(10,20,30)
# print(d)
# print(e)
# print(f)
# # print(g)

# a=[1,2,3]
# b=[3,4,5]
# abc= list(map(lambda x,y:x+y,a,b))
# print(abc)

for i in range(-3):
    print ("a")