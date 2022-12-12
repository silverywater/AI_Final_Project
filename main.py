from readCSV import readCSV
import Map
import Agent
import time
import csv
from MetricFunctions import calc_run_metrics
from FrontEnd import inputInterface



def main():
    input_array = [[0, 0], [0, 0], 0, 0, 0]
    inputInterface(input_array)

    if input_array[2] == 1:
        trailType = 'On'
    elif input_array[2] == 2:
        trailType = 'Off'
    elif input_array[2] == 3:
        trailType = 'Hybrid'

    if input_array[3] == 1:
        elevationDifficulty = 'Low'
    elif input_array[3] == 2:
        elevationDifficulty = 'Medium'
    elif input_array[3] == 3:
        elevationDifficulty = 'High'

    fileTrailMap = 'maps/TrailMap - 5x5.csv'
    fileElevationMap = 'maps/ElevationMap - 5x5.csv'

    trailMap = readCSV(fileTrailMap)
    elevationMap = readCSV(fileElevationMap)

    map = Map.Map(elevationMap, trailMap)
    map.printTrailMap()
    map.printElevationMap()
    map.printQTable()
    map.printPolicy()

    startTime= time.time()
    rewardList = []
    totalMovesList = []
    timeList=[]
    learningRate = 0.9
    #On = 0.3,  Off=0.6, Hybrid =0.45
    gamma = 0.6

    while time.time() - startTime < 30:
        agent = Agent.Agent(map, learningRate, gamma)
        agent.setTransitionModel(trailType, elevationDifficulty)

        while not agent.goalReached():

            location1 = agent.location

            location2 = agent.findNextLocation(location1)
            agent.takeMove(location2)

            location3 = agent.findNextLocation(location2)
            #print(location1, location2, location3)
            agent.updateQTable(location1,location2, location3)

        rewardList.append(agent.totalReward)
        totalMovesList.append(agent.moveCount)
        timeList.append(time.time()-startTime)

        learningRate*=0.995
        #gamma *=0.9995

        #map.printQTable()

    map.printQTable()
    map.updatePolicyMap()
    map.printPolicy()

    #print(totalMovesList)
    #print(rewardList)
    #print(timeList)

    print(learningRate)

    file = open('output.csv','a')
    csvFile = csv.writer(file)

    if map.returnTrail():
        csvFile.writerow([fileTrailMap, agent.trailType, agent.elevationDifficulty, calc_run_metrics(map.returnTrail())])
    else:
        csvFile.writerow([fileTrailMap, agent.trailType, agent.elevationDifficulty])

    print(map.returnTrail())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
