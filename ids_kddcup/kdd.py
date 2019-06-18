import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_kddcup99
from sklearn.preprocessing import scale
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import roc_curve
from sklearn.neighbors import KNeighborsClassifier

from sklearn.svm import SVC

from sklearn.tree import DecisionTreeClassifier

g = open('otuput.txt','w')
h = open('reduced.txt','w')
data, target = fetch_kddcup99(return_X_y = True, shuffle = True)
print(data.shape)
print(data)
print(target.shape)
print(target)
for i in target:
	g.write(str(i) + '\n')

a = list(set(target))
for i in a:
	h.write(str(i) + '\n')

# remove categorical features
f = open('description.txt','r')
description = f.read()
description = description.split('\n')
for i in range(len(description)):
	description[i] = description[i].split(':')[1]

print(description)
print(len(description))

newdata = []
for i in range(data.shape[0]):
	temp = []
	for j in range(len(description)):
		if description[j] == ' continuous.':
			temp.append(data[i][j])
	newdata.append(temp)

print(len(newdata))
print(newdata[0])
newdata = np.asarray(newdata)
print(newdata.shape)

processeddata = scale(newdata)
print(processeddata.shape)

dataA = []
targetA = []
dataB = []
targetB = []
dataC = []
targetC = []
# get training sample
for i in range(len(target)):
	if target[i] == b'nmap.' or target[i] == b'normal.':
		dataA.append(processeddata[i])
		targetA.append(target[i])

dataA = np.asarray(dataA)
targetA = np.asarray(targetA)
print('Data A')
print(dataA.shape)
print(targetA.shape)

for i in range(len(target)):
	if target[i] == b'smurf.' or target[i] == b'normal.':
		dataB.append(processeddata[i])
		targetB.append(target[i])

print('Data B')
dataB = np.asarray(dataB)
targetB = np.asarray(targetB)
print(dataB.shape)
print(targetB.shape)

for i in range(len(target)):
	if target[i] == b'satan.' or target[i] == b'normal.':
		dataC.append(processeddata[i])
		targetC.append(target[i])

print('Data C')
dataC = np.asarray(dataC)
targetC = np.asarray(targetC)
print(dataC.shape)
print(targetC.shape)

# target normal to abnormal
for i in range(len(target)):
	if target[i] == b'normal.':
		target[i] = 0
	else:
		target[i] = 1

for i in range(len(targetA)):
	if targetA[i] == b'normal.':
		targetA[i] = 0
	else:
		targetA[i] = 1

for i in range(len(targetB)):
	if targetB[i] == b'normal.':
		targetB[i] = 0
	else:
		targetB[i] = 1

for i in range(len(targetC)):
	if targetC[i] == b'normal.':
		targetC[i] = 0
	else:
		targetC[i] = 1

print('What is Target?')
print(type(target))
print(target.shape)
target = target.astype(int)
targetA = targetA.astype(int)
targetB = targetB.astype(int)
targetC = targetC.astype(int)
print('After')
print(type(target))
print(target.shape)

C45 = DecisionTreeClassifier(max_depth = 3)
C45.fit(processeddata[:5000], target[:5000])

result = C45.predict_proba(processeddata[5000:])
print(result)
print(result.shape)

# roc curve
print('Final Check')
print(target[5000:].shape)
fpr, tpr, _ = roc_curve(target[5000:], result[:,1], pos_label = 1)
print(fpr)
print(tpr)
plt.figure(1)
plt.plot(fpr, tpr, label = 'A')


C45A = DecisionTreeClassifier(max_depth = 3)
C45A.fit(dataA[:5000], targetA[:5000])
resultA = C45A.predict_proba(processeddata[5000:])
fprA, tprA, _ = roc_curve(target[5000:], resultA[:,1], pos_label = 1)
plt.plot(fprA, tprA, label = 'B')


C45B = DecisionTreeClassifier(max_depth = 3)
C45B.fit(dataB[:5000], targetB[:5000])
resultB = C45B.predict_proba(processeddata[5000:])
fprB, tprB, _ = roc_curve(target[5000:], resultB[:,1], pos_label = 1)
plt.plot(fprB, tprB, label = 'C')

C45C = DecisionTreeClassifier(max_depth = 3)
C45C.fit(dataC[:5000], targetC[:5000])
resultC = C45C.predict_proba(processeddata[5000:])
print('Final Check')
print(resultB.shape)
print(resultC.shape)
fprC, tprC, _ = roc_curve(target[5000:], resultC[:,1], pos_label = 1)
plt.plot(fprC, tprC, label = 'D')
plt.legend() 

plt.figure(2)
KNN = KNeighborsClassifier()
KNN.fit(processeddata[:5000], target[:5000])
result1 = KNN.predict_proba(processeddata[5000:])
fpr1, tpr1, _ = roc_curve(target[5000:], result1[:,1], pos_label = 1)
plt.plot(fpr1, tpr1, label = 'A')


KNNA = DecisionTreeClassifier(max_depth = 3)
KNNA.fit(dataA[:5000], targetA[:5000])
result1A = KNNA.predict_proba(processeddata[5000:])
fpr1A, tpr1A, _ = roc_curve(target[5000:], result1A[:,1], pos_label = 1)
plt.plot(fpr1A, tpr1A, label = 'B')


KNNB = DecisionTreeClassifier(max_depth = 3)
KNNB.fit(dataB[:5000], targetB[:5000])
result1B = KNNB.predict_proba(processeddata[5000:])
fpr1B, tpr1B, _ = roc_curve(target[5000:], result1B[:,1], pos_label = 1)
plt.plot(fpr1B, tpr1B, label = 'C')

KNNC = DecisionTreeClassifier(max_depth = 3)
KNNC.fit(dataC[:5000], targetC[:5000])
result1C = KNNC.predict_proba(processeddata[5000:])
fpr1C, tpr1C, _ = roc_curve(target[5000:], result1C[:,1], pos_label = 1)
plt.plot(fpr1C, tpr1C, label = 'D')
plt.legend() 

plt.figure(3)
SVM = SVC()
SVM.fit(processeddata[:5000], target[:5000])
result2 = SVM.decision_function(processeddata[5000:])
print(result1.shape)
fpr2, tpr2, _ = roc_curve(target[5000:], result2, pos_label = 1)
plt.plot(fpr2, tpr2, label = 'A')

SVMA = SVC()
SVMA.fit(dataA[:5000], targetA[:5000])
result2A = SVMA.decision_function(processeddata[5000:])
fpr2A, tpr2A, _ = roc_curve(target[5000:], result2A, pos_label = 1)
plt.plot(fpr2A, tpr2A, label = 'B')

SVMB = SVC()
SVMB.fit(dataB[:5000], targetB[:5000])
result2B = SVMB.decision_function(processeddata[5000:])
fpr2B, tpr2B, _ = roc_curve(target[5000:], result2B, pos_label = 1)
plt.plot(fpr2B, tpr2B, label = 'C')

SVMC = SVC()
SVMC.fit(dataC[:5000], targetC[:5000])
result2C = SVMC.decision_function(processeddata[5000:])
fpr2C, tpr2C, _ = roc_curve(target[5000:], result2C, pos_label = 1)
plt.plot(fpr2C, tpr2C, label = 'D')


plt.legend() 
plt.show()

print('Whar the Fuck?')
print(result1B.shape)
print(list(set(result1B[0])))