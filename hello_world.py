# Wite a program where the output is "Hello World"
# Test your code by typing python ./hello_world.py in the terminal and observe the output


# print("hello world!")
# print ("I did it dad!")
# print ("yippe")
##################################


# Write a program that asks the user for their first name 
# and says hello to that person

# name = input("please enter your name :")

# print(f"Hello, {name}")
# print("hows your day going" )

def main():
    user_name = input("What is your name? ")

    # 1. Ask the user for their favorite hobby and store it in a variable
    # Hint: use the input() function just like the name one above

    ## ADD CODE HERE
    user_hobby = input("what is a hobby you have? ")
    # 2. Use an f-string to print  "Hello [name], I hear you are great at [hobby]!"
    # Hint: put an "f" before the first quote, and {} around your variables

    ## ADD CODE HERE

    print(f"Hello {user_name} I heard that you were good at {user_hobby} !")

if __name__ == "__main__":
    main()
