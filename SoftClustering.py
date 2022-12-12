
import copy
import random


class SoftClustering:
    def __init__(self):
        self.points = []

        self.means = []

        self.pointsDist = []
        self.pointsProb = []

        self.changeInProbs = 100
        self.changeInMeans = 100
        
        
        pass

    def distance(self, point1, point2):

        #print("points ", point1, point2 )
        dist = 0
        index = 0
        for val in point1:
            dist += pow(point2[index] - point1[index], 2)
            
            index+=1
        #print("tmp ", dist)    
        dist = pow(dist, 0.5)
        #print("tmp2", dist)

        return dist
        pass

    def probOfPointInClusters(self, points, pointsDist, pointsProb, means):
        """"
        """
        newPointsDist = copy.deepcopy(pointsDist)
        newPointsProb = copy.deepcopy(pointsProb)
        
        indexP = 0
        for point in points:
            indexM = 0

            #print("dist ", newPointsDist)
            distSum = 0
            #set the distances from the means
            for mean in means:
                dist = self.distance(point, mean)
                #print("P, M : ", indexP, ", ", indexM)
                newPointsDist[indexP][indexM] = dist
                distSum += dist
                indexM += 1
            

            

            indexM = 0

            indexR = 0
            #set the probabilities
            for mean in means:
                #print(newPointsDist[indexP][indexR])
                # prob = newPointsDist[indexP][indexR] / distSum
                # print(prob)
                newPointsProb[indexP][indexR]  = newPointsDist[indexP][indexR] / distSum#prob
                #print( "tmp ", newPointsProb[indexP][indexR])
                indexR += 1


            #print("dist2 ", newPointsProb)
            indexP += 1

        self.changeInProbs = 0
        indexP = 0
        for point in points:
            indexM = 0
            for mean in means: 
                self.changeInProbs += abs(newPointsProb[indexP][indexM] - pointsProb[indexP][indexM])
                #print("change ", self.changeInProbs)
                indexM += 1
        
            indexP += 1

        self.pointsDist = copy.deepcopy(newPointsDist)
        self.pointsProb = copy.deepcopy(newPointsProb)

        pass

    def refitMeans(self):

        meansCopy = copy.deepcopy(self.means)
        newMeans = copy.deepcopy(self.means)
        indexM = 0

        for mean in meansCopy:
        #sum all xs and ys of the current mean, then average it out
            sums = [0] * len(mean)
            sumX = 0
            sumY = 0
            countOfPoints = 0

            indexP = 0
            for point in self.pointsProb:
                #if the point is most likely to belong to this mean then add xs and ys to sum
                if point[indexM] == max(point):
                    indexS = 0
                    for sum in sums:
                        sums[indexS] += self.points[indexP][indexS]
                        indexS +=1

                    # sumX += self.points[indexP][0]
                    # sumY += self.points[indexP][1]
                    countOfPoints += 1
                indexP += 1
            #print("Sums : ", sums)
            
            if countOfPoints > 0:
                indexS = 0
                for sum in sums:
                    newMeans[indexM][indexS] = sum / countOfPoints
                    indexS +=1
            else:
                    newMeans[indexM] = self.generateRandomMean()
            #print("New Mean ", newMeans[indexM])
            indexM += 1

        sumOld = 0
        sumNew = 0

        indexF = 0
        for mean in meansCopy:
            for v in mean:
                sumOld += v

        for mean in newMeans:
            for v in mean:
                sumNew += v
        
        self.changeInMeans = abs(sumOld - sumNew)


        #set new mean coordinates
        self.means = copy.deepcopy(newMeans)
        #

        pass

    def generateRandomMean(self):
        index1 = (int) (random.random() * len(self.points))

        index2 = (int) (random.random() * len(self.points))

        newMean = copy.deepcopy(self.points[index1])

        index = 0
        for var in newMean:
            newMean[index] = (self.points[index1][index] + self.points[index2][index]) / 2
            index+=1

        print("generated new mean : ", newMean)
        return newMean;
        pass

    def printData(self):
        print("\n\nData\n")
        print("Points : ", self.points)
        print("Dist", self.pointsDist)
        print("Probs : ", self.pointsProb)
        print("Change in probs : ", self.changeInProbs)
        print("Change in means : ", self.changeInMeans)
        print("Means : ", self.means)


    def runIteration(self):
        # print("\n\nProb Adjustment ")
        self.probOfPointInClusters(self.points, self.pointsDist, self.pointsProb, self.means) #here
        # self.printData()

        # print("\nMEANS REFIT")
        self.refitMeans()
        # self.printData()

        print("Change : ", self.changeInMeans)
        pass

    def setUp(self, input_points, numMeans):
        self.points = input_points


        #template - [ [0] * 4 for in range(3)   ]  creates a 3x4 array   3 rows, 4 columns
        # 2 points, 2 means                   
        #self.means = [[0, 0, 1],[0, 0, 0]]                    #num means(rows) by num variables per point(col)
        self.means = [[0] * len(self.points[0]) for i in range(numMeans)]

        indexM = 0
        for mean in self.means:
            self.means[indexM] = self.generateRandomMean()
            indexM +=1

        
        self.pointsDist = [[0] * len(self.means) for i in range(len(self.points))]
        self.pointsProb =  [[0] * len(self.means) for i in range(len(self.points))]      #num points(row) by num means(col) 


        pass

    def test(self):
        point1 = [-3,-3,-3, 1] 
        point2 = [2,2,1, 1]
        point3 = [1,2,1, 1]
        point4 = [5,5,5, 1]
        point5 = [5,6,4, 1]
        #print(self.distance(point1, point2))


        # # 5 points, 2 means
        input_points = [point1, point2, point3, point4, point5]   
        self.setUp(input_points, 3);                   

        countOfLilChange = 0

        iteration = 0


        while (countOfLilChange < 4 and iteration < 100):
            print("Iteration : ", iteration)
            self.runIteration()

            if self.changeInMeans < 1.0:
                countOfLilChange +=1
            else:
                countOfLilChange = 0
            iteration +=1
        self.printData()
     
        
        pass

def run():
    pass

SoftClustering().test()