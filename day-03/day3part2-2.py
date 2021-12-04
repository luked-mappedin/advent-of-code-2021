import statistics
from statistics import mode

def read_input(filename):
    with open(filename) as file:
        return [line.strip() for line in file]

inputs = read_input("day-03/input")
example_inputs = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

#print(inputs)
#mod = ""

def get_mode(input, pos):
    newlist = []
    for x in input:
        newlist.append(x[pos])
    #mod = mode(newlist)
    if newlist.count("1") >= newlist.count("0"):
        mod = "1"
    else: mod = "0"
    return mod

def get_low_mode(input, pos):
    newlist = []
    for x in input:
        newlist.append(x[pos])
    #mod = mode(newlist)
    if newlist.count("1") < newlist.count("0"):
        low_mod = "1"
    else: low_mod = "0"
    return low_mod

def filter_list(mod, lst, pos):
    fltlst = []
    for x in lst:
        if x[pos] == mod:
            fltlst.append(x)
    return fltlst

def get_o2(list):
    newlist = list
    loop_index = 0
    while len(newlist) > 1:
        mod = get_mode(newlist, loop_index)
        newlist = filter_list(mod, newlist, loop_index)
        loop_index += 1
    return newlist[0]

def get_co(list):
    newlist = list
    loop_index = 0
    while len(newlist) > 1:
        low_mod = get_low_mode(newlist, loop_index)
        newlist = filter_list(low_mod, newlist, loop_index)
        loop_index += 1
    return newlist[0]

co = (int(get_o2(inputs), 2))

o2 = (int(get_co(inputs), 2))

total = co * o2

print(total)