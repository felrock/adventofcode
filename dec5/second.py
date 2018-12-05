with open('input.txt', 'r') as f:
    line = f.readline()
    line = line.replace('\n', '')
    saveline = ''
    polymers = [ chr(65+i)+chr(97+i) for i in range(26) ]
    polymers += [ chr(97+i)+chr(65+i) for i in range(26) ]
    minsize = len(line)
    for i in range(26):

        tline = line.replace(chr(65+i), '')
        tline = tline.replace(chr(97+i), '')

        while tline != saveline:
            saveline = tline

            for p in polymers:
                tline = tline.replace(p, '')

        if len(tline) < minsize:
            minsize = len(tline)

    print('Challenge 1: ',minsize)

