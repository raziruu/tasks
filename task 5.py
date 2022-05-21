# # 1.  Write a Python function to multiply all the numbers in a list.
# def mul():
#     a = [8,2,3,-1,7]
#     c = 1
#     for i in a:
#         c = c * i
#     print(c)
# mul()


# # 2.  Write a Python function to sum all the numbers in a list.
# def sum():
#     a = [8, 2, 3, 0, 7]
#     c = 0
#     for i in a:
#         c = c + i
#     print(c)
# sum()


# # 3.  Write a python function to find min of three numbers.(no parameter and no return type)
# def mean():
#     a = 10
#     b = 20
#     c = 30
#     ok = (a + b + c)//3
#     print(ok)
# mean()


# # 4. Write a function called fizz_buzz that takes a number.
# # If the number is divisible by 3, it should return “Fizz”.
# # If it is divisible by 5, it should return “Buzz”.
# # If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# # Otherwise, it should return the same number.\
# def fizz_buzz():
#     a = int(input("Enter a number :"))
#     if a%3 == 0:
#         print("Fizz")
#     elif a%5 == 0:
#         print("Buzz")
#     elif a%5 == 0 and a%3 == 0:
#         print("FizzBuzz")
#     else:
#         print(a)
# fizz_buzz()


# # 5. Create a function that can accept two arguments name and age and print its value.
# def show(name,age):
#     print(f"Name : {name} Age :{age}")
# show("Sunil",20)


# # 6. Write a program function to find max of three numbers.(no parameter and no return type)
# def max():
#     a = int(input("Enter the first number :"))
#     b = int(input("Enter the second number :"))
#     c = int(input("Enter the third number :"))
#     if a > b and a > c:
#         print(f"{a} is the greatest number.")
#     elif b > c  and c > a:
#         print(f"{b} is the greatest number.")
#     else:
#         print(f"{c} is the greatest number.")
# max()


# # 7. Write a Python function to print the even numbers from a given list. 
# def even():
#     a = [1,2,3,4,5,6]
#     for i in a:
#         if i % 2 == 0:
#             print(i)
#         else:
#             continue
# even()
            

# # 8. Write a Python function to print the odd numbers from a given list. 
# def odd():
#     a = [1,2,3,4,5,6]
#     for i in a:
#         if i % 2 != 0:
#             print(i)
#         else:
#             continue
# odd()


# # 9. Write a Python function that takes a number as a parameter and check the number is prime or not.
# def prime(a):
#     if a > 1:
#         for i in range(2,a):
#             if a % i == 0:
#                 print("The number isn't prime.")
#                 break
#     else:
#         print("The number is prime.")
# prime(9)


# 10. Write a function to reverse a string.
# def rev():
#     a = "python"
# for i  in reversed(a):
#     print(i)
# rev()


# # 11. Write a program to create a function that takes two arguments, name and age, and print their value.
# def show(name,age):
#     print(f"Name : {name} Age :{age}")
# show("justin",20)

# # 13. Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction.
# #  Also, it must return both addition and subtraction in a single return call.
# def calculation(a,b):
#     add = a + b
#     print("add =", add)
#     sub = a - b
#     print("sub =", sub)
# calculation(3, 4)


# # 14. Write a program to create a function show_employee() using the following conditions.
# #     It should accept the employee’s name and salary and display both.
# #    If the salary is missing in the function call then assign default value 9000 to salary
# def show_employee(name,salary = 9000):
#     print(f"Hello {name}, Your salary is {salary}")
# show_employee("Jastin")


# # 15. Find the largest item from a given list. 
# def largest():
#     a = [4, 6, 8, 24, 12, 2]
#     c = a[0]
#     for i in a:
#         if i > c:
#             c = i
#     print(f"The largest number is {c}.")
# largest()

# # 16. Find the smalles item from a given list. 
# def smallest():
#     a = [4, 6, 8, 24, 12, 2]
#     c = a[0]
#     for i in a:
#         if i < c:
#             c = i
#     print(f"The smallest number is {c}.")
# smallest()
  

# # 17. Define a function that accepts roll number and returns whether the student is present or absent.
# def diary(roll_no):
#     if roll_no == 1 or roll_no == 2 or roll_no == 3 or roll_no ==4 or roll_no == 5:
#         print("Present")
#     else:
#         print("False")
# diary(2)

        
# # 18. Define a function that accepts a number and returns whether the number is even or odd.
# def check(num):
#     if num % 2 == 0:
#         print("The number is even.")
#     else:
#         print("The number is odd.")
# check(20)


# # 19. Define a function which counts vowels and consonant in a word.
# def count(name):
#     vow = 0
#     cons = 0
#     for i in name.lower():
#         if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#             vow = vow + 1
#         else:
#             cons = cons + 1
#     print(f"The number of vowels are {vow}.")
#     print(f"The number of constans are {cons}.")
# count("Narayan")

       
# # 20. Define a function that returns Factorial of a number.
# def fac(num):
#     print(1)
#    9 if num > 1:
#         for i in range(2,num):
#             if num % i == 0:
#                 print(i)
#     print(num)
# fac(27)


# # 21. Define a function that accepts lowercase words and returns uppercase words
# def change(word):
#     lower = word.lower()
#     if word == lower:
#         upper = word.upper()
#         print(upper)
#     else:
#         print("Enter the word in lower case.")
# change("lalita")


# # 22. Define a function that accepts radius and returns the area of a circle.
# def area(radius):
#     ok = 2 * 3.14 * (radius ** 2)
#     print(f"The area of circle is {ok}.")
# area(5)







