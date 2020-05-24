# KNN Classification Algorithm.
Anyone of you can use this library to do KNN Classification in Google Colab
with a all numeric valued dataset.
[Github Open Source](https://github.com/Mrrobi/python/packages/knnClassification)

## Existing methods
* KnnClassification(path,TargetAtLast) - It takes two parameter first one is a string of the csv file path and the second one is a boolean to specify, the position of the target coloum it target is at last then the value will be True.Returns a object of KnnClassification class
* loadToList() - It returns the loaded dataset as a python list.
* list_split(DataList) - It takes a single parameter the dataset list from the which is the return value of previous method,and it return a tuple containing three list Splited into Train(70%), Validation(15%), Test(15%).
* knn(x_list,y_list,k) - It takes three parameter first one is either validation list or test list, second one is train list and the third one is value of k, It returns the accuracy of the dataset.


## using process

### 1st need to add the library
```python
pip install KnnClassificationRobi
```
### 2nd You must need to mount your google drive if you want to load csv from your drive
```python
from google.colab import drive
drive.mount('/content/gdrive')
# You must need to run this code script at first to mount your drive with colab 
```
[Mount Drive with colab](https://colab.research.google.com/notebooks/io.ipynb)

### 3rd you need to copy the csv file path for further use

### 4th import KnnClassificationRobi and set the file path and target position
```python
import KnnClassificationRobi as KNN
KNN = KNN.KnnClassification("/content/sample_data/file_name.csv",True) #set path
```
### 5th load the dataset into a list and split it 
```python
DataList = KNN.loadToList() #Loading the list of given dataset
Train,Validation,Test = KNN.list_split(DataList) # Spliting dataset into three
```
### Run the knn to show the accuracy of the dataset 
```python
Accuracy = KNN.knn(Validation,Train,5) #Put Validation list to train or put test list to test.(here k=5)
print(Accuracy)
```

## N.B: Its not neccessary to split your dataset using given method(fix size) you could split your dataset by your own custom size as well :) 


