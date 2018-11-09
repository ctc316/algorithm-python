class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Event:
    def __init__(self, eid, loc, tickets):
        self.eid = eid
        self.loc = loc
        self.tickets = sorted(tickets)


class Buyer:
    def __init__(self, bid, loc):
        self.bid = bid
        self.loc = loc


# The following method get the manhatten distance betwen two points (x1,y1) and (x2,y2)
def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


# Enter your code here. Read input from STDIN. Print output to STDOUT
sizeOfWorld = int(input())

numberOfEvents = int(input())
event_list = [None for _ in range(numberOfEvents)]
for i in range(numberOfEvents) :
    eventLine = input()
    # TODO: you will need to parse and store the events
    evt = eventLine.strip().split(" ")
    event_list[i] = Event(evt[0], \
                          Location(int(evt[1]), int(evt[2])), \
                          [int(evt[i]) for i in range(3, len(evt))])


numberOfBuyers = int(input())
buyer_list = [None for _ in range(numberOfBuyers)]
for i in range(numberOfBuyers):
    buyerLine = input()
    # TODO: you will need to parse and store the buyers
    buyer = buyerLine.strip().split(" ")
    buyer_list[i] = Buyer(i, Location(int(buyer[0]), int(buyer[1])))


# The solution to the first sample above would be to output the following to console:
# (Obviously, your solution will need to figure out the output and not just hard code it)
# print("2 50")
for buyer in buyer_list:
    chosed_idx = None
    min_dist = 2^32 - 1
    for i, evt in enumerate(event_list):
        if len(evt.tickets) == 0:
            continue

        distance = manhattan_distance(buyer.loc.x, buyer.loc.y, evt.loc.x, evt.loc.y)
        if distance < min_dist:
            chosed_idx = i
            min_dist = distance
        elif distance == min_dist:
            chosed_evt = event_list[chosed_idx]
            if evt.tickets[0] < chosed_evt.tickets[0] or \
               evt.tickets[0] == chosed_evt.tickets[0] and evt.eid < chosed_evt.eid:
                chosed_idx = i
                min_dist = distance

    if chosed_idx is None:
        print(-1, 0)
    else:
        print(event_list[chosed_idx].eid, event_list[chosed_idx].tickets.pop(0))