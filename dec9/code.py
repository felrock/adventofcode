import sys
from collections import deque

class LinkedListNode( object ):

    def __init__(self, value=None, nxt=None):
        self.value = value
        self.nxt = nxt

class LinkedList( object ):

    def __init__(self):

        self.size = 0
        self.root = None

    def insert(self, value, index):

        i = 0
        node = self.root

        while index-1 > i:
            node = node.nxt
            i+= 1
        node.nxt = LinkedListNode(value, node.nxt)
        self.size += 1

    def remove(self, index):

        i=0
        node = self.root

        while index-1 > i:
            node = node.nxt
            i+= 1

        rmnode = node.nxt
        node.nxt = node.nxt.nxt
        self.size -= 1

        return rmnode.value

    def max(self):

        node = self.root
        m = 0
        while node.nxt != None:

            if node.nxt.value > m:
                m = node.nxt.value
            node = node.nxt

        return m

    def printList(self):
        node = self.root
        while node != None:
            print(node.value, end=' ')
            node = node.nxt
        print()

def marbleGame(players, lastmarble):

    circle = deque([0])
    playerscore = [ 0 for _ in range(players) ]
    playerindex = 0

    for marble in range(1, lastmarble+1):

        if marble % 23 == 0:

            # update circleindex and score
            circle.rotate(7)
            playerscore[playerindex] += marble
            playerscore[playerindex] += circle.pop()
            circle.rotate(-1)

        else:

            # add new marble
            circle.rotate(-1)
            circle.append(marble)

        playerindex = (playerindex + 1) % players

    return max(playerscore)

def fasterMarbleGame(players, lastmarble):

    ll = LinkedList()
    ll.root = LinkedListNode(0)
    pos = 1
    player = [0 for _ in range(players)]
    playerindex = 0

    for marble in range(1, lastmarble+1):

        if marble % 23 == 0:

            pos = (pos-7)%ll.size
            mrb = ll.remove(pos)
            player[playerindex] += marble + mrb
            ll.printList()
            sys.exit()
        else:

            ll.insert(marble, pos)
            pos = (pos+1)%(ll.size)
            ll.printList()

        playerindex = (playerindex + 1)%players

    return ll.max()

with open('input.txt', 'r') as f:

    line = f.readline().rstrip()
    players = int(line.split(' p')[0])
    lastmarble = int(line.split('h ')[-1].split(' p')[0])
    f.close()

#print('Challenge 1:', fasterMarbleGame(players, lastmarble))
#print('Challenge 2:', fasterMarbleGame(players, lastmarble))

print('Challenge 1:', marbleGame(players, lastmarble))
print('Challenge 2:', marbleGame(players, lastmarble*100))
