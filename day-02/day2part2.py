def read_input(filename):
    with open(filename) as file:
        return [line.strip() for line in file]

inputs = read_input("day-02/input")
hoz = 0
vert = 0
aim = 0
final = 0

for x in inputs:
    d, s = x.split(' ')
    s = int(s)
    
    if d == "down": aim = aim + s
    elif d == "up": aim = aim - s
    else: 
        hoz = hoz + s
        vert = vert + s * aim

final = vert * hoz
print(final)