known_users = ["T", "J", "Kartik", "Bhadu", "Bajaj", "Rajoria", "Yadav"]
print(known_users)
while True:
    print("Hi, my name is Travis")
    name = input("What is your name?: ").strip().capitalize()
    if name in known_users:
        print("Hello {}!\n".format(name))
        remove = input("Would you like to be removed from the list? (y/n): \n").lower()
        if remove == 'y':
            known_users.remove(name)
        elif remove == 'n':
            print("No Problem....")
        #print(known_users)
    else:
        print("I don't think we have met {}\n".format(name))
        add = input("Would you like to be in the list? (y/n) : \n").strip().lower()
        if add == 'y':
            known_users.append(name)
        elif add =='n':
            print("Okay....Have a nice day...!")

        #print(known_users)

# remove something using index then use "del.listname[index]"
# want to delete some elements then slicing can be done "del.listname[start:end]"
# want to add element anywhere in the list then use listname.insert(index)

