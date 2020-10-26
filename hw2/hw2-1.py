import csv
import numpy as np
import pandas as pd
import math
import operator
import random
feature_arr=['age','workclass','fnlwgt','education','education-num',
            'marital-status','occupation','relationship','race','sex',
            'capital-gain','capital-loss','hours-per-week','native-country']
input_type=['Id','age','workclass','fnlwgt','education','education-num',
            'marital-status','occupation','relationship','race','sex',
            'capital-gain','capital-loss','hours-per-week','native-country']
feature_continus_discrete_arr=['c','d','c','d','c','d','d','d','d','d','c','c','c','d']
data_type=['Id','age','workclass','fnlwgt','education','education-num',
            'marital-status','occupation','relationship','race','sex',
            'capital-gain','capital-loss','hours-per-week','native-country',
            'Category']

continue_feature_threshold={'age':37,'fnlwgt':178233,'education-num':10,'capital-gain':0,'capital-loss':0,'hours-per-week':40}
#判斷標準 中位數

answer_arr=['Id','Category']
class Node(object):
    def __init__(self,attribute,threshold):
        self.attr = attribute
        self.thres = threshold
        self.left = None
        self.right = None
        self.leaf = False
        self.predict = None
def trans_continue_to_bounding(data_arr,n):
     for i in range(1,len(feature_arr)+1):
        if feature_continus_discrete_arr[i-1]=='d':
            continue
        values=[int(row[i]) for row in data_arr]
        values.sort()
        size,rem=div_list_num(values,n)
        start=0
        end=size
        for row in data_arr:
            for j in range(n):
                start=j*size
                end=start+size-1
                if j==(n-1):
                    end+=rem
                if int(row[i]) >= values[start] and  int(row[i]) <=values[end]:
                    row[i]=str(j)
                
                    
               
                    


def div_list_num(values,n):
    size=0
    size+=math.floor(len(values)/n)
    rem=len(values)-size*n
    while rem > n:
        size+=math.floor(rem/n)
        rem=len(values)-size*n
    return size,rem


def trans_string_to_codestring(data_arr):
    for i in range(1,len(feature_arr)+1):
        if feature_continus_discrete_arr[i-1]=='c':
            continue
        codedict={}
        num=0
        for row in range(len(data_arr)):
            if data_arr[row][i] not in codedict.keys():
                codedict[data_arr[row][i]]=num
                num+=1
            data_arr[row][i]=str(codedict[data_arr[row][i]])
    
def compute_entropy(data_arr):
    arr_len=len(data_arr)
    labelcount={}
    for row in data_arr:
        tmp_category=row[-1]
        if tmp_category not in labelcount.keys():
            labelcount[tmp_category]=0
        labelcount[tmp_category]+=1
    entro=0
    #print(labelcount)
    for key in labelcount:
        pro=float(labelcount[key])/arr_len
        entro -=pro*math.log(pro,2)
    return entro
def find_most_category(classlist):
    classcount={}
    for vote in classlist:
        if vote not in classcount.keys():
            classcount[vote]=0
        classcount[vote]+=1
    sortedlist= sorted(classcount.items(),key=operator.itemgetter(1),reverse=True)
    #print(type(sortedlist))
    return sortedlist[0][0]
def choose_thres(data_arr,attribute):
    if(feature_continus_discrete_arr[attribute-1]=='d'):
        values=[float(row[attribute]) for row in data_arr]
        values=set(values)
        values=list(values)
        values.sort()
        max_ig=float("-inf")
        thres_val=0
        for i in range(0,len(values)-1):
            thres=(values[i]+values[i+1])/2
            ig=info_gain(data_arr,attribute,thres)
            if ig>max_ig:
                max_ig=ig
                thres_val=thres
        return thres_val
    else:
        values=[float(row[attribute]) for row in data_arr]
        return np.median(values)

def info_gain(data_arr,attr,threshold):
    sub1=[row for row in data_arr if float(row[attr])<=threshold]
    #print("sub1len:",len(sub1))
    sub2=[row for row in data_arr if float(row[attr])>threshold]
    #print("sub2len:",len(sub2))
    ig=compute_entropy(data_arr)-remainder(data_arr,[sub1 ,sub2])
    return ig

def remainder(data_arr,data_subsets):
        num=len(data_arr)
        rem=float(0)
        for sub in data_subsets:
            rem += float(len(sub)/num)*compute_entropy(sub)
        return rem
