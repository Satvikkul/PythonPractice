# #import random
# #import math
# #string.method()
#
# x = "happy birthday".count("day")
# # print(x)
#
# x = "happy birthday"
# print(x.upper())
# print(x.lower())
# print(x.capitalize())
# print(x.title())
#
# #  x.isalpha()
# #  x.islower()
# #  x.isupper()
# #  x.istitle()
# #  x.isalnum()
# #  x.isdigit()
#
# # count start of a letter using index
# print(x.index("birthday"))
#
# y = "000000Happy Birthday000000"
# print(y.strip("0"))
# #  y.lstrip("0") remove left zeroes similarly y.rstrip("0")
#
# # # use .strip() to remove empty spaces
# # name = input("what is your name?: ").strip()
# # print(name)
#
# print("\n")
# #####SLICE
# #   variable[start:end:step]
#
# word = "Supercalifragilistic"
# print(word[0:5:1])

# word = "antidisestablishmentarianism"
#
# answer = word[word.index('establishment'):word.index('arian')]
# print(answer)

# Boolean

# IF Statement

# # if condition:
# #   something...
# num1 = 500
# num2 = 500
# if num1 > num2 :
#     print("num1 in bigger than num2")
# elif num2 > num1:
#     print("num2 is bigger")
# else:
#     print("both are equal")

# Logical operators AND OR

# Data Structures
# LIST TUPLES DICTIONARY

# lst = [1,2,3,4,5,6, "a","b",True, False]
# x = lst[3]
# #print(lst[0:4])
#
# listInlist = [1,2,[3,4,5],6,7,8]
# # print(listInlist[2])
# # print(listInlist[2][0:2])
#
# table = [[1, 2, 3], ["a", "b", "c"], [4, 5, 6]]
# print(table[1])


# TUPLES
#our_tuple = (1,2,3,"a","b","c")
#print(type(our_tuple))
# iterable that means our_tuple[0:3] will give 1,2,3

# DICTIONARIES

# students = {
#      "Alice": ["ID001",25,"A"],
#      "Bob": ["ID002",27,"B"],
#      "Claire": ["ID003",17,"C"],
#      "Dan": ["ID004",23,"D"],
#      "Emma": ["ID005",22,"E"]
#      }
#
# students["Fred"] = 25
# students["Fred"] = 28
#
# del students["Fred"]
# # print(students)
# # print(students.keys())
# # print(students.values())
# # a = list(students.keys())
# # print(a)
# # print(a[2:5])
# # print(students.items())
# #print(students["Claire"][:2])
#
# students1 = {
#      "Alice": {"id":"0001","age":26,"grade":"A"},
#      "Bob": {"id":"0002","age":27,"grade":"B"},
#      "Claire": {"id":"0003","age":17,"grade":"C"},
#      "Dan": {"id":"0004","age":20,"grade":"D"},
#      "Emma": {"id":"0005","age":24,"grade":"E"}
#      }
# print(students1["Dan"]["age"])
# print(students1["Alice"]["id"])
# print(students1["Emma"]["grade"])

# LOOPS

# WHILE LOOP
# num = 1
# num1 = 1
# # while num <= 10:
# #     print(num)
# #     num = num + 1
#
# while num <= 10:
#     if num % 2 == 0:
#         print(num)
#     num = num + 1
# print("\n")
# while num1 <= 10:
#     if num1 % 2 != 0:
#         print(num1)
#     num1 = num1 + 1


# names = []
#
# while len(names) < 6:
#     new_name = input("add name: ").strip().capitalize()
#     names.append(new_name)
# print(names)

# FOR loop
# range(start:stop:steps)
# for i in range(1,11):
#     print(i)
# vowel = 0
# consonant = 0
# for letter in "My name is Satvik Kulshreshtha":
#     if letter.lower() in 'aeiou':
#         vowel = vowel + 1
#     elif letter == " ":
#         pass
#     else:
#         consonant = consonant + 1
#
# print("Total number of vowels = {}".format(vowel))
# print("Total number of consonants = {}".format(consonant))
#

# students = {
#     "male": ["anupam","satvik","mudit","prashant","arjun","harsha"],
#     "female": ["laxmi","madhu","megha","swadha","ekta"]
# }
#
# for key in students.keys():
#     for name in students[key]:
#         if 'l' in name:
#             print(name)

# LIST COMPREHENSION

# even_num = [x for x in range(1, 50) if x % 2 == 0]
# print(even_num)

# word = ["the","quick", "brown","fox","jumps","over","the","lazy","dog"]
# ans = [[w.upper(),w.lower(),len(w)] for w in word]
# print(ans)

# FUNCTIONS

# def add(x,y):
#     res = x + y
#     print(res)
#
# add(2,3)

# def rev(text):
#     text = text[::-1]
#     print(text)
#
# #rev("hello")
# rev([1,2,3,4])

# SCOPE of VARIABLE

# a = 100
#
# def f1():
#     a = 200
#     print(a)
#
# def f2():
#     print(a)
#
# f1()
# f2()

# ARGUMENTS AND PARAMTER
#
# def about(name,age,likes):
#     sentence = "Meet! {}, They are {} years old and they like {}".format(name,age,likes)
#     print(sentence)
#
# about("jack and jill",23,"Python")

# ARGS and KWARGS [packing and unpacking]

# unpacking
# print(1,2,3,4,5)
# number = [1,2,3,4,5]
# print(number)
# print(*number)   # * is used to unpack the list
### in packing, it makes all argument into mini individual arguments, this can be done to any iterable datatype

# packing
# def add(x,y):
#     print(x + y)
# add(1,2)

# def add(*numbers):
#     total = 0
#     for num in numbers:
#         total = total + num
#     print(total)
#
# add(1,2,3,4,5,6,7,8,9)

# def about(name, age, likes):
#     sentence = "Meet! {}, They are {} years old and they like {}".format(name, age, likes)
#     print(sentence)
#
#
# dict = {
#     "name": "satvik", "age": 26, "likes": "Python"
# }
# about(**dict) # two stars (**) for keywords
# about(name="t",age="29",likes="sae")

# def foo(**kwargs):
#     for key,value in kwargs.items():
#         print("{} : {}".format(key,value))
#
# foo(satvik="male", T="female",mudit="male")

# OBJECT AND CLASSES


