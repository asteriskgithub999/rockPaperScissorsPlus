import random
print("""
Rock Paper Scissors Plus v1.0
-----------------------------
""")
possiblechoices = ["rock", "paper", "scissors", "mic", "gun", "goku"]
user = input("Choose a move: ")
if user not in possiblechoices:
    while user not in possiblechoices:
        user = input("Invailid. Try again: ")
pc = random.choice(possiblechoices)
if pc == user:
    print(f"You both chose {user}")
elif pc == "paper" and user == "rock":
    print(f"PC chose {pc}! It wins!")
elif pc == "rock" and user == "paper":
    print(F"PC chose {pc}! You win!")
elif pc == "scissors" and user == "paper":
    print(f"PC chose {pc}! It wins!")
elif pc == "paper" and user == "scissors":
    print(f"PC chose {pc}! You win!")
elif pc == "gun" and user != "goku":
    print("*shoot* pc wins.")
elif pc == "goku":
    print("KAMEH! KAMEH! KAMEH! KAHHHHHH! u die")
elif user == "goku":
    print("u win")
elif pc == "mic":
    print("u win")
elif user == "mic":
    print("u lose")