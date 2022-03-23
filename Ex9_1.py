dwords = dict()
fhand = open("words.txt")

for line in fhand :
    words = line.split()
    for word in words :
        dwords[word] = dwords.get (words, 0) + 1

if "bubbles" in dwords :
    print ("True")
else:
    print("False")
