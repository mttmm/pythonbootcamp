# get the user's name
# print a greeting message
# ask if you want to start the story
# Start the story
name = input("What is your name? ")
start_story = input("Do you want to start the story? (yes/no) ")
if start_story == "yes":
    print(f"Once upon a time on a stormy night there was a man named {name}")
    outside = input("Do you want to go outside? (yes/no) ")
    if outside == "yes":
        print("You go outside and feel the rain on your head it hits you hard and all the sudden it starts to hail")
else:
        print("good bye")
        stay = input("Do you stay outside? (yes/no) ")
        if stay == "yes":
            print(
            "The hail hits you harder and harder you run and all the sudden you find a cave"
        )
        inside = input("Do you go in the cave? (yes/no) ")


# ==========================================================
# TECH LEAD REVIEW: Phase 2 - Fixing the "Logic Leak"
# ==========================================================
# Current Issue: The"Logic Leak."
# Even if a player says "no" to the story, the questions keep
# coming. We need to "Nest" our questions inside the 'if' blocks.
#
# NEW CONCEPT: THE "IF" TREE
# Think of an 'if' statement like a gate. If the gate is closed
# (the user said "no"), Python skips everything INSIDE that
# gate and moves to the very end.
# ==========================================================

# --- YOUR NESTING CHALLENGE ---
# 1. Take your 'outside' variable and move it INSIDE the
#    first 'if start_story == "yes":' block.
# 2. This means 'outside' must be indented (4 spaces or 1 tab).
# 3. Add an 'else:' statement at the very bottom that says
#    "Okay, goodbye!" if they say "no" to the story.

# HINT ON STRUCTURE:
# if condition1:
#     print("Success 1")
#     if condition2:
#         print("Success 2")
#     else:
#         print("Failed at Step 2")
# else:
#     print("Failed at Step 1")


##########################################################################

# name = input("What is your name? ")
# start_story = input("Do you want to start the story? (yes/no) ").lower()

# if start_story == "yes":
#     print(f"Once upon a time there was a man named {name}")

#     # Notice this next part is INDENTED!
#     # It only happens if they said "yes" to the story.
#     outside = input("Do you want to go outside? (yes/no) ").lower()

#     if outside == "yes":
#         print("You go outside and feel the rain...")
#         # Stay/Cave logic would go here, indented even further!
#     else:
#         print("You stayed home where it's dry. Game Over.")

# else:
#     print("Maybe another time!")
