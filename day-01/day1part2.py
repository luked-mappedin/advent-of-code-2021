
def read_integers(filename):
    with open(filename) as file:
        return [int(line.strip()) for line in file]
        
numbers = (read_integers("input"))

total = 0
posa = 0
posb = 0
posc = 0
lastpossum = 0

for position, _ in enumerate(numbers):
    
    # get the current position value plus the next two
    posa = numbers[position]
    try:
        posb = numbers[position + 1]
    except:
        continue

    try:
        posc = numbers[position + 2]
    except:
        continue

    # sum them
    possum = posa + posb + posc

    #compare them against the last possum
    if possum > lastpossum and lastpossum !=0: total = total + 1

    lastpossum = possum

print(total) 
