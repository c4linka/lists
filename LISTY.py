"""listNames = ["Ewa", "Ala", "Marcin"]


print("Ewa" in listNames)

listNumbers = [3, 2, 4]

(listNumbers + [5])

print(listNumbers)


listNumbers += [5]


print(listNumbers)
"""
namesList = ["Ewa", "Ala", "Kotki", "Pieski"]

access = input("Hello, I have an important list. You can check it, if you are on it. Type your name: ")
access = access.capitalize()

if access in namesList:
    print("You have an access, this is the secret list: ")
    print(namesList)
else: print("Access denied!")
