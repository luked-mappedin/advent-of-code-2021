def read_input(filename):
    with open(filename) as file:
        return [line.strip() for line in file]

inputs = read_input("day-02/input")
hoz = 0
vert = 0
final = 0

for x in inputs:
    d, s = x.split(' ')
    s = int(s)
    if d == "forward": hoz = hoz + s
    elif d == "down": vert = vert + s
    else: vert = vert - s

final = vert * hoz
print(final)