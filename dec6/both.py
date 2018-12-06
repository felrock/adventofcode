def getRegionWithinDist(dist, coords):
    '''
    Gets the size of the area that is atleast dist away from
    all nodes.
    '''
    area = 0

    for i in range(len(grid)):

        for j in range(len(grid[0])):

            # returns list with distances
            td = getDistToNodes(coords, (j,i))
            td = [t[0] for t in td]

            if sum(td) <= dist:
                area+=1

    return area

def getDistToNodes(coords, location):
    '''
    Returns the distance between a point and all
    points in the grid
    '''

    dist = []
    for coord in coords:

        x1, y1 = location[0], location[1]
        x2, y2 = coord[0][0], coord[0][1]
        d = abs(x1 - x2) + abs(y1 - y2)
        dist.append((d, coord[1]))

    return dist

def isEnclosed(name, grid):
    '''
    Checks if that for any given node in grid its possible
    to make a step in any direction without going out of
    bounds
    '''

    # bounds
    ylb = 0
    xlb = 0
    yhb = len(grid)-1
    xhb = len(grid[0])-1

    for i in range(len(grid)):

        for j in range(len(grid[0])):

            if grid[i][j] == name:

                if i+1 > yhb or i-1 < ylb or j+1 > xhb or j-1 < xlb:

                    return False
    return True

def calcSize(name, grid):
    '''
    Calculates a the size of a area that name "owns"
    '''

    size = 0
    for i in range(len(grid)):

        for j in range(len(grid[0])):

            if grid[i][j] == name:
                size += 1
    return size

if __name__ == '__main__':
    lines = []

    # Read coordinates from file
    with open('input.txt', 'r') as f:
        for line in f:
            lines.append(line)
        f.close()

    # Get the bounds of the coord area
    xmax,ymax = 0,0
    coords = []
    name = 0
    for line in lines:

        x, y = map(int, line.rstrip().split(','))
        coords.append(((x,y), name))

        if x > xmax:
            xmax = x

        if y > ymax:
            ymax = y
        name += 1


    # Label all the positions in the grid
    grid = [ ['' for _ in range(xmax+1)] for _ in range(ymax+1) ]
    for i in range(ymax+1):

        for j in range(xmax+1):

            # dist contains a tuple list with name and distance
            dist = getDistToNodes(coords, (j,i))
            dist.sort(key=lambda x:x[0])

            if dist[0][0] == dist[1][0]:

                grid[i][j] = '.'

            else:

                grid[i][j] = dist[0][1]

    # Get the maximum area size that doesnt touch the array
    # boundries( is infinite )
    maxsize = 0
    maxcoord = None
    for coord in coords:

        if isEnclosed(coord[1], grid):

            size = calcSize(coord[1], grid)

            if size > maxsize:

                maxsize = size
                maxcoord = coord

    print('First answer:', maxsize)
    print('Second answer', getRegionWithinDist(10000, coords))

