import numpy as np

class Agent:
    def __init__(self, map):
        self.map = map
        self.location = map.startPoint

        self.learningRate = 0.9
        self.gamma = 0.1

        #transition model if no user inputs given
        self.probOn = 0.5
        self.probOff = 0.5

        self.prob2m = 0.45
        self.prob5m = 0.45
        self.prob10m = 0.1


    def findPossibleMoves(self, location):
        moves = []
        x = location[0]
        y = location[1]

        #left
        if (y > 0 and self.map.trailMap[x][y-1] != 'X'):
            moves.append([x, y-1, 0])
        #rigth
        if (y < (self.map.columns - 1) and self.map.trailMap[x][y+1] != 'X'):
            moves.append([x, y+1, 1])

        # up
        if (x > 0 and self.map.trailMap[x - 1][y] != 'X'):
            moves.append([x - 1, y, 2])
        # down
        if (x < (self.map.rows - 1) and self.map.trailMap[x + 1][y] != 'X'):
            moves.append([x + 1, y, 3])

        return moves

    def setTransitionModel(self, trailType, elevationDifficulty):
        #trail type
        if trailType == 'On':
            self.probOn = 0.9
            self.probOff = 0.1
        elif trailType == 'Off':
            self.probOn = 0.1
            self.probOff = 0.9
        elif trailType == "Hybrid":
            self.probOn = 0.7
            self.probOff = 0.3

        #elevation difficulty
        if elevationDifficulty == 'Low':
            self.prob2m = 0.8
            self.prob5m = 0.1
            self.prob10m = 0.1
        elif elevationDifficulty == 'Medium':
            self.prob2m = 0.6
            self.prob5m = 0.3
            self.prob10m = 0.1
        elif elevationDifficulty == 'High':
            self.prob2m = 0.4
            self.prob5m = 0.35
            self.prob10m = 0.25
        return

    def findNextLocation(self,location):
        moves = self.findPossibleMoves(location)
        probabilities = []
        currentElevation = self.map.elevationMap[location[0]][location[1]]
        for row in moves:
            if self.map.trailMap[row[0]][row[1]] == 0:
                prob1 = self.probOff
            elif self.map.trailMap[row[0]][row[1]] == 1:
                prob1 = self.probOn
            elif self.map.trailMap[row[0]][row[1]] == 'G':
                prob1 = 0.9


            if abs(self.map.elevationMap[row[0]][row[1]] - currentElevation) <= 2:
                prob2 = self.prob2m
            elif abs(self.map.elevationMap[row[0]][row[1]] - currentElevation) <= 5:
                prob2 = self.prob5m
            else:
                prob2 = self.prob10m

            probabilities.append(prob1*prob2)

        norm = [float(i) / sum(probabilities) for i in probabilities]
        index = np.random.choice(len(moves),p=norm)

        return moves[index]

    def takeMove(self, nextLocation):
        self.location = nextLocation[:2]

    def updateQTable(self, previousLocation, currentLocation, nextLocation):
        prev = previousLocation[:2]
        current = currentLocation[:2]

        nextIndex = nextLocation[2]
        if self.map.qTable[current[0]][current[1]] == 'G':
            nextQ = 10
        else:
            nextQ = self.map.qTable[current[0]][current[1]][nextIndex]

        index = currentLocation[2]
        prevQ = self.map.qTable[prev[0]][prev[1]][index]

        self.map.qTable[prev[0]][prev[1]][index] = round(
            prevQ + self.learningRate * (self.calculateReward() + self.gamma *nextQ - prevQ),
            2)



    def calculateReward(self):
        return 1


    def goalReached(self):
        return self.map.trailMap[self.location[0]][self.location[1]] == 'G'