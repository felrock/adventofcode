def findPath( root, singles, steps, needs ):

    output = [root]
    pPaths = steps[root]

    while True:

        pPaths.sort()
        path = chr(255)

        for p in pPaths:
            if p in output:
                continue

            found = True
            for need in needs[p]:

                if need not in output:
                    found = False
                    break

            if found:
                path = p
                break

        if len(singles) > 0 and singles[0] < path:

            path = singles[0]
            pPaths.append(path)
            singles = singles[1:]

        if path != None and path in steps:

            output.append(path)
            pPaths.extend(steps[path])
            pPaths.remove(path)

        else:

            output.append(path)
            break

    return ''.join(output)

if __name__ == '__main__':

    lines = []
    with open('input.txt', 'r') as f:

        for line in f:
            lines.append(line)
        f.close()



    steps = {}
    needs = {}
    for line in lines:

        # index for input per line
        step    = line[5]
        waitfor = line[-13]

        if step in steps:
            steps[step].append(waitfor)

        else:
            steps[step] = [waitfor]

        if waitfor in needs:
            needs[waitfor].append(step)

        else:
            needs[waitfor] = [step]

    steps_list = [ [k,v] for k, v in steps.items()]
    steps_list.sort( key=lambda x:x[0] )

    singles = []
    for step in steps_list:
        if step[0] not in needs:
            singles.append(step[0])
    singles.sort()

    root = singles[0]
    singles = singles[1:]
    instructions = findPath( root, singles, steps, needs )

    # part two

    workers = []
    seconds = 0
    while len(instructions) > 0:

        if len(workers) =< 5:



