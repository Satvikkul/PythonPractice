# get user email
email = input("What is your email address?: ").strip()

# slice username and domain
username = email[:email.index("@")]

domain = email[email.index("@") + 1:]
# format message
output = "Your username is {} and your domain name is {}".format(username, domain)

# display output
print(output)

