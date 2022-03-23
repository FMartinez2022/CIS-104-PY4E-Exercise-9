ddays = dict()
fname = input('Enter File Name: ')
try:
    fhand = open(fname)
except FileNotFoundError :
    print("File not found")
    exit()

for line in fhand :
    words = line.split()
    if len(words) < 3 or words [0] != "From" :
        continue
    else :
        if words[2] not in ddays :
            ddays[words[2]] = 1
        else:
            ddays[words[2]] += 1
print (ddays)
