# --- Python Production Bootcamp: Indentation Lab ---
# Topic: The "Security Gate" Challenge

# Level 1: Ask for the secret password.

# Inside Level 1: Ask for the secret handshake.

# Inside Level 2: Ask for a favorite color.

# If they get all three right, they get to the "Vault."

# If they get any wrong, the program should use else to kick them out!

def main():
    print("--- WELCOME TO THE SECRET BASE ---")

    # DOOR 1
    password = input("Enter the secret password: ")

    if password == "pizza":
        print("Password correct! You entered the First Room.")

        # DOOR 2 (This only happens if DOOR 1 is opened!)
        # YOUR CODE HERE: Ask for a secret_handshake.
        # If it is "high-five", go to Door 3.

            # DOOR 3 (This only happens if DOOR 2 is opened!)
            # YOUR CODE HERE: Ask for a favorite_color.
            # If it is "blue", print "ACCESS GRANTED TO THE VAULT!"

            # YOUR CODE HERE: Add an 'else' for Door 3
            # (e.g., print "Wrong color! Alarm sounding!")

        # YOUR CODE HERE: Add an 'else' for Door 2
        # (e.g., print "Wrong handshake! Guards are coming!")

    else:
        print("Wrong password. Access Denied at the front gate.")

if __name__ == "__main__":
    main()