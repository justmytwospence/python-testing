ages = {
    "Jim": 30,
    "Pam": 28,
    "Kevin": 33,
}

person = input("Get age for: ")

try:
    print(f"{person}'s age is {ages[person]}.")
except KeyError:
    print(f"{person}'s age is unknown.")
