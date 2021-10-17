# Brandon Chen and Jack Xu
# CSCI 420
# Homework 06
# Cross Correlation of data

# imports
import numpy as np

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
    milkIndex = headerForCrossCorrelationMatrix.index("Milk")
    cerealIndex = headerForCrossCorrelationMatrix.index("Cerel")
    print(data[milkIndex][cerealIndex])


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
    answerReportQuestion(cross_correlation_matrix)
    # writeToFile(cross_correlation_matrix, 'correlation_matrix.csv')
    

if __name__ == '__main__':
    main()