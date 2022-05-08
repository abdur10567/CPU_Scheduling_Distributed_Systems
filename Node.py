from Process import Process
class Node:
    def __init__(self, algoChoice, overLoadedThreshold):
        self.localQueue = []
        self.runningProcessRemainingTime = 0
        self.totalRunningTime = 0
        self.idleTime = 0
        self.algoChoice = algoChoice
        self.overLoadedThreshold = overLoadedThreshold

    def addProcessToQueue(self, process):
        self.localQueue.append(process)

    def nextProcessInQueue(self):
        process = self.localQueue.pop(0)
        self.runningProcessRemainingTime = process.get_RemainBurstTime()

    def schedule(self):
        if self.algoChoice == 0:
            a = 2
        else:
            a = 1

    # might need some changes.
    def advanceOnStep(self):
        if self.runningProcessRemainingTime == 0:
            if self.isQueueEmpty():
                self.idleTime += 1
                self.totalRunningTime += 1
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
