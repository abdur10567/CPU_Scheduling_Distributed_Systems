class Process:
    def __init__(self, pid, arrivalTime, burstTime, priority, numThreadsRequired):
        self.pid = pid
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime
        self.priority = priority
        self.numThreadRequired = numThreadsRequired
        self.remainingBurstTime = burstTime
        self.waitTime = None
        self.turnAroundTime = None
        self.responseTime = None
        self.startTime = None
        self.finishTime = None
        self.finished = False

    def get_Pid(self):
        return self.pid

    def get_Priority(self):
        return self.priority

    def get_ArrivalTime(self):
        return self.arrivalTime

    def get_BurstTime(self):
        return self.burstTime

    def get_RemainBurstTime(self):
        return self.remainingBurstTime

    def get_StartTime(self):
        return self.startTime

    def get_FinishTime(self):
        return self.finishTime

    def get_TurnAroundTime(self):
        return self.turnAroundTime

    def get_ResponeTime(self):
        return self.responseTime

    def get_Proccesed(self):
        return self.finished

    def set_StartTime(self, a):
        self.startTime = a

    def set_FinishTime(self, a):
        self.finishTime = a

    def set_TurnAroundTIme(self, a):
        self.turnAroundTime = a

    def set_waitTime(self, a):
        self.waitTime = a

    def set_responeTime(self, a):
        self.responseTime = a

    def set_RemainingBurstTime(self, a):
        self.remainingBurstTime = a

    def set_Finished(self, a):
        self.finished = a
