# Addition of two number 
# a = int(input("Enter your input number: "))
# b = int(input("Enter your second Number: "))
# sum = a + b
# print("Sum of two Number ia = ",sum)

# Area of Circle 
 
# r = int(input("Enter radius of Circle : "))
# pi = 3.14
# a =  pi * r * r
# print("Area of circle is = " , a)


# Dicision making statment 
# if stateent 

# x = 10
# if x > 5:
#  print("x is greater then 5")
# else :
#  print("x is not graeter than 5")

# a = int(input("Enter your first number is : "))
# b = int(input("Enter your second number is : "))
# if a > b:
#   print("a is greater than b ")
# else :
#   print("b is greater than a ")

#  nested if-elif-if statement 

# score = int(input("Enter your score : "))
# if score > 90:
#   print("grade A")
# elif score < 90 & score > 80:
#   print("grade B")
# elif score < 80 & score >70:
#   print("grade C")
# elif score < 70 & score > 60:
#   print("grade D")
# elif score < 60 and score > 50:
#   print("grade E")
# else:
#   print("fail")


#  loop 
# for loop 


# for i in range(29):
#   print(i, end = " ")

# for i in range(1 , 10):
#   print(i , end = " ")


# for i in range(1 , 15 , 2):
#   print(i , end = " ")

# nested loop 
# for i in range(5):
#   print()
#   for j in range(5):
#     print("*", end = " ")

#  Sum of digits 

# n = int(input("Enter your input digits : "))
# tot = 0

# while(n>0):
#   digit = n % 10
#   tot = tot + digit
#   n = n // 10
#   print("Sum of given digits is = ", tot)

# factorial of any given number 

# n = int(input("Enter your number : "))
# fact = 1
# while(n > 0):
#  fact = fact * n
#  n = n - 1
#  print("factorial of number is = ",fact)

# String 
# Joining two string 

# name = "Suraj"
# name1 = "kumar"
# fullname = name + " "+ name1
# print(fullname)

# name = "Suraj"
# print(len(name))

# name = "Suraj kumar"
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.title())

#  Spliting and joining operation

# sentence = "Hello , How are you ?"
# word = sentence.split()
# print(word)

# name = ["Hello","how","are","you"]
# sentance = " ".join(name)
# print(sentance)

# String slicing 

# name = "Suraj kumar"
# print(name[1:7])

# name = "Suraj kumar"
# print(name[:5])
# print(name[1:])
# print(name[6:-1])
# print(name[::3])
# print(name[::-1])

# list 
# number = [1,2,4,5,6,6]
# name = ['apple','orange','banana']
# mixed_items = [1,"Suraj kumar",3.63,True]
# print(number)
# print(name)
# print(mixed_items)

# fruits = ['mango','banana','grapes']
# fruits.append("watermelan")
# print(fruits)
# print(fruits[2])
# fruits.remove("mango")
# print(fruits)

# number = [1,3,5,7,8,89,9]
# subset = number[1:4]
# print(subset)

# Concatenation of two list 

# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,0]
# final = list1 + list2
# print(final)

#  list comprehension

# cube = []
# for i in range(12):
#   cube.append(i**3)
#   print("Cubes of number is = ",cube)

#  tuple 

# coordinates = (10,20)
# coordinates [0] = 2
# print(coordinates)


# coordinates = (29,82)
# x,y = coordinates
# print(x,y)

# length and membership  test 

# name = ['apple','banana','grapes','papaya']
# print(len(name))
# print("banana" in name)

# Write a python program to add an items in a tuple

tuplex = (1,2,3,4,5,6)
listex = list(tuplex)
listex.append(30)
tuplex = tuple(listex)
print(tuplex)