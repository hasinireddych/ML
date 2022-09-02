import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
In [40]: model = KNeighborsClassifier(n_neighbors=3)
train_feature= np.array(train _feature).reshape((-1,1))
model.fit(train_feature, train label)
test_feature = p.array(test_feature).reshape((-1,1))
predicted = model.predict(test feature)
print ("Confusion Matrix: \n", confusion matrix(predicted, test_label))
cf matrix = confusion _matrix(predicted,test label)
TP = cf _matrix[0][@]
TN = cf matrix[1][1]
FP = cnf_matrix[0][1]
FN = enf_matrix[1][0]
Confusion Matrix :[re 0][3 1]]
In [42]: accuracy = (TP + TN) / (TP+TN+FP+FN)
print ("Accuray, accuracy")
sensitivity = TP/(TP + FN)
print ("Sensitivity :,sensitivity")
Specificity = TN/(TN+FP)
print ("Specificity :",Specificity)