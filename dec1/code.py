with open('input.txt', 'r') as f:
    current_freq = 0
    freq_dict = {}
    lines = []
    freq_dict[current_freq] = True
    found = False

    # Store lines for re-use
    for line in f:
        lines.append(line)

    while not found:

        for line in lines:

            change_in_freq = int(line)
            current_freq += change_in_freq

            if current_freq in freq_dict:
                found = True
                print('Seen before,', current_freq)
                break

            else:
                freq_dict[current_freq] = True
