from Process import Process


class Node:
    def __init__(self, nodeNum, algoChoice, overLoadedThreshold):
        self.localQueue = []
        self.runningProcessRemainingTime = 0
        self.totalRunningTime = 0
        self.idleTime = 0
        self.algoChoice = algoChoice
        self.overLoadedThreshold = overLoadedThreshold
        self.currentRunningProcessId = None
        self.nodeNum = nodeNum

    def addProcessToQueue(self, process):
        self.localQueue.append(process)

    def nextProcessInQueue(self):
        process = self.localQueue.pop(0)
        self.currentRunningProcessId = process.get_Pid()
        self.runningProcessRemainingTime = process.get_RemainBurstTime()

    def schedule(self):
        # FCFS, no process scheduling/sorting needs to be done
        if self.algoChoice == 0:
            pass
        # SJF, sort processes in queue by shortest burst time
        elif self.algoChoice == 1:
            for i in range(0, len(self.localQueue)):
                for j in range(i + 1, len(self.localQueue)):
                    if self.localQueue[i].get_BurstTime > self.localQueue[j].get_BurstTime:
                        tempProcess = self.localQueue[i];
                        self.localQueue[i] = self.localQueue[j]
                        self.localQueue[j] = tempProcess
        # priority, sort processes in queue by highest # priority first
        elif self.algoChoice == 2:
            for i in range(0, len(self.localQueue)):
                for j in range(i + 1, len(self.localQueue)):
                    if self.localQueue[i].get_Priority < self.localQueue[j].get_Priority:
                        tempProcess = self.localQueue[i];
                        self.localQueue[i] = self.localQueue[j]
                        self.localQueue[j] = tempProcess

    # might need some changes.
    def advanceOnStep(self):
        if self.runningProcessRemainingTime == 0:
            print("Finished Process #: "+self.currentRunningProcessId+" on node#: "+self.nodeNum)
            if self.isQueueEmpty():
                self.idleTime += 1
                self.totalRunningTime += 1
            else:
                self.nextProcessInQueue()
                self.totalRunningTime += 1
                self.runningProcessRemainingTime -= 1
        else:
            self.totalRunningTime += 1
            self.runningProcessRemainingTime -= 1

    def isQueueEmpty(self):
        if len(self.localQueue) == 0:
            return True
        else:
            return False

    def isOverLoaded(self):
        if self.overLoadedThreshold > self.getTotalBurstTime():
            return False
        else:
            return True

    def getTotalBurstTime(self):
        load = 0
        for i in self.localQueue:
            load += i.get_BurstTime()
        load += self.runningProcessRemainingTime
