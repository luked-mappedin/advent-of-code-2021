def read_integers(filename):
    with open(filename) as file:
        return [int(line.strip()) for line in file]

numbers = (read_integers("input"))

total = 0

for position, _ in enumerate(numbers):
    if numbers[position] > numbers[position - 1]: total = total + 1

print(total)
