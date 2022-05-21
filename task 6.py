# # 2. Create an inner function to calculate the addition in the following way
# # Create an outer function that will accept two parameters, a and b
# # Create an inner function inside an outer function that will calculate the addition of a and b
# # At last, an outer 
# def take(a,b):
#     def sum():
#         return a + b
#     add = sum()
#     return add
# print(take(10,20))


# # 4. Find the largest item from a given list.
# # x=[1,2,3,4,5,6,7,8]
# x=[1,2,3,4,5,6,7,8]
# c = 0
# for i in x:
#     if i > c:
#         c = i
# print(c)


# 5. What is the difference between 10 / 3 and 10 // 3?
# Ans : 10 / 3 will give you the division of 10 and 3 including the decimals
# Whereas 10 // 3 wil give you the division of 10 and 3 without the decimals.



# 6. What about two asterisks (**)?
# Ans : It will give you the power of any number . For eg 2 ** 2 == 4 is True


# 7. What is the difference between local and global variables?
# Ans : Global variables are those variables which can be used anywhere within the program.
# Ans : Local variables are those which are used within a function.


# # 8. Write a function called fizz_buzz that takes a number.
# # If the number is divisible by 3, it should return “Fizz”.
# # If it is divisible by 5, it should return “Buzz”.
# # If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# # Otherwise, it should return the same number.
# def fizz_buzz(a):
#     if a % 5 == 0 and a % 3 == 0:
#         print("FizzBuzz")
#     elif a % 3 == 0:
#         print("Fizz")
#     elif a % 5 == 0:
#         print("Buzz")
#     else:
#         print(a)
# fizz_buzz(5)
    

# # 9. Write a function for checking the speed of drivers. 
# # If speed is less than 70, it should print “Ok”.
# # if the speed is 80, it should print: “Warning”.
# def check(speed):
#     if speed < 70:
#         print("Ok")
#     elif speed == 80:
#         print("Warning")
#     else:
#         pass
# check(30)


# # 10. Write a program that prompts the user to input a positive integer. It should then print the multiplication table of that number.
# a = int(input("Enter a positive number :"))
# if a >= 0:
#     c = a
#     for i in range(1,11):
#         c = i * a
#         print(f"{a} * {i} = {c}")
# else:
#     print("Enter a positive number more than 0.")


# # 11. Write a program that prompts the user to input an integer and then outputs the number with the digits reversed. For example, if the input is 12345, the output should be 54321.
# a = input("Enter a integer :")
# for i in reversed(a):
#     print(i, end="")


# # 12. Write a python program that return the number of characters in a string. 
# myList = "Parameter"
# a = len(myList)
# print(a)


# # 13. Write a Python program to multiply all the numbers in a list using while and for loop.
# list = [8,2,3,-1,7]
# b = 0
# d = 1
# c = len(list)
# while c != 0:
#     d = d * list[b]
#     b = b + 1
#     c = c - 1
# print(d)


# # 14. Write a Python program to sum all the numbers in a list using for loop and while loop.
# list = [8, 2, 3, 0, 7]
# b = 0
# d = 0
# c = len(list)
# while c != 0:
#     d = d + list[b]
#     b = b + 1
#     c = c - 1
# print(d)


# # 15. Accept string from the user and display only those characters which are 
# # present at an even index.
# a = input("Enter a string :")
# c = len(a)
# for i in range(c):
#     if i % 2== 0:
#         print(a[i], end="")
#     else:
#         pass


# # 16. Accept string from the user and display only those characters which are 
# # present at an odd index.
# a = input("Enter a string :")
# c = len(a)
# for i in range(c):
#     if i % 2 != 0:
#         print(a[i], end="")
#     else:
#         pass


# # 17. Sum : 1 to 10 (or any number) using while loop.
# a = int(input("Enter a number :"))
# b = True
# c = 0
# d = a + 1
# while b == True:
#     for i in range(1,d):
#         c = c + i
#     b = False
# print(c)
    

# # 18. Write a Python program to print the even numbers from a given list. 
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a = len(list)
# for i in range(a):
#     c = list[i]
#     if c % 2== 0:
#         print(c)
#     else:
#         pass

# # 19. Write a Python program to print the odd numbers from a given list. 
# list  = [12,13,14,15,16,17,18,19]
# a = len(list)
# for i in range(a):
#     c = list[i]
#     if c % 2!= 0:
#         print(c)
#     else:
#         pass


# # 20. Write a program to accept percentage and display the Category according to the  following criteria :
# # Percentage	Category
# # < 41	                     Failed
# # >=41 & <55	Fair
# # >=55 & <65	Good
# # >=65	                     Excellent
# a = int(input("Enter your percentage :"))
# if a < 0:
#     print("Enter a valid marks.")
# elif a < 41:
#     print("Failed")
# elif a >= 41 and a < 55:
#     print("Fair")
# elif a >= 55 and a <65:
#     print("good")
# elif a >= 65:
#     print("Excellent")