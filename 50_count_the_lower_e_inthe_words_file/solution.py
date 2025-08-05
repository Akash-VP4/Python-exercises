file = open("words.txt")

count = 0

for line in file:
    count += line.count("e")

print(count)
