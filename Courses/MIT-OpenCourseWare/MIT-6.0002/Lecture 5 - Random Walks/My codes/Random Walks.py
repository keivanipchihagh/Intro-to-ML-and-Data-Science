#Imports
import random

""" Deals with locations and its calculations """
class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getDistance(self, other):
        xDist = self.x - other.getX()
        yDist = self.y - other.getY()
        return (xDist ** 2 + yDist ** 2) ** 0.5
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

""" Drunk object """
class Drunk(object):
    def __init__(self, name = None):
        """Assumes name is a str"""
        self.name = name

    def __str__(self):
        if self != None:
            return self.name
        return 'Anonymous'

""" Usual drunk, walks randomly with no bias """
class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(stepChoices)

""" Dunk biased to walk towards north """
class WeiredDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0, 1.1), (0.0, -0.9), (0.0, 1.0), (0.0, -1.0)]
        return random.choice(stepChoices)

""" Map & some functionality """
class Field(object):
    def __init__(self):
        self.drunks = {}
    def addDrunk(self, drunk, location):
        if drunk in self.drunks:
            raise ValueError('Duplicate Drunk')
        else:
            self.drunks[Drunk] = location
    def getLocation(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk Not Found')
        else:
            return self.drunks[drunk]
    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk Not Found')
        else:
            xDist, yDist = drunk.takeStep()
            self.drunks[drunk] = self.drunks[drunk].move(xDist, yDist)

""" Makes a drunk walk in the field """
def walk(field, drunk, numOfSteps):
    start = field.getLocation(drunk)
    for step in range(numOfSteps):
        field.moveDrunk(drunk)
    return start.getDistance(field.getLocation(drunk))

""" Simulates a walk """
def simWalks(numSteps, numTrials, dClass):
    Homer = dClass('Homer')
    origin = Location(0, 0)
    distances = []
    for trial in range(numTrials):
        field = Field()
        field.addDrunk(Homer, origin)
        distances.append(round(walk(field, Homer, numTrials), 1))
    return distances

""" Tests a drunk """
def drunkTest(walkLengths, numTrials, dClass):    
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, 'random walk of', numSteps, 'steps')
        print(' Mean =', round(sum(distances)/len(distances), 4))
        print(' Max =', max(distances), 'Min =', min(distances))

""" Testing the sim """
random.seed(0)
drunkTest((10, 100, 1000, 10000), 100, UsualDrunk)
