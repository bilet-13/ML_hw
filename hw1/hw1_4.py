import numpy as np
import random
import math
PI=3.14159
target_arr=['Iris-setosa','Iris-versicolor','Iris-virginica']
attribute_num=4
def arr_sep(l,data_arr):
    num=[]
    num.append([])
    num.append([])
    num.append([])
    for i in range(l):
        for k in range(len(target_arr)):
            if data_arr[i][4]==target_arr[k]:
                num[k].append(data_arr[i])
                break
    return num
def arr_mean_and_std(data_arr):
    mean_arr=[]
    for i in range(len(target_arr)):
        mean_arr.append([])
    std_arr=[]
    for i in range(len(target_arr)):
        std_arr.append([])
    arr=[]
    for i in range(len(target_arr)):
        for j in range(attribute_num):
            for k in range(len(data_arr[i])):
                arr.append(float(data_arr[i][k][j]))
            mean_arr[i].append(np.mean(arr))
            std_arr[i].append(np.std(arr))
            arr.clear()
    return mean_arr ,std_arr
'''def arr_sep(l,data_arr):
    num=[]
    num.append([])
    num.append([])
    num.append([])
    for i in range(l):
        for k in range(len(target_arr)):
            if data_arr[i][4]==target_arr[k]:
                num[k].append(data_arr[i])
                break
    return num'''
def arr_sep_kfold(data_arr,st1,st2,end):
    num=[]
    num.append([])
    num.append([])
    num.append([])
    for i in range(end):
        for k in range(len(target_arr)):
            if data_arr[st1+i][4]==target_arr[k]:
                num[k].append(data_arr[st1+i])
                break
    for i in range(end):
        for k in range(len(target_arr)):
            if data_arr[st2+i][4]==target_arr[k]:
                num[k].append(data_arr[st2+i])
                break
    return num
def arr_mean_and_std_kfold(data_arr,st1,st2,end):
    mean_arr=[]
    for i in range(len(target_arr)):
        mean_arr.append([])
    std_arr=[]
    for i in range(len(target_arr)):
        std_arr.append([])
    arr=[]
    for i in range(len(target_arr)):
        for j in range(attribute_num):
            for k in range(len(data_arr[i])):
                arr.append(float(data_arr[i][k][j]))
            mean_arr[i].append(np.mean(arr))
            std_arr[i].append(np.std(arr))
            arr.clear()
    return mean_arr ,std_arr

def judge_data(data_arr,sep_arr,train_num,mean_arr,std_arr):
    p_seto=len(sep_arr[0])/train_num
    p_vers=len(sep_arr[1])/train_num
    p_virg=len(sep_arr[2])/train_num
    for i in range(attribute_num):
        x=float(data_arr[i])
        p_seto+=math.log(math.exp(-math.pow(x-mean_arr[0][i],2)/(2*(std_arr[0][i]**2)))/(std_arr[0][i]*math.sqrt(2)*PI))
    for i in range(attribute_num):
        x=float(data_arr[i])
        p_vers+=math.log(math.exp(-math.pow(x-mean_arr[1][i],2)/(2*(std_arr[1][i]**2)))/(std_arr[1][i]*math.sqrt(2)*PI))
    for i in range(attribute_num):
        x=float(data_arr[i])
        p_virg+=math.log(math.exp(-math.pow(x-mean_arr[2][i],2)/(2*(std_arr[2][i]**2)))/(std_arr[2][i]*math.sqrt(2)*PI))
    if p_seto>p_vers:
        if p_seto>p_virg:
            return target_arr[0]
        else:
            return target_arr[2]
    else:
        if p_vers>p_virg:
            return target_arr[1]
        else:
            return target_arr[2]
fp = open('bezdekIris.data', "r")
arr=[]
line = fp.readline()
while line:
    line = line.strip('\n').split(',')  
    arr.append(line)
    line = fp.readline()
#print(arr[:]) 
fp.close()
random.shuffle(arr)
#print(len(arr))
#print(arr[:])
train_len=math.ceil(len(arr)*0.7)
 
s_s=0
s_ver=0
s_vir=0
ver_s=0
ver_ver=0
ver_vir=0
vir_s=0
vir_ver=0
vir_vir=0
sep_arr=arr_sep(train_len,arr)
(mean_arr,std_arr)=arr_mean_and_std(sep_arr)
#print(len(sep_arr[0]))
for i in range(len(arr)-train_len):
    p=judge_data(arr[train_len+i],sep_arr,len(arr)-train_len,mean_arr,std_arr)
    if arr[train_len+i][4]==target_arr[0]:
        if p==target_arr[0]:
            s_s+=1
        elif p==target_arr[1]:
            s_ver+=1
        elif p==target_arr[2]:
            s_vir+=1
    elif arr[train_len+i][4]==target_arr[1]:
        if p==target_arr[0]:
            ver_s+=1
        elif p==target_arr[1]:
            ver_ver+=1
        elif p==target_arr[2]:
            ver_vir+=1
    elif arr[train_len+i][4]==target_arr[2]:
        if p==target_arr[0]:
            vir_s+=1
        elif p==target_arr[1]:
            vir_ver+=1
        elif p==target_arr[2]:
            vir_vir+=1
