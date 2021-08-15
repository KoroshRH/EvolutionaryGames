import matplotlib.pyplot as plt
import numpy as np

minFitnessList = []
maxFitnessList = []
meanFitnessList = []

mode = "helicopter"

generations = open("generation-" + mode + ".txt", "r")

generationsCount = 0
for line in generations.readlines():
    lineList = line.split(",")
    minFitnessList.append(float(lineList[0])) 
    maxFitnessList.append(float(lineList[1])) 
    meanFitnessList.append(float(lineList[2])) 
    generationsCount += 1

x = np.arange(0, generationsCount, step=1)

plt.plot(x, minFitnessList, label="min")
plt.plot(x, maxFitnessList, label="max")
plt.plot(x, meanFitnessList, label="mean")
plt.legend()
plt.show()