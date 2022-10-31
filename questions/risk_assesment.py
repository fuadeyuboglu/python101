q1 = input("Are you a cigarette addict older than 75 years old? (Yes or No):")
q2 = input("Do you have a severe chronic disease? (Yes or No):")
q3 = input("Is your immune system too weak? (Yes or No):")

age = bool(q1.lower() == "yes")
chronic = bool(q2.lower() == "yes")
immune = bool(q3.lower() == "yes")


if age or chronic or immune:
    print("\nYou are in risky group")
else:
    print("\nYou are not in risky group")
