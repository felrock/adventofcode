import sys
with open('input.txt', 'r') as f:
    line = f.readline()
    line = line.replace('\n', '')
    saveline = ''
    polymers = [ chr(65+i)+chr(97+i) for i in range(26) ]
    polymers += [ chr(97+i)+chr(65+i) for i in range(26) ]

    while line != saveline:
        saveline = line
        for p in polymers:
            line = line.replace(p, '')

    print('Challenge 1: ',len(line))