def choose_attr(data_arr):
    max_info_gain=float('-inf')
    best_attr=None
    threshold=0
    for attr in range(1,len(feature_arr)+1 ):
        thres=choose_thres(data_arr,attr)
    ig = info_gain(data_arr,attr,thres)
    if ig > max_info_gain:
        max_info_gain=ig
        best_attr=attr
        threshold=thres
    return best_attr,threshold
def create_tree(data_arr):
    #print("now arrlen:",len(data_arr))
    classlist=[row[-1] for row in data_arr]
    if classlist.count(classlist[0])==len(classlist):
        leaf = Node(None,None)
        leaf.leaf=True
        leaf.predict=classlist[0]
        return leaf
    best_attr,threshold = choose_attr(data_arr)
    attrlist=[row[best_attr] for row in data_arr ]
    if attrlist.count(attrlist[0])==len(attrlist):
        leaf = Node(None,None)
        leaf.leaf=True
        f=classlist.count('0')
        t=classlist.count('1')
        if t>f:
            leaf.predict='1'
        else:
            leaf.predict='0'
        return leaf
    #print("choose success")
    tree=Node(best_attr,threshold)
    sub1=[row for row in data_arr if float(row[best_attr]) <= threshold]
    sub2=[row for row in data_arr if float(row[best_attr]) > threshold]
    #print("sub1len:",len(sub1))
    #print("sub2len:",len(sub2))
    #print("attribute:",feature_arr[best_attr-1],'threshold:',threshold)
    tree.left = create_tree(sub1)
    tree.right = create_tree(sub2)
    return tree
def printtree(root,level):
    if root.leaf:
        print("root.predict:",root.predict)
    else:
        print("attr:",feature_arr[root.attr-1],"threshold:",root.thres)
    if root.left:
        printtree(root.left,level+1)
    if root.right:
        printtree(root.right,level+1)
def predict(node,row_data,time):
    if node.leaf:
        if time<=10:
            print("in the leaf the prediction is:",node.predict)
        return node.predict
    if float(row_data[node.attr]) <= node.thres:
        if time<=10:
            print("attribe:",feature_arr[node.attr-1],"the value<=thres",node.thres,"go to left node")
        return predict(node.left,row_data,time)
    elif float(row_data[node.attr]) > node.thres:
        if time<=10:
            print("attribe:",feature_arr[node.attr-1],"the value>=thres",node.thres,"go to right node")
        return predict(node.right,row_data,time)
def print_result(tp,fp,fn,tn):
    print("confusion matrix\ntrue positive:",tp,' false positive:',fp,
    "\nfalse negative:",fn,'true negative:',tn)
    print('Accuracy:',(tp+tn)/(tp+tn+fp+fn))
    print('Precision:',tp/(tp+fp))
    print('Recall:',tp/(tp+fn))
    
def predict_and_handle_result(root,test_arr):
    tp=0
    fp=0
    fn=0
    tn=0
    time=0
    for row in test_arr:
        time+=1
        result=predict(root,row,time)
        if result == row[-1] and result=='0':
            tp+=1
        elif result == row[-1] and result=='1':
            tn+=1
        elif result != row[-1] and result=='1':
            fn+=1
        elif result != row[-1] and result=='0':
            fp+=1
    return tp,fp,fn,tn
def create_forest(data_arr,quantity,sub_data_size):
    forest=[]
    for i in range(quantity):
        sub_arr=random.sample(data_arr,sub_data_size)
        forest.append(create_tree(sub_arr))
    return forest
def forest_predict(forest,row):
    p=0
    n=0
    for tree in forest:
        result=predict(tree,row,20)
        if result=='0':
            p+=1
        elif result=='1':
            n+=1
    if p>n:
        return '0'
    else:
        return '1'
        
def handle_forest_predict(forest,test_arr):
    tp=0
    fp=0
    fn=0
    tn=0
    for row in test_arr:
        result=forest_predict(forest,row)
        if result == row[-1] and result=='0':
            tp+=1
        elif result == row[-1] and result=='1':
            tn+=1
        elif result != row[-1] and result=='1':
            fn+=1
        elif result != row[-1] and result=='0':
            fp+=1
    return tp,fp,fn,tn  



fp=open('X_train.csv','r',newline='')
xtestdict=csv.DictReader(fp)
f=open('Y_train.csv','r',newline='')
ytestdict=csv.DictReader(f)
#create 2d array ,include feature and outcome
data_arr=[]
row_len=0
#******
for row in xtestdict:
    data_arr.append([])
    for i in range(len(input_type)):
        data_arr[row_len].append(row[input_type[i]])
    row_len+=1
row_len=0
for row in ytestdict:
    data_arr[row_len].append(row[data_type[-1]]) #add category
    row_len+=1
