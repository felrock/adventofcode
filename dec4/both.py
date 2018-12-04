from datetime import datetime

def isAsleep(falls, wakes, time):
    ''' Determine if time is between falls and wake
    '''

    if falls[0] == wakes[0]:

        if time[1] >= falls[1] and time[1] <= wakes[1]:
            return True
        else:
            return False

    else:

        if time[0] == falls[0] and time[1] >= falls[1]:
            return True
        elif time[0] == wakes[0] and time[1] <= wakes[1]:
            return True
        else:
            return False




def CalcSleepTime(falls, wakes):
    ''' Return the differnce in time between falls and wake
        in minutes and the fall/wake tuples
    '''

    fall_h, fall_m = int(falls[0:2]), int(falls[3:5])
    wake_h, wake_m = int(wakes[0:2]), int(wakes[3:5])
    result = 0

    if wake_h == 0 and fall_h == 0:
        result = wake_m - fall_m
    elif wake_h == 0 and fall_h == 23:
        result = wake_m + ( 60 - fall_m)
    else:
        result = (60-wake_m) - (60-fall_m)

    return result, (fall_h, fall_m), (wake_h, wake_m)


with open('input.txt', 'r') as f:

    lines = []
    dd = {}
    guards = {}

    for line in f:
        lines.append(line)

        #add guards
        if '#' in line:

            gnr = line.split('#')[-1].split(' b')[0]

            if gnr not in guards:
                # Add a clean sleeping schedule for the new guard

                schedule = []
                for time1 in [23, 0]:
                    for time2  in range(60):
                        schedule.append([(time1,time2), 0])

                guards[gnr] = [0, schedule]

    # Sort the input acording to date and time
    lines.sort(key=lambda k: datetime.strptime(
                             k[1:17],
                             '%Y-%m-%d %H:%M'))

    # find total sleeping time for the guards
    falls = ''
    wakes = ''
    for line in lines:

        if '#' in line:
            # guard is switched

            gnr = line.split('#')[-1].split(' b')[0]

        elif 'falls' in line:
            # guard falls asleep

            falls = line[12:17]

        else:
            # guard wakes up

            wakes = line[12:17]
            time, ftuple, wtuple = CalcSleepTime(falls, wakes)
            guards[gnr][0] += time

            # Add the slept time to the sleeping schedule
            # in the dict 'guards'

            for schedule in guards[gnr][1]:

                if isAsleep(ftuple, wtuple, schedule[0]):
                    schedule[1] += 1

    # Find the guard that sleeps the most
    guards_lst = [(k,v) for k,v in guards.items()]
    ident, value = max(guards_lst, key=lambda x:x[1][0])

    # SEARCH FOR THE MOST SLEPT MINUTE

    timesasleep = 0
    freqmin = 0
    for schedule in guards[ident][1]:

        if schedule[1] > timesasleep:

            timesasleep = schedule[1]
            freqmin = schedule[0][1]

    print('Challenge 1 answer:', freqmin*int(ident))


    # SOLVE FOR SECOND CHALLENGE

    ident = ''
    maxmins = 0
    freqmin = 0

    for key, value in guards.items():

        for schedule in value[1]:
            if schedule[1] > maxmins:

                maxmins = schedule[1]
                freqmin = schedule[0][1]
                ident = key

    print('Challenge 2 answer:',freqmin*int(ident))















