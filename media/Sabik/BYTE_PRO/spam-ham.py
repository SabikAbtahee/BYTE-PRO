import pandas as pd
from sklearn.model_selection import train_test_split
from collections import defaultdict

def readData():
    dataframe = pd.read_csv("spam_detection_dataset.csv")
    #print (dataframe)
    return dataframe
    
def splitBody(train,test):
    trainlabel=[]
    trainBody=[]
    testlabel=[]
    testBody=[]
    for index, row in train.iterrows():
        trainlabel.append(row['label'])
        trainBody.append(row['body'].split(" "))
    for index, row in test.iterrows():
        testlabel.append(row['label'])
        testBody.append(row['body'].split(" "))
    
    return trainBody,testBody,trainlabel,testlabel

def splitDataframe(dataframe):
    train , test = train_test_split(dataframe, test_size=0.1)
    return train,test
    
def spamHamCount(trainBody,trainlabel):
    ham=defaultdict(int)
    spam=defaultdict(int)
    wordProbabilityHam={}
    
    for i in range(len(trainlabel)):
        if(trainlabel[i]=='ham'):
            for j in range(len(trainBody[i])):
                ham[trainBody[i][j]]+=1
        else:
            for j in range(len(trainBody[i])):
                spam[trainBody[i][j]]+=1
    
    for j in range(len(trainlabel)):
        for h in range(len(trainBody[j])):
            wordProbabilityHam[trainBody[j][h]]=(ham[trainBody[j][h]])/(ham[trainBody[j][h]]+spam[trainBody[j][h]])
    return wordProbabilityHam   

def testData(wordprobabilityHam,testBody,testlabel):
    TN=0
    TP=0
    FP=0
    FN=0
    ham=1
    spam=1
    match=0
    for i in range(len(testlabel)):
        ham=1
        spam=1
        for j in range(len(testBody[i])):
            if testBody[i][j] in wordprobabilityHam:
               ham *= wordprobabilityHam[testBody[i][j]]
               spam *= 1-wordprobabilityHam[testBody[i][j]]
            else:
               ham*=0.5
               
        if(ham>spam):
            if(testlabel[i]=='ham'):
                TN+=1
                match+=1
            else:
                FN+=1
        else:
            if(testlabel[i]=='spam'):
                TP+=1
                match+=1
            else:
                FP+=1
                
    return TN,TP,FP,FN,match

def runloop(dataframe):
    train,test=splitDataframe(dataframe)
    trainBody,testBody,trainlabel,testlabel = splitBody(train,test)
    wordprobabilityHam = spamHamCount(trainBody,trainlabel)
    TN,TP,FP,FN,match=testData(wordprobabilityHam,testBody,testlabel)
    return TN,TP,FP,FN,match,len(testlabel)


def printAll(Accuracy,Precision,Recall):

    print("All Information: \n ")
    print("Accuracy: {}%".format(Accuracy))
    print("Precision: ", Precision)
    print("Recall: ", Recall)
    
    
def calculate_precision_accuracy_recall(TN,TP,FP,FN,match,totalMatch,testCase):
    #print(TN,TP,FP,FN,match,totalMatch,testCase)
    match=sum(match)/testCase
    TP=sum(TP)/testCase
    TN=sum(TN)/testCase
    FP=sum(FP)/testCase
    FN=sum(FN)/testCase
    #print(TN,TP,FP,FN,match)
    
    Accuracy = (match)/totalMatch *100
    Precision = TP / (TP+FP)
    Recall = TP / (TP+FN)
    
    printAll(Accuracy,Precision,Recall)

def main():
    dataframe=readData()
    TN,TP,FP,FN,match=[],[],[],[],[]
    
    
    testCase=15
    
    
    for i in range(testCase):
        TN1,TP1,FP1,FN1,match1,totalMatch=runloop(dataframe)
        TN.append(TN1)
        TP.append(TP1)
        FP.append(FP1)
        FN.append(FN1)
        match.append(match1)
        
    calculate_precision_accuracy_recall(TN,TP,FP,FN,match,totalMatch,testCase)
    
    
if __name__=="__main__":
    main()