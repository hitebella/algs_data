# The airport has 2 runways to handle all takeoffs and landings.
# When a plane enters a holding queue (take off or landing), it is assigned an integer ID number.
# Use successive evenintegers for ID's of planes arriving at takeoff queues,
# and odd integers for landing queues. At each time, 0-3 planes may arrive at the
# takeoff queues and 0-3 planes may arrive at the landing queues.
import random


# a new plane takes off/lands every 10 minutes & two planes can do this at a time
class Clock:
    def __init__(self):
        self.hours = 12
        self.minutes = 0

    def getHours(self):
        return self.hours

    def getMinutes(self):
        return self.minutes

    def show(self):
        print("%d:%02d" % (self.hours, self.minutes))

    def getClockTime(self):
        return ((self.hours * 100) + self.minutes)

    def takeoff_landing(self):
        self.minutes += 5
        if self.minutes >= 60:
            self.minutes = 0
            self.hours += 1
        if self.hours >= 24:
            self.hours = 0


class Plane:
    def __init__(self, id, time):
        self.id = id
        self.time = time

    def getID(self):
        return self.id

    def getTime(self):
        return self.time

    def getAction(self):
        if self.id % 2 == 1:
            return "take off"
        else:
            return "land"


class HoldingQueue():
    def __init__(self):
        self.id = []
        self.time = []
        self.planeCount = 0

    def enqueue(self, plane, clock):
        print("Plane", plane.getID(), "is now waiting to", plane.getAction(), ". Current time:", clock.getClockTime())
        self.time.insert(0, clock.getClockTime())
        self.id.insert(0, plane)
        self.planeCount += 1

    def dequeue(self, clock):
        timeWaited = abs(clock.getClockTime() - self.time[1])
        if timeWaited == 50:
            timeWaited = 10
        print('Current time:', clock.getClockTime())
        print("Plane", self.peek().getID(), "is now going to", self.peek().getAction(), ". Time waited:", timeWaited)
        return self.id.pop()
        self.planeCount -= 1

    def peek(self):
        return self.id[-1]

    def clearQueue(self):
        self.id = []

    def get_all_IDs(self):
        return self.id


c = Clock()
# 120 hours of airport activity = 5 days
count = -1
runway = HoldingQueue()
#ensures only 0-3 planes take off at a time
request_chance = 1 / 3
print("the time is", c.getClockTime())
while count < 5:
    p1 = random.random()
    p2 = random.random()
    p3 = random.random()
    if (p1 < request_chance) & (len(runway.get_all_IDs()) < 3):
        p = Plane(random.randint(1, 2), c.getClockTime())
        runway.enqueue(p, c)
        c.takeoff_landing()
    if (p2 < request_chance) & (len(runway.get_all_IDs()) < 3):
        p = Plane(random.randint(1, 2), c.getClockTime())
        runway.enqueue(p, c)
        c.takeoff_landing()
    if (p3 < request_chance) & (len(runway.get_all_IDs()) < 3):
        p = Plane(random.randint(1, 2), c.getClockTime())
        runway.enqueue(p, c)
        c.takeoff_landing()
    if len(runway.get_all_IDs()) == 3:
        ran = random.randint(1,2)
        if ran == 1:
            c.takeoff_landing()
            runway.dequeue(c)
        if ran == 2:
            c.takeoff_landing()
            runway.dequeue(c)
            c.takeoff_landing()
            runway.dequeue(c)
    if c.getClockTime() == 1200:
        count += 1
