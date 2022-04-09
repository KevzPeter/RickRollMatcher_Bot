map = {}

with open("lyrics.txt", "r") as file:
    for line in file.readlines():
        for word in line.strip().lower().split(" "):
            if(word in map):
                map[word] += 1
            else:
                map[word] = 1

print(map)
