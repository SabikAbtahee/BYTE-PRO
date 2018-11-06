from _sitebuiltins import _Printer
from operator import attrgetter

pidMain = []
arrivalTimeMain =[]
burstTimeMain = []

waitingTimeSJF=[]
turnAroundTimeSJF=[]


class Complection():
    def __init__(self,pid,arrivalTime,burstTime,completeTime,waitingTime,turnAroundTime):
        self.pid = pid
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime
        self.completeTime = completeTime
        self.waitingTime = waitingTime
        self.turnAroundTime = turnAroundTime

    def getPids(self):
        return self.pid

    def getArrivalTime(self):
        return self.arrivalTime

    def getBurstTime(self):
        return self.burstTime

    def getCompleteTime(self):
        return self.completeTime

    def getWaitingTime(self):
        return self.waitingTime

    def getTurnAroundTime(self):
        return self.turnAroundTime

class ProcessSJf():
    def __init__(self,pid,arrivalTime,burstTime):
        self.pid =pid
        self.arrivalTime =arrivalTime
        self.burstTime = burstTime

    def getPids(self):
        return self.pid

    def getArrivalTime(self):
        return self.arrivalTime

    def getBurstTime(self):
        return self.burstTime


class ProcessRR():
    def __init__(self, pid, arrivalTime, burstTime):
        self.pid = pid
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime

    def getPids(self):
        return self.pid

    def getArrivalTime(self):
        return self.arrivalTime

    def getBurstTime(self):
        return self.burstTime

def skipLine(f):
    for i in range(6):
        f.readline()
    return f

def getTime(words):
    temp1 = words.split(':')
    time = temp1[1].split('.')
    # print(int(time[0])+1)
    return int(int(time[0])*60+int(time[1]))

def manipulateValue(words):
    pidMain.append(words[0])
    arrivalTimeMain.append(getTime(words[10]))
    burstTimeMain.append(int(words[5]))
def readFile():
    with open('C:/Users/Chinmoy/Desktop/TempFolder/top.txt') as f:
        skipLine(f)
        for i in range(9):
            manipulateValue(f.readline().split())


def separatePids():
    for i in range(len(burstTimeMain)):
        if(burstTimeMain[i]<=averageBurstTime):
            processSJF.append(ProcessSJf(pidMain[i],arrivalTimeMain[i],burstTimeMain[i]))
        else:
            processRR.append(ProcessRR(pidMain[i], arrivalTimeMain[i], burstTimeMain[i]))

def getMinimum(process):
    mini = 9999999999999999999999
    index =-1
    j =0
    for i in process:
        if(mini>=i.getArrivalTime()):
            mini = i.getArrivalTime()
            index = j
        j+=1
    return [mini,index]

def getMinimumBurstTime(process):
    mini = 9999999999999999999999
    index = -1
    j = 0
    for i in process:
        if (mini >= i.getBurstTime()):
            mini = i.getBurstTime()
            index = j
        j += 1
    return [mini, index]

def getMaximum(process):
    maxi = -9999999999999999999999
    index = -1
    j = 0
    for i in process:
        if (maxi >= i.getArrivalTime()):
            maxi = i.getArrivalTime()
            index = j
        j += 1
    return [maxi, index]

def executeSJF():
    tempProcess = []
    tempProcess = list(processSJF)
    index = getMinimum(processSJF)[1]
    # print(index)

    tempProcess.remove(processSJF[index])
    tempPr = processSJF[index]
    # print(tempPr.getPids())
    completionTimeSJF.append(Complection(tempPr.getPids(),tempPr.getArrivalTime(),tempPr.getBurstTime(),
                                         tempPr.getBurstTime(),0, tempPr.getBurstTime()))
    indexCom = 0

    for j in range(len(tempProcess)):
        x = []
        for i in range(len(tempProcess)):
            if (tempProcess[i].getArrivalTime() <= completionTimeSJF[indexCom].getCompleteTime()):
                x.append(tempProcess[i])
        tempIndex = getMinimumBurstTime(x)[1]
        tempPr = x[tempIndex]

        completionTimeSJF.append(Complection(tempPr.getPids(), tempPr.getArrivalTime(), tempPr.getBurstTime(),
                                             tempPr.getBurstTime() + completionTimeSJF[indexCom].getCompleteTime(),
                                             completionTimeSJF[indexCom].getCompleteTime() - tempPr.getArrivalTime(),
                                             tempPr.getBurstTime() + completionTimeSJF[
                                                 indexCom].getCompleteTime() - tempPr.getArrivalTime()))

        # print(completionTimeSJF[indexCom].getPids(),' ',completionTimeSJF[indexCom].getWaitingTime())
        waitingTimeSJF.append(completionTimeSJF[indexCom].getCompleteTime() - tempPr.getArrivalTime())
        turnAroundTimeSJF.append(tempPr.getBurstTime() + completionTimeSJF[indexCom].getCompleteTime() - tempPr.getArrivalTime())

        indexCom += 1
        tempProcess.remove(tempPr)
        # print(x[tempIndex].getPids())

    # print(completionTimeSJF[indexCom].getPids(), ' ', completionTimeSJF[indexCom].getWaitingTime())
            # print(completionTimeSJF[0].getPids())

    print("Result--> SJF")
    print('PID   Arrival Time  Burst Time Completion Time   Waiting Time   Turn around time')
    for i in range(len(completionTimeSJF)):
        print(completionTimeSJF[i].getPids(),'  ',completionTimeSJF[i].getArrivalTime(),'  ',completionTimeSJF[
            i].getBurstTime(),'  ',completionTimeSJF[i].getWaitingTime(),'  ',completionTimeSJF[i].getTurnAroundTime())

    print('Avg Waiting time = ',sum(waitingTimeSJF)/len(waitingTimeSJF))
    print('Avg turn around time = ',sum(turnAroundTimeSJF)/len(turnAroundTimeSJF))

readFile()
averageBurstTime =sum(burstTimeMain)/len(burstTimeMain)
processSJF = []
processRR = []
completionTimeSJF = []


separatePids()
executeSJF()




# for p in processSJF:
#     print(p.getPids())






# print(getAvgBurstTime())