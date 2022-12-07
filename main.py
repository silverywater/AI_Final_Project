from readCSV import readCSV
import Map



def main():
    trailMap = readCSV('TrailMap.csv')
    elevationMap = readCSV('ElevationMap.csv')

    map = Map.Map(elevationMap, trailMap)
    map.printPolicy()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
