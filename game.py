import random
user_action=input("Enter a choice(rock,paper,scissor):")
possible_action=["rock","scissor","paper"]
computer_action=random.choice(possible_action)
print(f"\nYou chose {user_action},computer chose {computer_action}.\n")
if user_action=="rock":
    print("Rock smashes scissor! You win!")
else:
    print(("Paper covers rock! You lose."))
if user_action=="paper":
    if computer_action=="rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissor cuts paper! You lose:")
elif user_action == "Scissor":
    if computer_action=="paper":
        print("Scissor cuts paper! You win !")
    else:
        print("Rock smashes scissors! you lose.")