print('confusion matrix:\n',s_s,
s_ver,
s_vir,'\n',
ver_s,
ver_ver,
ver_vir,'\n',
vir_s,
vir_ver,
vir_vir)
print('\nClassification accuracy:',(s_s+ver_ver+vir_vir)/(len(arr)-train_len))
print('setosa_sensitivity:',s_s/(s_s+s_ver+s_vir))        
print('versicolor_sensitivity:',ver_ver/(ver_s+ver_ver+ver_vir))  
print('virginica_sensitivity:',vir_vir/(vir_s+vir_ver+vir_vir))
print('setosa_precession:',s_s/(s_s+ver_s+vir_s))        
print('versicolor_precession:',ver_ver/(s_ver+ver_ver+vir_ver))  
print('virginica_precession:',vir_vir/(s_vir+ver_vir+vir_vir))
random.shuffle(arr)
k_len=math.ceil(len(arr)/3)
#print(k_len)
s_s=[0,0,0]
s_ver=[0,0,0]
s_vir=[0,0,0]
ver_s=[0,0,0]
ver_ver=[0,0,0]
ver_vir=[0,0,0]
vir_s=[0,0,0]
vir_ver=[0,0,0]
vir_vir=[0,0,0]
sep_arr=arr_sep_kfold(arr,1*k_len,2*k_len,k_len)
(mean_arr,std_arr)=arr_mean_and_std_kfold(sep_arr,1*k_len,2*k_len,k_len)
#print(mean_arr[:],std_arr[:])
for i in range(k_len):
    p=judge_data(arr[i],sep_arr,2*k_len,mean_arr,std_arr)
    if arr[i][4]==target_arr[0]:
        if p==target_arr[0]:
            s_s[0]+=1
        elif p==target_arr[1]:
            s_ver[0]+=1
        elif p==target_arr[2]:
            s_vir[0]+=1
    elif arr[i][4]==target_arr[1]:
        if p==target_arr[0]:
            ver_s[0]+=1
        elif p==target_arr[1]:
            ver_ver[0]+=1
        elif p==target_arr[2]:
            ver_vir[0]+=1
    elif arr[i][4]==target_arr[2]:
        if p==target_arr[0]:
            vir_s[0]+=1
        elif p==target_arr[1]:
            vir_ver[0]+=1
        elif p==target_arr[2]:
            vir_vir[0]+=1
sep_arr=arr_sep_kfold(arr,0*k_len,2*k_len,k_len)
(mean_arr,std_arr)=arr_mean_and_std_kfold(sep_arr,0*k_len,2*k_len,k_len)
#print(len(sep_arr[0]))
for i in range(k_len):
    p=judge_data(arr[k_len+i],sep_arr,2*k_len,mean_arr,std_arr)
    #print(p)
    if arr[k_len+i][4]==target_arr[0]:
        if p==target_arr[0]:
            s_s[1]+=1
        elif p==target_arr[1]:
            s_ver[1]+=1
        elif p==target_arr[2]:
            s_vir[1]+=1
    elif arr[k_len+i][4]==target_arr[1]:
        if p==target_arr[0]:
            ver_s[1]+=1
        elif p==target_arr[1]:
            ver_ver[1]+=1
        elif p==target_arr[2]:
            ver_vir[1]+=1
    elif arr[k_len+i][4]==target_arr[2]:
        if p==target_arr[0]:
            vir_s[1]+=1
        elif p==target_arr[1]:
            vir_ver[1]+=1
        elif p==target_arr[2]:
            vir_vir[1]+=1
sep_arr=arr_sep_kfold(arr,0*k_len,1*k_len,k_len)
(mean_arr,std_arr)=arr_mean_and_std_kfold(sep_arr,0*k_len,1*k_len,k_len)
#print(len(sep_arr[0]))
for i in range(k_len):
    p=judge_data(arr[2*k_len+i],sep_arr,2*k_len,mean_arr,std_arr)
    if arr[2*k_len+i][4]==target_arr[0]:
        if p==target_arr[0]:
            s_s[2]+=1
        elif p==target_arr[1]:
            s_ver[2]+=1
        elif p==target_arr[2]:
            s_vir[2]+=1
    elif arr[2*k_len+i][4]==target_arr[1]:
        if p==target_arr[0]:
            ver_s[2]+=1
        elif p==target_arr[1]:
            ver_ver[2]+=1
        elif p==target_arr[2]:
            ver_vir[2]+=1
    elif arr[2*k_len+i][4]==target_arr[2]:
        if p==target_arr[0]:
            vir_s[2]+=1
        elif p==target_arr[1]:
            vir_ver[2]+=1
        elif p==target_arr[2]:
            vir_vir[2]+=1
#print(s_s)
f_s_s=np.mean(s_s)
f_s_ver=np.mean(s_ver)
f_s_vir=np.mean(s_vir)
f_ver_s=np.mean(ver_s)
f_ver_ver=np.mean(ver_ver)
f_ver_vir=np.mean(ver_vir)
f_vir_s=np.mean(vir_s)
f_vir_ver=np.mean(vir_ver)
f_vir_vir=np.mean(vir_ver)
print('\nconfusion matrix:\n',f_s_s,
f_s_ver,
f_s_vir,'\n',
f_ver_s,
f_ver_ver,
f_ver_vir,'\n',
f_vir_s,
f_vir_ver,
f_vir_vir)
print('\nClassification accuracy:',(f_s_s+f_ver_ver+f_vir_vir)/(len(arr)-(2*k_len)))
print('setosa_sensitivity:',f_s_s/(f_s_s+f_s_ver+f_s_vir))        
print('versicolor_sensitivity:',f_ver_ver/(f_ver_s+f_ver_ver+f_ver_vir))  
print('virginica_sensitivity:',f_vir_vir/(f_vir_s+f_vir_ver+f_vir_vir))
print('setosa_precession:',f_s_s/(f_s_s+f_ver_s+f_vir_s))        
print('versicolor_precession:',f_ver_ver/(f_s_ver+f_ver_ver+f_vir_ver))  
print('virginica_precession:',f_vir_vir/(f_s_vir+f_ver_vir+f_vir_vir))