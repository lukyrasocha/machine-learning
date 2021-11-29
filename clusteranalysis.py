# Got inspired from the book by Miller & Ranum
# Author: Lukas Rasocha

#Imports
import math
import numpy as np
import random
import matplotlib.pyplot as plt

k = list(range(2,14)) # trying different clusters

#Function to calculate the distance of two points in a len(point1)-space
def eucliD(point1, point2):
    sum = 0
    for index in range(len(point1)):
        diff = (point1[index] - point2[index]) ** 2
        sum = sum + diff
        distance = math.sqrt(sum)
    return distance


def readfile(filename):
   with open (filename, "r") as fileHandler: 
      key = 0
      datadict = {}
      for line in fileHandler:
          key = key + 1
          items = line.split()
          feature1 = float(items[1])
          incidents00_14 = float(items[2])
          datadict[key] = [distancePerWeek,incidents00_14] 
   return datadict


def createClusters(datadict, repeats):
    clusterList = []
    listOfSum = []  
    
    for numberOfClusters in k:
        centroids = [] 
        centroidCount = 0  
        centroidKeys = []  
        myMainSum = 0
        while centroidCount < numberOfClusters:     
            rkey = random.randint(1, len(datadict)) # picks a random key
        
            if rkey not in centroidKeys:    
                centroids.append(datadict[rkey]) 
                centroidKeys.append(rkey) # this adds the rkey to the list so we can check if the rkey has been already used (so we dont pick two points twice)
                centroidCount = centroidCount + 1
        
        for apass in range(repeats):
            
            clusters = [] 
            for i in range(numberOfClusters):
                clusters.append([]) 

            #calculating distances from datapoints to centroids and putting datapoints to corresponding clusters
            for akey in datadict:
                distances = []
                
                for clusterIndex in range(numberOfClusters): 
                    dist = eucliD(datadict[akey], centroids[clusterIndex]) # this calculates the distances (from centroids) to each datapoint
                    distances.append(dist)
                
                mindist = min(distances) 
                index = distances.index(mindist) 
                clusters[index].append(akey)  

                # now when you print clusters[1] you get all the datapoints KEYS that are closest to centroid 1

            dimensions = len(datadict[1]) 
            # calculates new centroid for every cluster by calculating the average of the datapoints in corresponding cluster.
            for clusterIndex in range (numberOfClusters):
                sums = [0] * dimensions 
                
                for akey in clusters[clusterIndex]: 
                    datapoints = datadict[akey] 
                    for ind in range(len(datapoints)):
                        sums[ind] = sums[ind] + datapoints[ind] # ads up the coordinates so we can calculate the average position of all datapoints in each cluster
                        
                for ind in range(len(sums)): 
                    clusterLen = len(clusters[clusterIndex])
                    if clusterLen !=0:
                        sums[ind] = sums[ind] / clusterLen 
                        
                centroids[clusterIndex] = sums # creates a new centroid that is the average of all datapoints in each cluster
                  
        for clusterIndex in range(numberOfClusters): #calculates the distances
            for akey in clusters[clusterIndex]: 
                distanceFromCentroid = eucliD(centroids[clusterIndex], datadict[akey])
                myMainSum += distanceFromCentroid
        listOfSum.append(myMainSum)
        indexK = k.index(numberOfClusters)
        clusterList.append([])
        clusterList[indexK].append(clusters)
            
    plt.figure(1)
    plt.plot(listOfSum, '.-')
    plt.show()
          
    return (listOfSum, clusterList)

#Find best number of clusters using the Elbow method
def findBestK(listOfSum, clusterList):
    bestList = []
    best = []
    bestRelative = []
    bestSum = 0
    for index in range(len(listOfSum)-1): 
        bestDifference = listOfSum[index] - listOfSum[index+1] 
        bestSum = bestSum + bestDifference
        best.append(bestDifference)
    for index in range(len(best)):
        bestRelative.append(best[index] / bestSum)
    
    for relative in bestRelative:
        
        if math.sqrt(relative*relative) < 0.15:
            bestList.append(relative)
    
    lowestIndex = bestRelative.index(bestList[0])
    print("LOWEST INDEX IS ", lowestIndex)
    
    bestK = k[lowestIndex]
    print("FINAL BEST NUMBER OF CLUSTER IS", bestK)
    
    print("*****************FINISH CLUSTER HURRAY *****************", clusterList[lowestIndex])
    
    bestCluster = clusterList[lowestIndex]  
    return bestCluster, bestK


def visualize(datadict, bestCluster, bestK):
    colors = [[0,1,0],[1,0,0],[0,0,1],[1,0,1], [1,1,0], [0,1,1], [1,0.4,0], [0, 0.2, 0.4], [0.2, 0, 0.5], [0.1, 0.5, 0], [0, 0.5, 0.2], [0.4, 1, 0.1], [0.3, 0, 0.5], [0.1, 0, 0.8]]
    for number in bestCluster:
        for index in range(bestK):
            for akey in number[index]:
                datapoint = datadict[akey]
                plt.plot(datapoint[0], datapoint[1], 'o', color = (colors[index]))
        plt.show()
                
                    
def clusterAnalysisAirlines(dataFile):
   airDict = readfile(dataFile)
   listOfSum,clusters = createClusters(airDict, 20)
   airBest,bestK = findBestK(listOfSum,clusters)

   visualize(airDict,airBest, bestK)
    

 
if __name__ == '__main__':
    clusterAnalysisAirlines("airplanes.txt")

                        
                        
                    
                


          
            
                
            
        
        


    
    
        

