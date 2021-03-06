#!/usr/bin/env python
# coding: utf-8

# In[5]:


import csv
with open('iris.data.txt', 'r') as csvfile:
    lines = csv.reader(csvfile)
    for row in lines :
        print (', '.join(row))


# # Handle Data

# In[11]:


import csv
import random
def loadDataset(filename, split, trainingSet=[] , testSet=[]):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])


# # Similarity

# In[25]:


import math
def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)


# # Neighbors

# In[23]:


import operator
def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key = operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


# #  Response

# In[35]:


def getResponse(neighbors):
    # Creating a list with all the possible neighbors
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]


# # Accuracy 

# In[36]:


def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0


# #  Main

# In[45]:


def main():
    trainingSet=[]
    testSet=[]
    loadDataset('iris.data.txt', 0.66, trainingSet, testSet)
    print ('Train: ' + repr(len(trainingSet)))
    print ('Test: ' + repr(len(testSet)) )   
    data1 = [2, 2, 2, 'a']
    data2 = [4, 4, 4, 'b']
    distance = euclideanDistance(data1, data2, 3)
    print ('Distance: ' + repr(distance))
    trainSet = [[2, 2, 2, 'a'], [4, 4, 4, 'b']]
    testInstance = [5, 5, 5]
    k = 1
    neighbors = getNeighbors(trainSet, testInstance, 1)
    print(neighbors)
    testSet = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
    predictions = ['a', 'a', 'a']
    accuracy = getAccuracy(testSet, predictions)
    print(accuracy)

        
    

main()
        

