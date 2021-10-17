# Brandon Chen and Jack Xu
# CSCI 420
# Homework 06
# Cross Correlation of data

# imports
import numpy as np
import math

header = ['ID', 'Milk', 'ChdBby', 'Vegges', 'Cerel', 'Bread', 'Rice', 'Meat', 'Eggs', 'YogChs', 'Chips', 'Soda', 'Fruit', 'Corn', 'Fish', 'Sauce', 'Beans', 'Tortya', 'Salt', 'Scented', 'Salza']
headerForCrossCorrelationMatrix = header[1:]

# gather the data from a filename
# split the data by commas and then strip the spaces from the strings and convert each attribute to integers
# populate two lists at a time
# 1. lists of all the grocery purchases for all shoppers [[id1, id2, id3, ...], [milkQuantity1, milkQuantity2, milkQuantity3, ...], [...], ...]
# 2. list of purchases for the shopper [id, milkQuantity, ChdBbyQuantity, ...]
# return an array of data
def gatherData(filename):
    file = open(filename)
    file.readline()
    
    dataArray = []
    groceryArray = [[] for headerNum in range(len(header))]
    print(len(groceryArray))
    line = file.readline()
    while line:
        data = line.split(',')
        for attribute in range(len(data)):
            attributeVal = int(data[attribute].strip())
            data[attribute] = attributeVal
            groceryArray[attribute].append(attributeVal)
        
        dataArray.append(data)
        line = file.readline()
    return dataArray, groceryArray

# use the numpy package to create a cross-correlation matrix
# round the correlation coefficients to two decimal places
def cross_correlation(data):
    # print(data)
    correlation_coefficient_matrix = np.corrcoef(data[1:])
    # print(correlation_coefficient_matrix)
    for row in range(len(correlation_coefficient_matrix)):
        for col in range(len(correlation_coefficient_matrix[0])):
            correlation_coefficient_matrix[row][col] = round(correlation_coefficient_matrix[row][col], 2)
            # print(correlation_coefficient_matrix[row][col])
    return correlation_coefficient_matrix

def answerReportQuestion(data):
    biggest = 0
    indexi, indexj = -1,-1
    #2a
    # for i in range (len(data)):
    #     for j in range (len(data)):
    #         current_val = abs(data[i][j])
    #         # print(current_val)
    #         if (current_val > biggest  and current_val < 1):
    #             indexi = i
    #             indexj = j
    #             biggest = current_val
    # print(biggest)
    # print(indexi,indexj)
    # print(len(data))
    # print(len(header))
    #2b
    # cerealIndex = headerForCrossCorrelationMatrix.index("Cerel")
    # chipsIndex = headerForCrossCorrelationMatrix.index("Chips")
    # print(cerealIndex, chipsIndex)
    # print(data[cerealIndex][chipsIndex])
    #2c
    # print(headerForCrossCorrelationMatrix)
    # fishIndex = headerForCrossCorrelationMatrix.index("Fish")
    # fishRow = data[fishIndex]
    # # print(fishIndex)
    # fishMax = 0
    # fishMaxIndex = -1
    # for i in range(len(fishRow)):
    #     currVal = abs(fishRow[i])
    #     if (currVal > fishMax and currVal < 1):
    #         fishMax = currVal
    #         fishMaxIndex = i
    # print(fishMax, headerForCrossCorrelationMatrix[fishMaxIndex])
    #2d
    # veggieIndex = headerForCrossCorrelationMatrix.index("Vegges")
    # veggieRow = data[veggieIndex]
    # veggieMax = 0
    # veggieMaxIndex = - 1
    # for i in range(len(veggieRow)):
    #     currVal = abs(veggieRow[i])
    #     if ( currVal > veggieMax and currVal < 1):
    #         veggieMax = currVal
    #         veggieMaxIndex = i
    # print(veggieMax, headerForCrossCorrelationMatrix[veggieMaxIndex])
    #2e
    # milkIndex = headerForCrossCorrelationMatrix.index("Milk")
    # cerealIndex = headerForCrossCorrelationMatrix.index("Cerel")
    # print(data[milkIndex][cerealIndex])
    #2f
    # notStrongName1 = headerForCrossCorrelationMatrix[15]
    # notStrongName2 = headerForCrossCorrelationMatrix[17]
    # print(data[15])
    # print(data[17])
    # print(notStrongName1, notStrongName2)
    #2g
    # fishIndex = headerForCrossCorrelationMatrix.index("Fish")
    # print(data[fishIndex])

