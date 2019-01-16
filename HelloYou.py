name = input("What is your name?: ")
# print(name)

age = input("What is your age?: ")

city = input("What is the city you live in?: ")

love = input("What do you love doing?: ")
# print(name)
# print(age)
# print(city)
# print(love)

string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name,age,city,love)
print(output)
#print(name + " aged " + age + " " + "lives in " + city + " and love to " + love)



