with open('input.txt', 'r') as f:

    trip_sum = 0
    pair_sum = 0
    for line in f:

        sumdict = {}
        for char in line:

            if char in sumdict:
                sumdict[char] += 1
            else:
                sumdict[char] = 1

        sumlist = [ v for k, v in sumdict.items() ]
        twos, threes = False, False

        for s in sumlist:

            if s == 2:
                twos = True

            elif s == 3:
                threes = True

        if threes:
            trip_sum += 1

        if twos:
            pair_sum += 1

    print(pair_sum, '*', trip_sum,'=', pair_sum*trip_sum)
