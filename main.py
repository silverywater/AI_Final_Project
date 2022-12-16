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

    print('User Input: ')
    print(input_array)
    print()



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

    fileTrailMap = 'maps/TrailMap - 10x10 - 1.csv'
    fileElevationMap = 'maps/ElevationMap - 10x10 - 1.csv'

    trailMap = readCSV(fileTrailMap)
    elevationMap = readCSV(fileElevationMap)

    map = Map.Map(elevationMap, trailMap)
    if input_array[0] != input_array[1]:
        map.startPoint = input_array[0]
        map.setGoal(input_array[1])
    print('Existing Trails Map: ')
    map.printTrailMap()
    print()

    print('Elevation Map')
    map.printElevationMap()
    print()
    #map.printQTable()
    #map.printPolicy()

    startTime= time.time()
    rewardList = []
    totalMovesList = []
    timeList=[]
    learningRate = 0.1
    #On = 0.3,  Off=0.6, Hybrid =0.45
    gamma = 1

    file = open('reward.csv', 'w')
    csvFile = csv.writer(file)

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

        csvFile.writerow([time.time()-startTime,agent.totalReward,agent.moveCount])
        rewardList.append(agent.totalReward)
        totalMovesList.append(agent.moveCount)
        timeList.append(time.time()-startTime)


    print('Final Q Table')
    map.printQTable()
    print()

    map.updatePolicyMap()
    print('Final Policy Map')
    map.printPolicy()
    print()

    #print(totalMovesList)
    #print(rewardList)
    #print(timeList)


    file = open('output.csv','a')
    csvFile = csv.writer(file)

    if map.returnTrail():
        csvFile.writerow([fileTrailMap, agent.trailType, agent.elevationDifficulty, calc_run_metrics(map.returnTrail())])
    else:
        csvFile.writerow([fileTrailMap, agent.trailType, agent.elevationDifficulty])

    print('Suggested Trail:')
    print(map.returnTrail())
    print()

    print('Trail Metrics:')
    print(calc_run_metrics(map.returnTrail()))
    print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
