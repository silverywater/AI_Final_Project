from readCSV import readCSV
import Map
import Agent
import time



def main():
    trailMap = readCSV('TrailMap.csv')
    elevationMap = readCSV('ElevationMap.csv')

    map = Map.Map(elevationMap, trailMap)
    map.printTrailMap()
    map.printElevationMap()
    map.printQTable()
    map.printPolicy()

    startTime= time.time()

    while time.time() - startTime < 10:
        agent = Agent.Agent(map)
        agent.setTransitionModel('On', 'Low')

        while not agent.goalReached():

            location1 = agent.location

            location2 = agent.findNextLocation(location1)
            agent.takeMove(location2)

            location3 = agent.findNextLocation(location2)
            #print(location1, location2, location3)
            agent.updateQTable(location1,location2, location3)

        map.printQTable()

    map.printQTable()
    map.updatePolicyMap()
    map.printPolicy()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
