freq = {}
file = open("words.txt")

count = 0

for line in file:
    for letter in line:
        freq[letter] = freq.get(letter, 0) + 1
        count += 1

for key, value in freq.items():
    print(key + ":", f"{value/count:.2f}")
