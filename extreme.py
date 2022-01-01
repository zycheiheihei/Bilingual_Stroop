import numpy as np


data = np.array([1,1,1,1,1,1,1,1,1,1,10])
arithmeticMean = data.mean()
standardDeviation = data.std()
residualError = abs(data - arithmeticMean)
print(standardDeviation)
print(arithmeticMean)
sum = 0
cnt = 0
for i in range(data.shape[0]):
    if residualError[i]<3*standardDeviation:
        sum+=data[i]
        cnt+=1
    else:
        print("extreme case erased")