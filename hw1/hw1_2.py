import matplotlib.pyplot as plt
import numpy as np 

#%matplotlib inline
attribute_num=4
name_arr=[' sepal_length',' sepal_width',' petal_length',' petal_width']
target_arr=['Iris-setosa','Iris-versicolor','Iris-virginica']
def arr_init(arr,l,data_arr,feature_num):
    for i in range(l):
        arr.append(float(data_arr[i][feature_num]))
def visual_data(mean_arr,std_arr,name_arr):
    index=np.arange(len(name_arr))
    arr=[]
    for i in range(len(name_arr)):
        arr.append(i)
    plt.bar(index, mean_arr,width=0.2, label = 'average' )
    for item,mean_arr in zip(index,mean_arr):
        x=item-0.25
        plt.text(
            x, 
            mean_arr, 
            str(mean_arr),
        )
    plt.bar(index+0.2, std_arr,width=0.2,label = 'standard_deviation')
    for index,std_arr in zip(index,std_arr):
        item=index+0.2
        plt.text(
            item, 
            std_arr+0.20, 
            str(std_arr),
        )
    
    plt.ylabel("cm")
    plt.xticks(arr,name_arr)  
    
    plt.figure()
def arr_sep(l,data_arr):
    num=[]
    num1=[]
    num2=[]
    for i in range(l):
        if data_arr[i][4]==target_arr[0]:
            num.append(data_arr[i])
    for i in range(l):
        if data_arr[i][4]==target_arr[1]:
            num1.append(data_arr[i])
    for i in range(l):
        if data_arr[i][4]==target_arr[2]:
            num2.append(data_arr[i])
            
    return num,num1,num2
def arr_mean_and_std(data_arr):
    mean_arr=[]
    #for i in range(len(target_arr)):
        #mean_arr.append([])
    std_arr=[]
    #for i in range(len(target_arr)):
        #std_arr.append([])
    arr=[]
    
    for j in range(attribute_num):
        for k in range(len(data_arr)):
            arr.append(float(data_arr[k][j]))
        mean_arr.append(round(np.mean(arr),6))
        std_arr.append(round(np.std(arr),6))
        arr.clear()
    return mean_arr ,std_arr


    
def pring_hist(arr,num,title):
    l=plt.hist(arr,bins=num,edgecolor='k')
    plt.title(title)
    #plt.legend()
    #print(l)
    plt.show()
    plt.figure()
def print_split_hist(data_arr,feature_num):
    num1=[]
    num2=[]
    num3=[]
    for i in range(len(data_arr)):
        if(data_arr[i][4]==target_arr[0]):
            num1.append(data_arr[i][feature_num])
        elif(data_arr[i][4]==target_arr[1]):
            num2.append(data_arr[i][feature_num])
        elif(data_arr[i][4]==target_arr[2]):
            num3.append(data_arr[i][feature_num])
    pring_hist(num1,10,target_arr[0]+name_arr[feature_num])
    pring_hist(num2,10,target_arr[1]+name_arr[feature_num])
    pring_hist(num3,10,target_arr[2]+name_arr[feature_num])
def split_arr(data_arr):
    num1=[]
    num2=[]
    num3=[]
    for i in range(len(data_arr)):
        if(data_arr[i][4]==target_arr[0]):
            num1.append(data_arr[i])
        elif(data_arr[i][4]==target_arr[1]):
            num2.append(data_arr[i])
        elif(data_arr[i][4]==target_arr[2]):
            num3.append(data_arr[i])
    return num1,num2,num3
    
fp = open('bezdekIris.data', "r")
arr=[]
line = fp.readline()
while line:
    line = line.strip('\n').split(',')  
    arr.append(line)
    line = fp.readline()
#print(arr[:]) 
fp.close()
#print(len(arr))
f1=[]
f2=[]
f3=[]
f4=[]
arr_init(f1,len(arr),arr,0)
arr_init(f2,len(arr),arr,1)
arr_init(f3,len(arr),arr,2)
arr_init(f4,len(arr),arr,3)
#print(type(f2))
means=[]
means.append(np.mean(f1))
means.append(np.mean(f2))
means.append(np.mean(f3))
means.append(np.mean(f4))
stds=[]
stds.append(np.std(f1))
stds.append(np.std(f2))
stds.append(np.std(f3))
stds.append(np.std(f4))
visual_data(means,stds,name_arr)
pring_hist(f1,10,name_arr[0])
pring_hist(f2,10,name_arr[1])
pring_hist(f3,10,name_arr[2])
pring_hist(f4,10,name_arr[3])
arr1,arr2,arr3=split_arr(arr)
n1,n2,n3=arr_sep(len(arr),arr)
m1,s1=arr_mean_and_std(n1)
m2,s2=arr_mean_and_std(n2)
m3,s3=arr_mean_and_std(n3)
visual_data(m1,s1,name_arr)
visual_data(m2,s2,name_arr)
visual_data(m3,s3,name_arr)
#visual_data_split(means,stds,name_arr)
print_split_hist(arr,0)
print_split_hist(arr,1)
print_split_hist(arr,2)
print_split_hist(arr,3)

