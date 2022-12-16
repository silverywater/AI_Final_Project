import numpy as np
import time

class Map:
    def __init__(self, elevationMap, trailMap):
        self.elevationMap = elevationMap
        self.trailMap = trailMap

        self.rows = len(trailMap)
        self.columns = len(trailMap[0])

        # generate Q table and policy map
        self.qTable = []
        self.policyMap = []
        for i in range(len(self.trailMap)):
            rowQTable = []
            rowPolicy = []
            for j in range(len(self.trailMap[i])):
                if self.trailMap[i][j] != "X":

                    #record starting position and goal
                    if self.trailMap[i][j] == "S":
                        self.startPoint = [i, j]
                        rowQTable.append([0.0, 0.0, 0.0, 0.0])
                        rowPolicy.append('?')
                        self.trailMap[i][j] = 1
                    elif self.trailMap[i][j] == "G":
                        rowQTable.append('G')
                        rowPolicy.append('G')
                        self.goal = [i, j]
                    else:
                        rowQTable.append([0.0, 0.0, 0.0, 0.0])
                        rowPolicy.append('?')


                else:
                    rowQTable.append('X')
                    rowPolicy.append('X')
            self.qTable.append(rowQTable)
            self.policyMap.append(rowPolicy)



    #update policy at the end: [L<, R>, U^, Dv]
    def updatePolicyMap(self):
        for i in range(len(self.qTable)):
            for j in range(len(self.qTable[i])):
                if self.qTable[i][j] != 'X' and self.qTable[i][j] != 'G':
                    direction = np.argmax(self.qTable[i][j])
                    maximum = min(self.qTable[i][j])
                    if max(self.qTable[i][j]) == 0:
                        for k in range(len(self.qTable[i][j])):
                            if self.qTable[i][j][k] >= maximum and self.qTable[i][j][k] != 0:
                                maximum = self.qTable[i][j][k]
                                direction = k

                    if self.qTable[i][j][direction] == 0:
                        self.policyMap[i][j] = '?'
                    elif direction == 0:
                        self.policyMap[i][j] = '<'
                    elif direction == 1:
                        self.policyMap[i][j] = '>'
                    elif direction == 2:
                        self.policyMap[i][j] = '^'
                    elif direction == 3:
                        self.policyMap[i][j] = 'v'
        return


    #print Maps
    def printElevationMap(self):
        for row in self.elevationMap:
            print(row)

    def printTrailMap(self):
        for row in self.trailMap:
            print(row)

    def printPolicy(self):
        for row in self.policyMap:
            print(row)

    def printQTable(self):
        for row in self.qTable:
            print(row)


    def returnTrail(self):
        steps = []
        location = self.startPoint

        startTime = time.time()

        while True and time.time() - startTime < 10:
            x = location[0]
            y = location[1]
            step = [x, y, self.elevationMap[x][y], self.trailMap[x][y]]
            if step in steps:
                print("Agent got stuck")
                return
            steps.append(step)
            if self.trailMap[x][y] == 'G':
                break

            direction = np.argmax(self.qTable[x][y])
            maximum = min(self.qTable[x][y])
            if max(self.qTable[x][y]) == 0:
                for k in range(len(self.qTable[x][y])):
                    if self.qTable[x][y][k] >= maximum and self.qTable[x][y][k] != 0:
                        maximum = self.qTable[x][y][k]
                        direction = k

            if direction == 0:
                location = [x, y - 1]

            elif direction == 1:
                location = [x, y + 1]

            elif direction == 2:
                location = [x - 1, y]
            elif direction == 3:
                location = [x + 1, y]

        return steps

    def setGoal(self, newGoal):
        self.trailMap[self.goal[0]][self.goal[1]] = 1
        self.qTable[self.goal[0]][self.goal[1]] = [0.0, 0.0, 0.0, 0.0]
        self.policyMap[self.goal[0]][self.goal[1]]= '?'


        self.trailMap[newGoal[0]][newGoal[1]] = 'G'
        self.qTable[newGoal[0]][newGoal[1]] = 'G'
        self.policyMap[newGoal[0]][newGoal[1]] = 'G'
