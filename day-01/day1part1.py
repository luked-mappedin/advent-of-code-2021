
inputs = open("inputs.txt")
numbers = list(inputs)
total = 0

for position, _ in enumerate(numbers):

    if numbers[position] > numbers[position - 1]:
        total = total + 1
    else: next

print(total) 
