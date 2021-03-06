from Process import Process
from Node import Node
import random


def hardCodedProcesses():
    p1 = Process(1, 0, 24, 0)
    p2 = Process(2, 0, 27, 0)
    p3 = Process(3, 10, 40, 0)
    p4 = Process(4, 0, 14, 0)
    p5 = Process(5, 0, 25, 0)
    p6 = Process(6, 4, 18, 0)
    p7 = Process(7, 0, 17, 0)
    p8 = Process(8, 15, 32, 0)
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

def RandomProcesses(count):
    processList = []
    latestArrival = 5
    longestBurst = 50
    lowestPriority = 10

    for i in range(1,count):
        p = Process(i,random.randint(0,latestArrival),random.randint(1,longestBurst),random.randint(1,lowestPriority))
        processList.append(p)

    return processList

def nodeCreation(numOfNodes):
    nodeArray = []
    for i in range(1,numOfNodes):
        n = Node(i,random.randint(0,2),random.randint(30,50))
        nodeArray.append(n)
    return nodeArray


def centralQueueAlgorithm(listOfProcesses, arrayOfNodes):
    # sort processes by arrival time
    tempProcess = None
    for i in range(0, len(listOfProcesses)):
        for j in range(i + 1, len(listOfProcesses)):
            if listOfProcesses[i].get_ArrivalTime() > listOfProcesses[j].get_ArrivalTime():
                tempProcess = listOfProcesses[i];
                listOfProcesses[i] = listOfProcesses[j]
                listOfProcesses[j] = tempProcess

    numOfNodes = len(arrayOfNodes)
    totalElapsedTime = 0;
    globalQueue = []
    requestQueue = []

    exitMainLoop = True

    # main loop that acts as clock
    while True:
        exitMainLoop = True

        # if more processes are still coming in, dont stop the main loop
        if len(listOfProcesses) != 0:
            exitMainLoop = False

        # schedule global queue with FCFS
        while True:
            if len(listOfProcesses) != 0:
                pToAddToGlobal = listOfProcesses[0]
                if pToAddToGlobal.arrivalTime == totalElapsedTime:
                    globalQueue.append(listOfProcesses.pop(0))
                else:
                    break
            else:
                break

        # if processes are still in global queue, don't stop main loop
        if len(globalQueue) != 0:
            exitMainLoop = False

        # first check if there are any pending process requests from nodes in the system
        while len(requestQueue) != 0:
            # check globalQueue not empty
            if len(globalQueue) != 0:
                pToAddToNodeQueue = globalQueue.pop(0)
                nodeToAddProcessTo = requestQueue.pop(0)
                nodeToAddProcessTo.addProcessToQueue(pToAddToNodeQueue)
                print(
                    "Process #: " + pToAddToNodeQueue.get_Pid() + " moved from global queue to local queue of node #: " + nodeToAddProcessTo.nodeNum,"current time:", totalElapsedTime )
            else:
                break

        # for all nodes
        for node in arrayOfNodes:
            # if nodes are still running something, don't stop main loop
            if exitMainLoop:
                if not node.isQueueEmpty():
                    exitMainLoop = False
                else:
                    if node.runningProcessRemainingTime != 0:
                        exitMainLoop = False

            # make sure processes on the node's local queue are scheduled in right order
            node.schedule()

            # advances processes on node
            node.advanceOnStep()

            # check if any node is underloaded. If it is, make it request a process from global queue
            while not node.isOverLoaded():
                if len(globalQueue) != 0:
                    print("Node #:", node.nodeNum, "has made a request for a process from global queue")
                    pToAddToNodeQueue = globalQueue.pop(0)
                    node.addProcessToQueue(pToAddToNodeQueue)
                    print(
                        "Process #:", pToAddToNodeQueue.get_Pid(), "moved from global queue to local queue of node #:",node.nodeNum, "current time:", totalElapsedTime )
                else:
                    # if global queue is empty, add node request to queue after checking if a request was already made
                    if node not in requestQueue:
                        print("Node #:", node.nodeNum, "has made a request for a process from global queue")
                        requestQueue.append(node)
                        print(
                            "Node #:", node.nodeNum, "'s request for a process cannot be fulfilled as the global queue is empty. Request added to request queue.","current time:", totalElapsedTime )

        # check if all processing is done, or the clock needs to keep going
        if exitMainLoop:
            break
        else:
            totalElapsedTime += 1


def main():
    # create some hard coded processes.
    
    #listOfProcesses = hardCodedProcesses()
    listOfProcesses = RandomProcesses(100)

    # decide how many nodes to create and return an array of them ( can randomize the parameter here)
    arrayOfNodes = nodeCreation(2)

    # do central queue algo
    centralQueueAlgorithm(listOfProcesses, arrayOfNodes)


# call the main function if it exists
if __name__ == '__main__':
    main()
