with open('input.txt', 'r') as f:

    claims = []
    fabric = [ [0 for _ in range(1000)] for _ in range(1000) ]
    total = 0
    for claim in f:
        claims.append(claim)

    for claim in claims:

        sizeStr = claim.split(': ')[-1].split('x')
        sizeInt = (int(sizeStr[0]), int(sizeStr[1]))
        coordStr = claim.split('@ ')[-1].split(': ')[0].split(',')
        x, y = (int(coordStr[0]), int(coordStr[1]))

        for iy in range(y, y+sizeInt[1]):
            for ix in range(x, x+sizeInt[0]):
                   fabric[iy][ix] += 1
    for col in fabric:
        for item in col:
            if item >= 2:
                total += 1
    print(total)

