import statistics
from statistics import mode

def read_input(filename):
    with open(filename) as file:
        return [line.strip() for line in file]

inputs = read_input("day-03/input")

example_inputs = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

co2 = []
o2 = []
total = 0
binlist1 = []
binlist2 = []
binlist3 = []
binlist4 = []
binlist5 = []
binlist6 = []
binlist7 = []
binlist8 = []
binlist9 = []
binlist10 = []
binlist11 = []
binlist12 = []
masterlist = [binlist1, binlist2, binlist3, binlist4, binlist5, binlist6, binlist7, binlist8, binlist9, binlist10, binlist11, binlist12]
counter = 0
def check_binary(number):
    if number == "1":
        return True
    return False

def filter_list(list, pos, mod):
    for x in list:
        if list[pos] == "1":
            newlist.append(x)
            return newlist
        elif list[pos] == "0":
            newlist.append(list)
            return newlist

def filter_o2(inputlist, newlist, target):
    for x in inputlist:
        if x == target:
            newlist.append(x)
            return newlist

for x in inputs:    
    binlist1.append(x[0])
    binlist2.append(x[1])
    binlist3.append(x[2])
    binlist4.append(x[3])
    binlist5.append(x[4])
    binlist6.append(x[5])
    binlist7.append(x[6])
    binlist8.append(x[7])
    binlist9.append(x[8])
    binlist10.append(x[9])
    binlist11.append(x[10])
    binlist12.append(x[11])
    
def oxygen(input):
    lst = input
    loop_index = 0
    while len(lst) > 1:
        lst = filter_list(lst, loop_index,  )
        loop_index += 1

def find_mode(list, pos):
    for x in list:
            

for pos ,y in enumerate(masterlist):    
    if mode(y) == "1":
        for x in inputs:
            o2 = filter_list(inputs, pos, o2)
    else:
        for x in inputs:
            co2 = filter_list(inputs, pos, co2)

print(co2)
print(o2)

#print(total)

