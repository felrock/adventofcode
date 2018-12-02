



with open('input.txt', 'r') as f:

    lines = [ line for line in f ]
    found = False


    for line1 in lines:
        if found:
            break
        for line2 in lines:

            if line1 != line2:
                t = 0
                for c1,c2 in zip(line1,line2):
                    if c1 != c2:
                        t += 1
                if t == 1:
                    found = True
                    for c1,c2 in zip(line1,line2):

                        if c1 == c2:
                            print(c1, end='')
