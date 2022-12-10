from readCSV import readCSV
import Map
import Agent
import time



def main():
    trailMap = readCSV('maps/TrailMap - 5x5.csv')
    elevationMap = readCSV('maps/ElevationMap - 5x5.csv')

    map = Map.Map(elevationMap, trailMap)
    map.printTrailMap()
    map.printElevationMap()
    map.printQTable()
    map.printPolicy()

    startTime= time.time()
    rewardList = []
    totalMovesList = []

    while time.time() - startTime < 60:
        agent = Agent.Agent(map)
        agent.setTransitionModel('On', 'Low')

        while not agent.goalReached():

            location1 = agent.location

            location2 = agent.findNextLocation(location1)
            agent.takeMove(location2)

            location3 = agent.findNextLocation(location2)
            #print(location1, location2, location3)
            agent.updateQTable(location1,location2, location3)

        rewardList.append(agent.totalReward)
        totalMovesList.append(agent.moveCount)

        #map.printQTable()

    map.printQTable()
    map.updatePolicyMap()
    map.printPolicy()

    print(totalMovesList)
    print(rewardList)

    print(map.returnTrail())




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
