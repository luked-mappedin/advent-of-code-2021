numbers = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
total = 0

for position, _ in enumerate(numbers):
#for position in numbers:

    if numbers[position] > numbers[position - 1]:
        total = total + 1
    else: next

print(total) 
