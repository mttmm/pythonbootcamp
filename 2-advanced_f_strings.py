# --- Python Production Bootcamp: Challenge 1.2 ---
# Topic: Advanced f-strings (Multiple Variables)


def main():
    # 1. Collect 4 pieces of information
    name = input("Enter a name: ")
    place = input("Enter a place (e.g., Mars, The Kitchen): ")
    # YOUR CODE HERE: Ask for an 'object'adjective = input("Enter a adjective :")
    adjective =input("Enter a adjective :" )
    # YOUR CODE HERE: Ask for an 'adjective'
    object = input("Enter a object :")

    # 2. Build the story
    # Hint: You can put a \n inside your string to start a new line!
    # Example: print(f"Line 1\nLine 2")

    # YOUR CODE HERE:
    # Print a story like: "Once upon a time, [name] went to [place].
    # They found a [adjective] [object]. It was the best [object] ever!"
    print(f"Once upon a time {name} and found an {adjective} {object} and it took him to {place}")

if __name__ == "__main__":
    main()