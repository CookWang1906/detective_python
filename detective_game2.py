#stupid ah detective game
import random

characters = ["Alice", "Bob", "Charlie", "David"]
murderer = random.choice(characters)
victim = random.choice([i for i in characters if i != murderer])
weapon = random.choice(["knife", "gun", "poison", "rope"])

print("Welcome to the Detective Game!")
print(f"You are a detective trying to solve a murder mystery.")
print("You have several suspects: ", end="")
print(", ".join([i for i in characters if i != murderer]))

while True:
    print("\nWhat would you like to do?")
    print("1. Question a suspect")
    print("2. Inspect the crime scene")
    print("3. Make an accusation")
    print("4. Quit?")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        suspect = random.choice([i for i in characters if i != murderer])
        print(f"You question {suspect}.")
        if suspect == murderer:
            print(f"{suspect} acts nervous but doesn't confess.")
        else:
            print(f"{suspect} has an alibi and is not the murderer.")
    elif choice == "2":
        print("You inspect the crime scene and find some clues.")
        print(f"You found a {weapon} covered in fingerprints and a dead body of {victim}.")
        print(f"You also find a bloody footprint that doesn't match the victim's.")
    elif choice == "3":
        accusation_suspect = input("Who do you accuse? ")
        accusation_weapon = input("What weapon do you accuse them of using? ").lower()

        if accusation_suspect == murderer and accusation_weapon == weapon:
            print("Congratulations! You've solved the case and captured the murderer!")
        else:
            print("Your accusation was incorrect. The murderer is still on the loose.")
    elif choice == "4":
        # Quit the game
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")