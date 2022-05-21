# #1. Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
# a=int(input("enter a num:"))
# b=int(input("enter another num:"))
# if a==b:
#     print("1")
# elif a>b:
#     print("2")
# else:
#     print("3")

# #2. Print "Hello" if a is equal to b, and c is equal to d.
# a=int(input("enter a num:"))
# b=int(input("enter another num:"))
# c=int(input("enter another num:"))
# d=int(input("enter another num:"))
# if a==b and c==d:
#     print("hello")
    
# # 3. Print "Hello" if a is equal to b, or if c is equal to d.
# a=int(input("enter a num:"))
# b=int(input("enter another num:"))
# c=int(input("enter another num:"))
# d=int(input("enter another num:"))
# if a==b or c==d:
#     print("hello")
    
#     #4. For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative and print ‘zero’ if it is 0.
# x=int(input("enter a number:"))
# if x > 0:
#     print("true")
# elif x < 0:
#     print("false")
# elif x == 0:
#     print("zero")
    
#     #5. Check whether the user input number is even or odd and display it to user.
# a=int(input("enter anumber"))
# if a%2==0:
#     print("even")
# else:
#     print("odd")
    
     #6.  WAP which accepts marks of four subjects and display total marks, percentage and grade.
# # Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail
 
# marks1=int(input("enter your marks in math: "))
# marks2=int(input("enter your marks in english: "))
# marks3=int(input("enter your marks in science: "))
# marks4=int(input("enter your marks in computer: "))
# total_marks=marks1+marks2+marks3+marks4
# percentage=total_marks/4
# print(f"Your total marks is {total_marks}")
# print(f"Your percentage is {percentage}%")
# if percentage>70:
#     print("distinction")
# elif percentage>60:
#     print("First")
# elif percentage>40:
#     print("pass")
# else :
#     print("fail")




# # 7. What is the output of ‘APPLE’ > ‘apple’?
# # print('APPLE'>'apple')
# a="APPLE"
#print(a.lower())


# # 8. Write a Python program to display your details like name, age, address in three different lines.

# name="rajil shrestha"
# age=18
# address="banepa"
# print(f"{name} \n{age} \n{address}")

# # 9. Write a python program which accepts the radius of circle from user and compute the area.
# radius=float(input("Enter the radius: "))
# area=(22/7)*radius**2
# print(f"the area of circle is {area}")



# # 10. A school decided to replace the desks in three classrooms. Each desk sits two students. 
# # Given the number of students in each class, print the smallest possible number of desks that can be purchased.
# # The program should read three integers: the number of students in each of the three classes, a, b and c respectively.
# # Hint. In the first test there are three groups. The first group has 20 students and thus needs 10 desks. 
# # The second group has 21 students, so they can get by with no fewer than 11 desks. 
# # 11 desks are also enough for the third group of 22 students. So, we need 32 desks in total. 


# classA=int(input("Enter the number of students in class A: "))
# classB=int(input("Enter the number of students in class B: "))
# classC=int(input("Enter the number of students in class C: "))
# total_desk=(classA//2+classB//2+classC//2)+(classA%2+classB%2+classC%2)
# print(f"total desk required is {total_desk}")





# # 11. Given three integers, print the smallest one. (Three integers should be user input)
# a=int(input("enter a number: "))
# b=int(input("enter a number: "))
# c=int(input("enter a number: "))
# if a<b and a<c:
#     print(f"{a} is the smallest number")
# elif b<a and b<c:
#     print(f"{b} is the smallest number")
# elif c<a and c<b:
#     print(f"{c} is the smallest number")
# else:
#     print("all number are equal.")


# 12. Write a program that takes three numbers and prints their sum. Every number is given on a separate line.
# a=int(input("enter a number: \n"))
# b=int(input("enter a number: \n"))
# c=int(input("enter a number: \n"))
# sum=a+b+c
# print(f"their sum is {sum}")

# # 13. Write a program that reads the length of the base and the height of a right-angled triangle and prints the area.
# # Every number is given on a separate line.

# length=int(input("enter the lenght of the base: \n"))
# height=int(input("enter the height of the right-angled triangle: \n"))
# area=0.5*length*height
# print(f"the area is {area}")


# # 14. N students take K apples and distribute them among each other evenly. The remaining 
# # (the undivisible) part remains in the basket. How many apples will each single student 
# # get? How many apples will remain in the basket? The program reads the numbers N and 
# # K. It should print the two answers for the questions above.


# no_of_student=int(input("Enter the number of Student: "))
# no_of_apples=int(input("Enter the number of Apple: "))
# apple_per_student=no_of_apples//no_of_student
# remaning_apple=no_of_apples%no_of_student
# print(f"Each student got {apple_per_student} apples", end=" and ")
# print(f"remaining apples in the basket is {remaning_apple}")