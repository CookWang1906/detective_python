import time
import random

#Remember the suspect is reported to be like that, but its not actually his real look. Maybe he disguise, so you must have a cold head.
#height
height = [1.7, 1.75, 1.8, 1.85, 1.9, 1.95, 2]
rand_height = random.choice(height)
if rand_height == 1.7:
    height = [1.7, 1.75]
    rand_height = random.choice(height)
elif rand_height == 1.75:
    height = [1.7, 1.75, 1.8]
    rand_height = random.choice(height)
elif rand_height == 1.8:
    height = [1.75, 1.85, 1.8]
    rand_height = random.choice(height)
elif rand_height == 1.85:
    height = [1.8, 1.85, 1.9]
    rand_height = random.choice(height)
elif rand_height == 1.9:
    height = [1.95, 1.9, 1.85]
    rand_height = random.choice(height)
elif rand_height == 1.95:
    height = [2, 1.95, 1.9]
    rand_height = random.choice(height)
elif rand_height == 2:
    height = [2, 1.95]
    rand_height = random.choice(height)
    
#race
race = ["White", "Black", "Asian"]
rand_race = random.choice(race)

#hair
hair = ["Black hair", "Bald", "Brown hair"]
rand_hair = random.choice(hair)

#information
suspect = ["Michael", "Jason", "Johnny", "Lee", "Wang", "Long", "Jamal", "Daniel", "James", "Jack", "Darius", "Kai", "Hayato", "John", "Harold", "Gary", "Richard"]
sus_michael = [1.85, "White", "Bald"]
sus_jason = [1.9, "White", "Bald"]
sus_johnny = [1.8, "White", "Brown hair"]
sus_lee = [1.75, "Asian", "Black hair"]
sus_wang =[1.75, "Asian", "Black hair"]
sus_long = [1.7, "Black", "Black hair"]
sus_jamal = [1.8, "Black", "Black hair"]
sus_daniel = [1.9, "Black", "Brown hair"]
sus_james = [1.85, "Black", "Bald"]
sus_jack = [2, "White", "Bald"]
sus_darius = [2, "White", "Black hair"]
sus_kai = [1.7, "Black", "Black hair"]
sus_hayato = [1.75, "Asian", "Brown hair"]
sus_john = [1.85, "White", "Brown hair"]
sus_harold = [1.95, "White", "Bald"]
sus_gary = [1.95, "White", "Black hair"]
sus_richard = [1.95, "White", "Brown hair"]

#play time
print("Here are the name of the suspect\n",suspect)

time.sleep(2)
print("\nHere are the info of the suspect in order of the name")
print("Michael: ", sus_michael)
print("Jason:   ", sus_jason)
print("Johnny:  ", sus_johnny)
print("Lee:     ", sus_lee)
print("Wang:    ", sus_wang)
print("Long:    ", sus_long)
print("Jamal:   ", sus_jamal)
print("Daniel:  ", sus_daniel)
print("James:   ", sus_james)
print("Jack:    ", sus_jack)
print("Darius:  ", sus_darius)
print("Kai:     ", sus_kai)
print("Hayato:  ", sus_hayato)
print("John:    ", sus_john)
print("Harold:  ", sus_harold)
print("Gary:    ", sus_gary)
print("Richard: ", sus_richard)

form = input("\nDo you want them to stand by height? (Y/N): ")
if form == "Y":
    print("\nLong:    ", sus_long)
    print("Kai:     ", sus_kai)
    print("Hayato:  ", sus_hayato)
    print("Lee:     ", sus_lee)
    print("Wang:    ", sus_wang)
    print("Johnny:  ", sus_johnny)
    print("Jamal:   ", sus_jamal)
    print("Michael: ", sus_michael)
    print("James:   ", sus_james)
    print("John:    ", sus_john)
    print("Daniel:  ", sus_daniel)
    print("Jason:   ", sus_jason)
    print("Richard: ", sus_richard)
    print("Gary:    ", sus_gary)
    print("Harold:  ", sus_harold)
    print("Jack:    ", sus_jack)
    print("Darius:  ", sus_darius)
else:
    print()

killer = random.choice(suspect)

time.sleep(3)
print(f"\nThe suspect is said to be about {rand_height}m, {rand_race}, {rand_hair}.")

eliminate = input("\nWho do you think is the killer?: ")

if eliminate == killer:
    print("Congratulations, you have found the killer!")
elif eliminate != killer:
    print(f"You failed! The real killer is {killer}.")
else:
    print()