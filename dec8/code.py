import sys
import copy


# part one
def mm(entries):

    total = 0
    children, meta = entries[:2]
    del entries[:2]

    if children == 0:

        s = sum(entries[:meta])
        del entries[:meta]

        return s

    else:
        for _ in range(children):

            total += mm(entries)

        total += sum(entries[:meta])
        del entries[:meta]


    return total

# part two
def rootScore(entries):

    score = 0
    scores = []
    children, meta = entries[:2]
    del entries[:2]

    if children == 0:
        s = sum(entries[:meta])
        del entries[:meta]

        return s
    else:

        for _ in range(children):

            scores.append(rootScore(entries))

        # Get the references for the root score
        references = entries[:meta]
        del entries[:meta]

        for ref in references:

            # -1 since 1 is first ref not 0
            if ref-1 < len(scores):
                score += scores[ref-1]

        return score


with open('input.txt', 'r') as f:

    entries = list(map(int, f.readline().rstrip().split(' ')))
    entries2 = copy.deepcopy(entries)
    print('Challenge 1:', mm(entries))
    print('Challenge 2:', rootScore(entries2))
