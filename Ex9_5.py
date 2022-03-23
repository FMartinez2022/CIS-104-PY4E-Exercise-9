domnames = dict()
fname = input('Enter File Name: ')
try :
    fhand = open(fname)
except FileNotFoundError :
    print("File not found")
    exit()

for line in fhand :
    words = line.split()
    if len(words) < 2 or words [0] != "From" :
        continue
    else :
        atpos = words[1].find('@')
        domain = words[1][atpos + 1:]
        if domain not in domnames :
            domnames[domain] = 1
        else:
            domnames[domain] += 1
print (domnames)
