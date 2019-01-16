from random import choice

questions = ["Why is sky blue?: ", "Who created Apple.Inc?: ", "Who is Bill Gates?: "]
questions = choice(questions)
answer = input(questions).strip().lower()

# answer = input("melody itni choclaty kyun hai?????  ").strip().lower()

while answer != "just because":
    answer = input("Why??  ").strip().lower()
print("ohhh okay")


