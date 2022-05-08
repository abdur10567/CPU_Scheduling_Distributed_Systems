from Process import Process
from Node import Node

def hardCodedProcesses():
    p1 = Process(1, 0, 10, 0, None)
    p2 = Process(2, 0, 10, 0, None)
    p3 = Process(3, 10, 10, 0, None)
    p4 = Process(4, 0, 10, 0, None)
    p5 = Process(5, 0, 10, 0, None)
    p6 = Process(6, 4, 10, 0, None)
    p7 = Process(7, 0, 10, 0, None)
    p8 = Process(8, 15, 10, 0, None)
    processList = []
    processList.append(p1)
    processList.append(p2)
    processList.append(p3)
    processList.append(p4)
    processList.append(p5)
    processList.append(p6)
    processList.append(p7)
    processList.append(p8)
    return processList

def nodeCreation(numOfNodes):
    a = Node(0,50)
    b = Node(0,30)
    c = [a,b]
    return c



def localQueueAlgorithm(listOfProcesses,arrayOfNodes):
    #sort processes by arrival time
    tempProcess = None
    for i in range(0, len(listOfProcesses)):
        for j in range(i+1, len(listOfProcesses)):
            if(listOfProcesses[i].get_ArrivalTime()>listOfProcesses[j].get_ArrivalTime()):
                tempProcess = listOfProcesses[i];
                listOfProcesses[i] = listOfProcesses[j]
                listOfProcesses[j] = tempProcess

    numOfNodes = len(arrayOfNodes)
    totalElapsedTime = 0;
    globalQueue = []
    maximumPossibleBurstTime = 0
    for i in listOfProcesses:
        maximumPossibleBurstTime+=i.get_BurstTime()

    #flag for checking if global queue is empty
    globalQueueEmpty = False

    while(totalElapsedTime<=maximumPossibleBurstTime):
        exitLoop = True

        #schedule global queue with FCFS
        while True:
            if (len(listOfProcesses) != 0):
                pToAddToGlobal = listOfProcesses[0]
                if(pToAddToGlobal.arrivalTime==totalElapsedTime):
                    globalQueue.append(listOfProcesses.pop(0))
                else:
                    break
            else:
                break









def main():
    # create some hard coded processes.
    listOfProcesses = hardCodedProcesses()
    #decide how many nodes to create and return an array of them ( can randomize the parameter here)
    arrayOfNodes = nodeCreation(2)

    #do localQueue algo
    localQueueAlgorithm(listOfProcesses,arrayOfNodes)


# call the main function if it exists
if __name__ == '__main__':
    main()
