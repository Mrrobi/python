class KnnRegression:
  def __init__(self,path, TargetAtLast):
    self.path = path
    self.TargetAtLast = TargetAtLast
  def loadToList(self):
    from numpy import genfromtxt
    dataset = genfromtxt(self.path, delimiter=',')
    DataList = dataset.tolist()
    import random
    import math as m
    for x in DataList:
      for y in range(len(x)):
        z = float(x[y])
        if m.isnan(z):
          x[y] = 0
    random.shuffle(DataList)
    return DataList
  def list_split(self, DataList):
    Train_set=[]
    Val_set=[]
    Test_set=[]
    from random import random
    for x in DataList:
      R = random()
      if R >= 0 and R <= 0.7:
        Train_set.append(x)
      elif R >= 0.7 and R <= 0.85:
        Val_set.append(x)
      else:
        Test_set.append(x)
    return Train_set, Val_set, Test_set
  def knn(self, Val_set, Train_set, k):
    from scipy.spatial import distance
    import operator
    correct = 0
    error = 0;
    for s in Val_set:
      ValueDict = {}
      for v in Train_set:
        if self.TargetAtLast :
              ed = distance.euclidean(s[:(len(s)-1)], v[:(len(v)-1)])
              ValueDict[ed] = v[-1]
        else:
              ed = distance.euclidean(s[1:], v[1:])
              ValueDict[ed] = v[0]
        
      sorted_L = sorted(ValueDict.keys())
      count = 1
      total_val = 0.0
      for x in sorted_L:
        total_val = total_val + ValueDict[x]
        count = count + 1
        if(count > k):
          break
      val = total_val/k
      if self.TargetAtLast:
          error = error + (s[-1] - val)**2
      else:
          error = error + (s[0] - val)**2
    accuracy = (error/len(Val_set))**(1/2)
    return accuracy
