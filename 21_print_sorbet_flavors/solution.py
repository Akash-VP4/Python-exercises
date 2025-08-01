FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

for i in range(len(FLAVORS)):
    for j in range(i + 1, len(FLAVORS)):
        print(FLAVORS[i] + ", " + FLAVORS[j])
