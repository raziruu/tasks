# # 1. Write a program to accept percentage and display the Category according to the  following criteria :

# # Percentage	Category
# # < 40	                     Failed
# # >=40 & <55	Fair
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


# # 2. Write a Python Program to Swap Two Variables.
# a = 10
# b = 20
# c = a
# a = b
# b = c
# print(a)
# print(b)


# # 3. Write a program to print multiplication table of a  number 10 using for loop.
# c = 1
# for i in range(1,11):
#         c = i * 10
#         print(f"10 * {i} = {c}")


# # Question no 4. Print list in reverse order using a loop. Hint: list1=[1,2,3,4]
# list1=[1,2,3,4]

# for i in reversed(list1):

#     print(i, end='')



# #  Question no 5. Display numbers from -10 to -1 using for loop.
# for i in range(-11,0):

#     print(i)

# # 7. Find the factorial of a number 5.
# for i in range(1,6):
#     if 5 % i == 0:
#         print(i)


# # # 8. Use a loop to display elements from a given list present at odd index positions. 
# list = [10,20, 30, 40, 50, 60, 70, 80, 90, 100]
# a = len(list)
# for i in range(a):
#     c = list[i]
#     if i % 2!= 0:
#         print(c)
#     else:
#         pass


# # 9. Calculate the cube of all numbers from 1 to a given number. (1-6)
# a = int(input("enter a number:"))
# print(1 ** 3)


# Question no 10.  Print First 10 natural numbers using for loop.
# for i in range(1,11):
#     print(i)