f.close()
fp.close()
#**************************************
#data preprocessing staryt!!!!!!!!!!!!!!!!!!

#shuffle data
np.random.shuffle(data_arr)

#delete miss value
arr_len=0
while arr_len<len(data_arr):
    a=0
    a=data_arr[arr_len].count(' ?')
    arr_len+=1
    if a>0:
        arr_len-=1
        del data_arr[arr_len]

#modified discrete data
trans_string_to_codestring(data_arr)

#modified continue date
trans_continue_to_bounding(data_arr,15)

#data preprocessinjg end!!!!!!!!!!!!!!!!!!!!!!!!!
#*****************************
#use holdout validation
test_num=math.floor(len(data_arr)*0.3)
data_num=len(data_arr)-test_num
test_arr=data_arr[:test_num]
holdout_arr=data_arr[test_num:]
#create tree
tp=0
fp=0
fn=0
tn=0

holdout_root = create_tree(holdout_arr)
tp,fp,fn,tn=predict_and_handle_result(holdout_root,test_arr)
print("decision tree with holdout validation result:")    
print_result(tp,fp,fn,tn)

#use random forest
holdout_forest=create_forest(holdout_arr,1000,20)
tp,fp,fn,tn=handle_forest_predict(holdout_forest,test_arr)
print("\nndom forest has2000 tree with 50 datas with holdout validation result:")    
print_result(tp,fp,fn,tn)


#use k-fold cross-validation
test_num=math.floor(len(data_arr)/3)
k1_test_arr=data_arr[:test_num]
k1_data_arr=data_arr[test_num:]
k2_test_arr=data_arr[test_num:test_num*2]
k2_1=data_arr[:test_num]
k2_2=data_arr[test_num*2:]
k2_data_arr=k2_1+k2_2
k3_test_arr=data_arr[test_num*2:]
k3_data_arr=data_arr[:test_num*2]

k1_root=create_tree(k1_data_arr)
k1_tp,k1_fp,k1_fn,k1_tn=predict_and_handle_result(k1_root,test_arr)
k2_root=create_tree(k2_data_arr)
k2_tp,k2_fp,k2_fn,k2_tn=predict_and_handle_result(k2_root,test_arr)
k3_root=create_tree(k3_data_arr)
k3_tp,k3_fp,k3_fn,k3_tn=predict_and_handle_result(k3_root,test_arr)
f_tp=(k1_tp+k2_tp+k3_tp)/3
f_fp=(k1_fp+k2_fp+k3_fp)/3
f_fn=(k1_fn+k2_fn+k3_fn)/3
f_tn=(k1_tn+k2_tn+k3_tn)/3
print("\ndecision tree with k-fold result:")
print_result(f_tp,f_fp,f_fn,f_tn)
k1_forest=create_forest(k1_data_arr,700,20)
k1_tp,k1_fp,k1_fn,k1_tn=handle_forest_predict(k1_forest,k1_test_arr)
k2_forest=create_forest(k2_data_arr,700,20)
k2_tp,k2_fp,k2_fn,k2_tn=handle_forest_predict(k2_forest,k2_test_arr)
k3_forest=create_forest(k3_data_arr,700,10)
k3_tp,k3_fp,k3_fn,k3_tn=handle_forest_predict(k3_forest,k3_test_arr)
f_tp=(k1_tp+k2_tp+k3_tp)/3
f_fp=(k1_fp+k2_fp+k3_fp)/3
f_fn=(k1_fn+k2_fn+k3_fn)/3
f_tn=(k1_tn+k2_tn+k3_tn)/3
print("\nndom forest has2000 tree with 50 datas with k-fold validation result:")    
print_result(f_tp,f_fp,f_fn,f_tn)

print("end")
filep=open('X_test.csv','r',newline='')
xtest=csv.DictReader(filep)
#create 2d array ,include feature and outcome
test_data_arr=[]
row_len=0
#******
for row in xtest:
    test_data_arr.append([])
    for i in range(len(input_type)):
        test_data_arr[row_len].append(row[input_type[i]])
    row_len+=1
row_len=0
wfp=open('Y_test.csv','w',newline='')
writer=csv.writer(wfp)
writer.writerow(['Id','Category'])

#modified discrete data
trans_string_to_codestring(test_data_arr)

#modified continue date
trans_continue_to_bounding(test_data_arr,15)
time=20
pre_root=create_tree(data_arr)
for row in test_data_arr:
    #print(row[0])
    result=predict(pre_root,row,time)
    writer.writerow([row[0],result])
        
        

