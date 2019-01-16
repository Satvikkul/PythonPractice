# So this project is going to let users choose from a range of films and the user will pick a film and
# then the program will ask them for their age.
# If they're old enough to watch the film and there are enough seats available then the program will let
# them use a book to see the film.
# If not the program will tell them that they're too young or there's nine of seats available or whenever.

films = {
    "Finding Dory": [3, 5],
    "Bourne": [18, 5],
    "Tarzan": [15, 3],
    "Ghost Busters": [12, 5]
}

while True:
    choice = input("What film would you want to watch?: ").strip().title()
    if choice in films:
        #print("tickets left for this film: ", films[choice][1])
        age = int(input("How old are you?: ").strip())

        if age >= films[choice][0]:
            if films[choice][1] > 0:
             print("Enjoy the film")
             films[choice][1] = films[choice][1] - 1
             print("Tickets left: ",films[choice][1])
            else:
                print("This Film is Sold Out")
        else:
            print("You are too young to see this film")

    else:
        print("We don't have that film...")


