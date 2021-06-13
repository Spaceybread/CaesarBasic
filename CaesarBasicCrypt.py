set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i' , 'j', 'k' , 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word = []
op = ''
edNumber = 0

def join(w):
    n = ""
    for l in w:
        n += l
    return n

key = int(input('key: '))

if key > 25:
    print('Key must be less than 26')
    quit(0)
elif key < -25:
    print('Key must be greater than -26')
    quit(0)

ed = int(input('encode(0) or decode(1): '))
if ed == 0:
    edNumber = 1
else:
    edNumber = -1

letter = input('sentence: ')

for i in letter:
    if i == ' ':
        newLetter = ' '
    else:
        letterNumber = set.index(i)
        newLoc = letterNumber + (key * edNumber)

        if newLoc >= 0 and newLoc < 25:
            newLetter = set[newLoc]
        elif newLoc > 25:
            newLoc = newLoc - 26
            newLetter = set[newLoc]
        else:
            newLoc = 26 + newLoc
            newLetter = set[newLoc]

    word.append(newLetter)

print(join(word))