# Get the center of a Cluster given a cluster
# Find the average of all the points in the cluster
def getMiddleOfCluster(cluster):
    numPoints = len(cluster)
    middlePoint = [0]*len(cluster[0])
    for point in cluster:
        for attribute in range(len(point)):
            middlePoint[attribute] += point[attribute]
    for attributeMean in range(len(middlePoint)):
        middlePoint[attributeMean] = middlePoint[attributeMean]/numPoints
    return middlePoint

# Get the distance between clusters by comparing the centers of the two clusters
# Use the Euclidean Distance between the center of the clusters
def getDistanceBetweenClusters(center1, center2):
    total_distance = 0
    for index in range(len(center1)):
        total_distance += ((center1[index] - center2[index])**2)
    return math.sqrt(total_distance)


def getCenterOfCluster(clusterVal):
    print(clusterVal)
    medianArray = []
    attributeNum = len(clusterVal[0])
    for attributeID in range(1,attributeNum):
        attributeValArray = []
        #Create a new array from each entry with this attribute
        for entry in clusterVal:
            attributeValArray.append(entry[attributeID])
        #Find the median of this array and append it to the median array
        medianOfAttribute = np.median(attributeValArray)
        medianArray.append(medianOfAttribute)
    return medianArray

def agglomerate(data):
    # clusters will be a dictionary of {clusterID:[nodes]}
    clusters = {}
    # clusterCenters will be a dictionary of {clusterID:[id]}
    clusterCenters = {}
    # initialize data into clusters
    clusterID = 1
    for dataPoint in data:
        clusters[clusterID] = [dataPoint]
        clusterCenters[clusterID] = dataPoint[1:]
        clusterID += 1
    
    # keep clustering while there is more than 1 cluster
    while len(clusters) > 1:
        print(len(clusters))
        closestClusters = [-1, -1]
        closestDistance = float('inf')
        for id1 in clusters:
            for id2 in clusters:
                if id1 == id2:
                    continue
                center1 = clusterCenters[id1]
                center2 = clusterCenters[id2]
                # print(center1)
                # print(center2)
                dist = getDistanceBetweenClusters(center1, center2)
                if dist < closestDistance:
                    closestDistance = dist
                    closestClusters = [id1, id2]
        # print(closestClusters)
        # print(clusters[closestClusters[0]])
        if (closestClusters[0] != -1 and closestClusters[1] != -1):
            #We have 2 closest cluster
            #Sort the id
            closestClusters.sort()
            id1 = closestClusters[0]
            id2 = closestClusters[1]
            cluster1 = clusters[id1]
            cluster2 = clusters[id2]
            #Merge the 2 clusters
            cluster1.extend(cluster2)
            mergedCluster = cluster1
            #Update cluster1 in the dictionary
            clusters[id1] = mergedCluster
            clusters.pop(id2)
            clusterCenters.pop(id2)
            medianArray = getCenterOfCluster(mergedCluster)
            # print(medianArray)
            clusterCenters[id1] = medianArray
    print(clusters)

# write the correlation coefficient matrix to a file
def writeToFile(matrix, filename):
    file = open(filename, 'w')
    for row in range(len(matrix)):
        string = ''
        for col in range(len(matrix[0])):
            string += str(matrix[row][col]) + '   '
        file.write(string + '\n')
    return

# main function
def main():
    shopperArray, groceryArray = gatherData('HW_CLUSTERING_SHOPPING_CART_v2211.csv')
    cross_correlation_matrix = cross_correlation(groceryArray)
    agglomerate(shopperArray)
    # agglomerate(cross_correlation_matrix)
    # answerReportQuestion(cross_correlation_matrix)
    # writeToFile(cross_correlation_matrix, 'correlation_matrix.csv')
    

if __name__ == '__main__':
    main()