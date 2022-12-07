import numpy as np

class Map:
    def __init__(self, elevationMap, trailMap):
        self.elevationMap = elevationMap
        self.trailMap = trailMap

        # generate Q table and policy map
        self.qTable = []
        self.policyMap = []
        for i in range(len(self.trailMap)):
            rowQTable = []
            rowPolicy = []
            for j in range(len(self.trailMap[i])):
                if self.trailMap[i][j] != "X":
                    rowQTable.append([0.0, 0.0, 0.0, 0.0])
                    rowPolicy.append('?')

                    #record starting position and goal
                    if self.trailMap[i][j] == "S":
                        self.startPoint = [i, j]
                    elif self.trailMap[i][j] == "G":
                        self.goal = [i, j]

                else:
                    rowQTable.append('X')
                    rowPolicy.append('X')
            self.qTable.append(rowQTable)
            self.policyMap.append(rowPolicy)



    #update policy at the end: [L<, R>, U^, Dv]
    def updatePolicyMap(self):
        for i in range(len(self.qTable)):
            for j in range(len(self.qTable[i])):
                if self.qTable[i][j] != 'X':
                    direction = np.argmax(self.qTable[i][j])
                    if direction == 0:
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

