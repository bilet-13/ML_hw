import numpy as np 
import random
import math as ma
K=1
data_num=8124
''' cap_shape,cap_surface cap_color bruises odor gill_attachment gill_spacing gill_size gill_color stalk_shape stalk_root stalk_surface_above_ring
stalk_surface_below_ring  stalk_color_above_ring stalk_color_below_ring veil_type veil_color ring_number  ring_type spore_print_color population habitat'''
d1= ['bell','conical','convex','flat','knobbed','sunken']
d2 = ['fibrous','grooves','scaly','smooth']
d3 = ['brown','buff','cinnamon','gray','green','pink','purple','red','white','yellow']
d4 = ['bruises','no']
d5 = ['almond','anise','creosote','fishy','foul','musty','none','pungent','spicy']
d6 = ['attached','descending','free','notched']
d7 = ['close','crowded','distant']
d8 = ['broad','narrow']
d9 = ['black','brown','buff','chocolate','gray','green','orange','pink','purple','red','white','yellow']
d10= ['enlarging','tapering']
# drop d11= ['bulbous','club','cup','equal', 'rhizomorphs','rooted', 'missing']
d12= ['fibrous','scaly','silky','smooth']
d13= ['fibrous','scaly=y','silky','smooth']
d14= ['brown','buff','cinnamon','gray','orange', 'pink','red','white','yellow']
d15= ['brown','buff','cinnamon','gray','orange', 'pink','red','white','yellow']
d16= ['partial','universal']
d17= ['brown','orange','white','yellow']
d18= ['none','one','two']
d19= ["cobwebby","evanescent","flaring","large=l", "none",'pendant','sheathing','zone']
d20= ["black","brown","buff","chocolate","green", "orange","purple","white","yellow"]
d21= ["abundant","clustered","numerous", "scattered","several","solitary"]
d22=["grasses","leaves","meadows","paths", "urban","waste","woods"]

f1 = ['b','c','f','x','k','s']
f2 = ['f','g','y','s']
f3 = ['n','b','c','g','r','p','u','e','w','y']
f4 = ['t','f']
f5 = ['a','l','c','y','f','m','n','p','s']
f6 = ['a','d','f','n']
f7 = ['c','w','d']
f8 = ['b','n']
f9 = ['k','n','b','h','g','r','o','p','u','e','w','y']
f10 = ['e','t']
#f11 = ['b','c','u','e','z','r','?']
f12=['f','y','k','s']
f13=['f','y','k','s']
f14=['n','b','c','g','o','p','e','w','y']
f15=['n','b','c','g','o','p','e','w','y']
f16=['p','u']
f17=['n','o','w','y']
f18=['n','o','t']
f19=['c','e','f','l','n','p','s','z']
f20=['k','n','b','h','r','o','u','w','y']
f21=['a','c','n','s','v','y']
f22=['g','l','m','p','u','w','d']
droped_num=11
p_e=0
p_p=0
def data_size(data_arr,feature_arr,feature_num,size):
    num1=[]
    num2=[]
    num1_all=0
    num2_all=0
    for i in range(len(feature_arr)):
        num1.append(0)
        num2.append(0)
    for i in range(size):
        for k in range(len(feature_arr)):
            if feature_arr[k]==data_arr[i][feature_num]:
                if data_arr[i][0]=='e':
                    num1[k]+=1
                else:
                    num2[k]+=1
                break
    for i in range(len(feature_arr)):
        num1_all+=num1[i]
        num2_all+=num2[i]
    for i in range(len(feature_arr)):
            num1[i]/=num1_all
            num2[i]/=num2_all
    return num1,num2
#**************** ^^^^ not laplace ^^^^^ ****************VVVVVV laplace VVVVVVV**
def data_size_laplace(data_arr,feature_arr,feature_num,size):
    num1=[]
    num2=[]
    num1_all=0
    num2_all=0
    for i in range(len(feature_arr)):
        num1.append(0)
        num2.append(0)
    for i in range(size):
        for k in range(len(feature_arr)):
            if feature_arr[k]==data_arr[i][feature_num]:
                if data_arr[i][0]=='e':
                    num1[k]+=1
                else:
                    num2[k]+=1
                break
    for i in range(len(feature_arr)):
        num1[i]+=K
        num1_all+=num1[i]
        num2[i]+=K
        num2_all+=num2[i]
    for i in range(len(feature_arr)):
        num1[i]/=num1_all
        num2[i]/=num2_all
    return num1,num2

def data_size_3kfold(data_arr,feature_arr,feature_num,st1,st2,end_num):
    num1=[]
    num2=[]
    num1_all=0
    num2_all=0
    for i in range(len(feature_arr)):
        num1.append(0)
        num2.append(0)
    for i in range(end_num):
        for k in range(len(feature_arr)):
            if feature_arr[k]==data_arr[st1+i][feature_num]:
                if data_arr[st1+i][0]=='e':
                    num1[k]+=1
                else:
                    num2[k]+=1
                break
    for i in range(end_num):
        for k in range(len(feature_arr)):
            if feature_arr[k]==data_arr[st2+i][feature_num]:
                if data_arr[st2+i][0]=='e':
                    num1[k]+=1
                else:
                    num2[k]+=1
                break
    for i in range(len(feature_arr)):
        num1_all+=num1[i]
        num2_all+=num2[i]
    for i in range(len(feature_arr)):
        num1[i]/=num1_all
        num2[i]/=num2_all
    return num1,num2

def data_size_3kfold_laplace(data_arr,feature_arr,feature_num,st1,st2,end_num):
    num1=[]
    num2=[]
    num1_all=0
    num2_all=0
    for i in range(len(feature_arr)):
        num1.append(0)
        num2.append(0)
    for i in range(end_num):
        for k in range(len(feature_arr)):
            if feature_arr[k]==data_arr[st1+i][feature_num]:
                if data_arr[st1+i][0]=='e':
                    num1[k]+=1
                else:
                    num2[k]+=1
                break
    for i in range(end_num):
        for k in range(len(feature_arr)):
            if feature_arr[k]==data_arr[st2+i][feature_num]:
                if data_arr[st2+i][0]=='e':
                    num1[k]+=1
                else:
                    num2[k]+=1
                break
    for i in range(len(feature_arr)):
        num1[i]+=K
        num1_all+=num1[i]
        num2[i]+=K
        num2_all+=num2[i]
    for i in range(len(feature_arr)):
        num1[i]/=num1_all
        num2[i]/=num2_all
    return num1,num2

def probability_arr(data_arr):
    arr=[]
    for i in range(len(f1)):
        if data_arr[1]==f1[i]:
            arr.append(i)
            break
    for i in range(len(f2)):
        if data_arr[2]==f2[i]:
            arr.append(i)
            break
    for i in range(len(f3)):
        if data_arr[3]==f3[i]:
            arr.append(i)
            break
    for i in range(len(f4)):
        if data_arr[4]==f4[i]:
            arr.append(i)
            break
    for i in range(len(f5)):
        if data_arr[5]==f5[i]:
            arr.append(i)
            break
    for i in range(len(f6)):
        if data_arr[6]==f6[i]:
            arr.append(i)
            break
    for i in range(len(f7)):
        if data_arr[7]==f7[i]:
            arr.append(i)
            break
    for i in range(len(f8)):
        if data_arr[8]==f8[i]:
            arr.append(i)
            break
    for i in range(len(f9)):
        if data_arr[9]==f9[i]:
            arr.append(i)
            break
    for i in range(len(f10)):
        if data_arr[10]==f10[i]:
            arr.append(i)
            break
    for i in range(len(f12)):
        if data_arr[12]==f12[i]:
            arr.append(i)
            break
    for i in range(len(f13)):
        if data_arr[13]==f13[i]:
            arr.append(i)
            break
    for i in range(len(f14)):
        if data_arr[14]==f14[i]:
            arr.append(i)
            break
    for i in range(len(f15)):
        if data_arr[15]==f15[i]:
            arr.append(i)
            break
    for i in range(len(f16)):
        if data_arr[16]==f16[i]:
            arr.append(i)
            break
    for i in range(len(f17)):
        if data_arr[17]==f17[i]:
            arr.append(i)
            break
    for i in range(len(f18)):
        if data_arr[18]==f18[i]:
            arr.append(i)
            break
    for i in range(len(f19)):
        if data_arr[19]==f19[i]:
            arr.append(i)
            break
    for i in range(len(f20)):
        if data_arr[20]==f20[i]:
            arr.append(i)
            break
    for i in range(len(f21)):
        if data_arr[21]==f21[i]:
            arr.append(i)
            break
    for i in range(len(f22)):
        if data_arr[22]==f22[i]:
            arr.append(i)
            break
    #print(len(arr))
    return arr
    
def judge_data(data_arr,e_p,ef1,ef2,ef3,ef4,ef5,ef6,ef7,ef8,ef9,
               ef10,ef12,ef13,ef14,ef15,
              ef16,ef17,ef18,ef19,ef20,ef21,ef22,p_p,pf1,pf2,pf3,
              pf4,pf5,pf6,pf7,pf8,pf9,pf10,pf12,pf13,pf14,pf15,pf16,pf17,
              pf18,pf19,pf20,pf21,pf22):
    p_arr=probability_arr(data_arr)
    e=(e_p*ef1[p_arr[0]]*ef2[p_arr[1]]*ef3[p_arr[2]]*ef4[p_arr[3]]
       *ef5[p_arr[4]]*ef6[p_arr[5]]*ef7[p_arr[6]]*ef8[p_arr[7]]
       *ef9[p_arr[8]]*ef10[p_arr[9]]*ef12[p_arr[10]]*ef13[p_arr[11]]
       *ef14[p_arr[12]]*ef15[p_arr[13]]*ef16[p_arr[14]]*ef17[p_arr[15]]
       *ef18[p_arr[16]]*ef19[p_arr[17]]*ef20[p_arr[18]]*ef21[p_arr[19]]
       *ef22[p_arr[20]])
    p=(p_p*pf1[p_arr[0]]*pf2[p_arr[1]]*pf3[p_arr[2]]*pf4[p_arr[3]]
       *pf5[p_arr[4]]*pf6[p_arr[5]]*pf7[p_arr[6]]*pf8[p_arr[7]]
       *pf9[p_arr[8]]*pf10[p_arr[9]]*pf12[p_arr[10]]*pf13[p_arr[11]]
       *pf14[p_arr[12]]*pf15[p_arr[13]]*pf16[p_arr[14]]*pf17[p_arr[15]]
       *pf18[p_arr[16]]*pf19[p_arr[17]]*pf20[p_arr[18]]*pf21[p_arr[19]]
       *pf22[p_arr[20]])
    if e>p:
        return 'e'
    else :
        return 'p'
    
    

#************
fp = open('agaricus-lepiota.data', "r")
data_arr=[]
line = fp.readline()
while line:
    line = line.strip('\n').split(',')  
    data_arr.append(line)
    line = fp.readline()
#print(arr[:]) 
fp.close()
#data_arr=np.delete(arr,11,axis=1)
random.shuffle(data_arr)
np.set_printoptions(threshold=np.inf)
#print(data_arr)
train_num=ma.ceil(8124*0.7)
test_num=8124-train_num
f1_size=data_size(data_arr,f1,1,train_num)
for i in range (6):
    p_e+=f1_size[0][i]
for i in range (6):
    p_p+=f1_size[1][i]
p_e/=train_num
p_p/=train_num
train_num=ma.ceil(8124*0.7)
test_num=8124-train_num
e_f1_arr,p_f1_arr=data_size(data_arr,f1,1,train_num)
e_f2_arr,p_f2_arr=data_size(data_arr,f2,2,train_num)
e_f3_arr,p_f3_arr=data_size(data_arr,f3,3,train_num)
e_f4_arr,p_f4_arr=data_size(data_arr,f4,4,train_num)
e_f5_arr,p_f5_arr=data_size(data_arr,f5,5,train_num)
e_f6_arr,p_f6_arr=data_size(data_arr,f6,6,train_num)
e_f7_arr,p_f7_arr=data_size(data_arr,f7,7,train_num)
e_f8_arr,p_f8_arr=data_size(data_arr,f8,8,train_num)
e_f9_arr,p_f9_arr=data_size(data_arr,f9,9,train_num)
e_f10_arr,p_f10_arr=data_size(data_arr,f10,10,train_num)
e_f12_arr,p_f12_arr=data_size(data_arr,f12,12,train_num)
e_f13_arr,p_f13_arr=data_size(data_arr,f13,13,train_num)
e_f14_arr,p_f14_arr=data_size(data_arr,f14,14,train_num)
e_f15_arr,p_f15_arr=data_size(data_arr,f15,15,train_num)
e_f16_arr,p_f16_arr=data_size(data_arr,f16,16,train_num)
e_f17_arr,p_f17_arr=data_size(data_arr,f17,17,train_num)
e_f18_arr,p_f18_arr=data_size(data_arr,f18,18,train_num)
e_f19_arr,p_f19_arr=data_size(data_arr,f19,19,train_num)
e_f20_arr,p_f20_arr=data_size(data_arr,f20,20,train_num)
e_f21_arr,p_f21_arr=data_size(data_arr,f21,21,train_num)
e_f22_arr,p_f22_arr=data_size(data_arr,f22,22,train_num)

tp=0
fp=0
fn=0
tn=0
for i in range(8124-train_num):
    c=judge_data(data_arr[train_num+i],p_e,e_f1_arr,e_f2_arr,e_f3_arr,e_f4_arr,e_f5_arr,e_f6_arr,e_f7_arr,e_f8_arr,e_f9_arr,
               e_f10_arr,e_f12_arr,e_f13_arr,e_f14_arr,e_f15_arr,
              e_f16_arr,e_f17_arr,e_f18_arr,e_f19_arr,e_f20_arr,e_f21_arr,e_f22_arr,p_p,p_f1_arr,p_f2_arr,p_f3_arr,
              p_f4_arr,p_f5_arr,p_f6_arr,p_f7_arr,p_f8_arr,p_f9_arr,p_f10_arr,p_f12_arr,p_f13_arr,p_f14_arr,p_f15_arr,p_f16_arr,p_f17_arr,
              p_f18_arr,p_f19_arr,p_f20_arr,p_f21_arr,p_f22_arr)
    if c==data_arr[train_num+i][0] and c=='e':
        tp+=1
    elif c==data_arr[train_num+i][0] and c=='p':
        tn+=1
    elif c!=data_arr[train_num+i][0] and c=='e':
        fn+=1
    elif c!=data_arr[train_num+i][0] and c=='p':
        fp+=1
print('Holdout validation without laplace')
print('confusion matrix:\n',tp,fn,'\n',fp,tn)
print('Classification accuracy:',((tp+tn)/(tp+tn+fp+fn)))
print('Sensitivity:',(tp/(tp+fn)))
print('Precision:',(tp/(tp+fp)))
e_f1_arr,p_f1_arr=data_size_laplace(data_arr,f1,1,train_num)
e_f2_arr,p_f2_arr=data_size_laplace(data_arr,f2,2,train_num)
e_f3_arr,p_f3_arr=data_size_laplace(data_arr,f3,3,train_num)
e_f4_arr,p_f4_arr=data_size_laplace(data_arr,f4,4,train_num)
e_f5_arr,p_f5_arr=data_size_laplace(data_arr,f5,5,train_num)
e_f6_arr,p_f6_arr=data_size_laplace(data_arr,f6,6,train_num)
e_f7_arr,p_f7_arr=data_size_laplace(data_arr,f7,7,train_num)
e_f8_arr,p_f8_arr=data_size_laplace(data_arr,f8,8,train_num)
e_f9_arr,p_f9_arr=data_size_laplace(data_arr,f9,9,train_num)
e_f10_arr,p_f10_arr=data_size_laplace(data_arr,f10,10,train_num)
e_f12_arr,p_f12_arr=data_size_laplace(data_arr,f12,12,train_num)
e_f13_arr,p_f13_arr=data_size_laplace(data_arr,f13,13,train_num)
e_f14_arr,p_f14_arr=data_size_laplace(data_arr,f14,14,train_num)
e_f15_arr,p_f15_arr=data_size_laplace(data_arr,f15,15,train_num)
e_f16_arr,p_f16_arr=data_size_laplace(data_arr,f16,16,train_num)
e_f17_arr,p_f17_arr=data_size_laplace(data_arr,f17,17,train_num)
e_f18_arr,p_f18_arr=data_size_laplace(data_arr,f18,18,train_num)
e_f19_arr,p_f19_arr=data_size_laplace(data_arr,f19,19,train_num)
e_f20_arr,p_f20_arr=data_size_laplace(data_arr,f20,20,train_num)
e_f21_arr,p_f21_arr=data_size_laplace(data_arr,f21,21,train_num)
e_f22_arr,p_f22_arr=data_size_laplace(data_arr,f22,22,train_num)
tp=0
fp=0
fn=0
tn=0
for i in range(8124-train_num):
    c=judge_data(data_arr[train_num+i],p_e,e_f1_arr,e_f2_arr,e_f3_arr,e_f4_arr,e_f5_arr,e_f6_arr,e_f7_arr,e_f8_arr,e_f9_arr,
               e_f10_arr,e_f12_arr,e_f13_arr,e_f14_arr,e_f15_arr,
              e_f16_arr,e_f17_arr,e_f18_arr,e_f19_arr,e_f20_arr,e_f21_arr,e_f22_arr,p_p,p_f1_arr,p_f2_arr,p_f3_arr,
              p_f4_arr,p_f5_arr,p_f6_arr,p_f7_arr,p_f8_arr,p_f9_arr,p_f10_arr,p_f12_arr,p_f13_arr,p_f14_arr,p_f15_arr,p_f16_arr,p_f17_arr,
              p_f18_arr,p_f19_arr,p_f20_arr,p_f21_arr,p_f22_arr)
    if c==data_arr[train_num+i][0] and c=='e':
        tp+=1
    elif c==data_arr[train_num+i][0] and c=='p':
        tn+=1
    elif c!=data_arr[train_num+i][0] and c=='e':
        fn+=1
    elif c!=data_arr[train_num+i][0] and c=='p':
        fp+=1
print('\nHoldout validation with laplace')
print('confusion matrix:\n',tp,fn,'\n',fp,tn)
print('Classification accuracy:',((tp+tn)/(tp+tn+fp+fn)))
print('Sensitivity:',(tp/(tp+fn)))
print('Precision:',(tp/(tp+fp)))

k1_acc=0.0
k1_sen=0.0
k1_pre=0.0
e_f1_arr,p_f1_arr=data_size_3kfold(data_arr,f1,1,0,2708,2708)
e_f2_arr,p_f2_arr=data_size_3kfold(data_arr,f2,2,0,2708,2708)
e_f3_arr,p_f3_arr=data_size_3kfold(data_arr,f3,3,0,2708,2708)
e_f4_arr,p_f4_arr=data_size_3kfold(data_arr,f4,4,0,2708,2708)
e_f5_arr,p_f5_arr=data_size_3kfold(data_arr,f5,5,0,2708,2708)
e_f6_arr,p_f6_arr=data_size_3kfold(data_arr,f6,6,0,2708,2708)
e_f7_arr,p_f7_arr=data_size_3kfold(data_arr,f7,7,0,2708,2708)
e_f8_arr,p_f8_arr=data_size_3kfold(data_arr,f8,8,0,2708,2708)
e_f9_arr,p_f9_arr=data_size_3kfold(data_arr,f9,9,0,2708,2708)
e_f10_arr,p_f10_arr=data_size_3kfold(data_arr,f10,10,0,2708,2708)
e_f12_arr,p_f12_arr=data_size_3kfold(data_arr,f12,12,0,2708,2708)
e_f13_arr,p_f13_arr=data_size_3kfold(data_arr,f13,13,0,2708,2708)
e_f14_arr,p_f14_arr=data_size_3kfold(data_arr,f14,14,0,2708,2708)
e_f15_arr,p_f15_arr=data_size_3kfold(data_arr,f15,15,0,2708,2708)
e_f16_arr,p_f16_arr=data_size_3kfold(data_arr,f16,16,0,2708,2708)
e_f17_arr,p_f17_arr=data_size_3kfold(data_arr,f17,17,0,2708,2708)
e_f18_arr,p_f18_arr=data_size_3kfold(data_arr,f18,18,0,2708,2708)
e_f19_arr,p_f19_arr=data_size_3kfold(data_arr,f19,19,0,2708,2708)
e_f20_arr,p_f20_arr=data_size_3kfold(data_arr,f20,20,0,2708,2708)
e_f21_arr,p_f21_arr=data_size_3kfold(data_arr,f21,21,0,2708,2708)
e_f22_arr,p_f22_arr=data_size_3kfold(data_arr,f22,22,0,2708,2708)

tp=0
fp=0
fn=0
tn=0
for i in range(2708):
    c=judge_data(data_arr[2708+2708+i],p_e,e_f1_arr,e_f2_arr,e_f3_arr,e_f4_arr,e_f5_arr,e_f6_arr,e_f7_arr,e_f8_arr,e_f9_arr,
               e_f10_arr,e_f12_arr,e_f13_arr,e_f14_arr,e_f15_arr,
              e_f16_arr,e_f17_arr,e_f18_arr,e_f19_arr,e_f20_arr,e_f21_arr,e_f22_arr,p_p,p_f1_arr,p_f2_arr,p_f3_arr,
              p_f4_arr,p_f5_arr,p_f6_arr,p_f7_arr,p_f8_arr,p_f9_arr,p_f10_arr,p_f12_arr,p_f13_arr,p_f14_arr,p_f15_arr,p_f16_arr,p_f17_arr,
              p_f18_arr,p_f19_arr,p_f20_arr,p_f21_arr,p_f22_arr)
    if c==data_arr[2708+2708+i][0] and c=='e':
        tp+=1
    elif c==data_arr[2708+2708+i][0] and c=='p':
        tn+=1
    elif c!=data_arr[2708+2708+i][0] and c=='e':
        fn+=1
    elif c!=data_arr[2708+2708+i][0] and c=='p':
        fp+=1
k1_tp=tp
k1_fp=fp
k1_fn=fn
k1_tn=tn
#print('\nHoldout validation without laplace')
#print('tp:',tp,'tn:',tn,'fn:',fn,'fp:',fp)
k1_acc=((tp+tn)/(tp+tn+fp+fn))
k1_sen=(tp/(tp+fn))
k1_pre=(tp/(tp+fp))

k2_acc=0.0
k2_sen=0.0
k2_pre=0.0
e_f1_arr,p_f1_arr=data_size_3kfold(data_arr,f1,1,0,5416,2708)
e_f2_arr,p_f2_arr=data_size_3kfold(data_arr,f2,2,0,5416,2708)
e_f3_arr,p_f3_arr=data_size_3kfold(data_arr,f3,3,0,5416,2708)
e_f4_arr,p_f4_arr=data_size_3kfold(data_arr,f4,4,0,5416,2708)
e_f5_arr,p_f5_arr=data_size_3kfold(data_arr,f5,5,0,5416,2708)
e_f6_arr,p_f6_arr=data_size_3kfold(data_arr,f6,6,0,5416,2708)
e_f7_arr,p_f7_arr=data_size_3kfold(data_arr,f7,7,0,5416,2708)
e_f8_arr,p_f8_arr=data_size_3kfold(data_arr,f8,8,0,5416,2708)
e_f9_arr,p_f9_arr=data_size_3kfold(data_arr,f9,9,0,5416,2708)
e_f10_arr,p_f10_arr=data_size_3kfold(data_arr,f10,10,0,5416,2708)
e_f12_arr,p_f12_arr=data_size_3kfold(data_arr,f12,12,0,5416,2708)
e_f13_arr,p_f13_arr=data_size_3kfold(data_arr,f13,13,0,5416,2708)
e_f14_arr,p_f14_arr=data_size_3kfold(data_arr,f14,14,0,5416,2708)
e_f15_arr,p_f15_arr=data_size_3kfold(data_arr,f15,15,0,5416,2708)
e_f16_arr,p_f16_arr=data_size_3kfold(data_arr,f16,16,0,5416,2708)
e_f17_arr,p_f17_arr=data_size_3kfold(data_arr,f17,17,0,5416,2708)
e_f18_arr,p_f18_arr=data_size_3kfold(data_arr,f18,18,0,5416,2708)
e_f19_arr,p_f19_arr=data_size_3kfold(data_arr,f19,19,0,5416,2708)
e_f20_arr,p_f20_arr=data_size_3kfold(data_arr,f20,20,0,5416,2708)
e_f21_arr,p_f21_arr=data_size_3kfold(data_arr,f21,21,0,5416,2708)
e_f22_arr,p_f22_arr=data_size_3kfold(data_arr,f22,22,0,5416,2708)


tp=0
fp=0
fn=0
tn=0
for i in range(2708):
    c=judge_data(data_arr[2708+i],p_e,e_f1_arr,e_f2_arr,e_f3_arr,e_f4_arr,e_f5_arr,e_f6_arr,e_f7_arr,e_f8_arr,e_f9_arr,
               e_f10_arr,e_f12_arr,e_f13_arr,e_f14_arr,e_f15_arr,
              e_f16_arr,e_f17_arr,e_f18_arr,e_f19_arr,e_f20_arr,e_f21_arr,e_f22_arr,p_p,p_f1_arr,p_f2_arr,p_f3_arr,
              p_f4_arr,p_f5_arr,p_f6_arr,p_f7_arr,p_f8_arr,p_f9_arr,p_f10_arr,p_f12_arr,p_f13_arr,p_f14_arr,p_f15_arr,p_f16_arr,p_f17_arr,
              p_f18_arr,p_f19_arr,p_f20_arr,p_f21_arr,p_f22_arr)
    if c==data_arr[2708+i][0] and c=='e':
        tp+=1
    elif c==data_arr[2708+i][0] and c=='p':
        tn+=1
    elif c!=data_arr[2708+i][0] and c=='e':
        fn+=1
    elif c!=data_arr[2708+i][0] and c=='p':
        fp+=1
k2_tp=tp
k2_fp=fp
k2_fn=fn
k2_tn=tn
#print('\nHoldout validation without laplace')
#print('tp:',tp,'tn:',tn,'fn:',fn,'fp:',fp)
k2_acc=((tp+tn)/(tp+tn+fp+fn))
k2_sen=(tp/(tp+fn))
k2_pre=(tp/(tp+fp))

k3_acc=0.0
k3_sen=0.0
k3_pre=0.0
e_f1_arr,p_f1_arr=data_size_3kfold(data_arr,f1,1,2708,5416,2708)
e_f2_arr,p_f2_arr=data_size_3kfold(data_arr,f2,2,2708,5416,2708)
e_f3_arr,p_f3_arr=data_size_3kfold(data_arr,f3,3,2708,5416,2708)
e_f4_arr,p_f4_arr=data_size_3kfold(data_arr,f4,4,2708,5416,2708)
e_f5_arr,p_f5_arr=data_size_3kfold(data_arr,f5,5,2708,5416,2708)
e_f6_arr,p_f6_arr=data_size_3kfold(data_arr,f6,6,2708,5416,2708)
e_f7_arr,p_f7_arr=data_size_3kfold(data_arr,f7,7,2708,5416,2708)
e_f8_arr,p_f8_arr=data_size_3kfold(data_arr,f8,8,2708,5416,2708)
e_f9_arr,p_f9_arr=data_size_3kfold(data_arr,f9,9,2708,5416,2708)
e_f10_arr,p_f10_arr=data_size_3kfold(data_arr,f10,10,2708,5416,2708)
e_f12_arr,p_f12_arr=data_size_3kfold(data_arr,f12,12,2708,5416,2708)
e_f13_arr,p_f13_arr=data_size_3kfold(data_arr,f13,13,2708,5416,2708)
e_f14_arr,p_f14_arr=data_size_3kfold(data_arr,f14,14,2708,5416,2708)
e_f15_arr,p_f15_arr=data_size_3kfold(data_arr,f15,15,2708,5416,2708)
e_f16_arr,p_f16_arr=data_size_3kfold(data_arr,f16,16,2708,5416,2708)
e_f17_arr,p_f17_arr=data_size_3kfold(data_arr,f17,17,2708,5416,2708)
e_f18_arr,p_f18_arr=data_size_3kfold(data_arr,f18,18,2708,5416,2708)
e_f19_arr,p_f19_arr=data_size_3kfold(data_arr,f19,19,2708,5416,2708)
e_f20_arr,p_f20_arr=data_size_3kfold(data_arr,f20,20,2708,5416,2708)
e_f21_arr,p_f21_arr=data_size_3kfold(data_arr,f21,21,2708,5416,2708)
e_f22_arr,p_f22_arr=data_size_3kfold(data_arr,f22,22,2708,5416,2708)

tp=0
fp=0
fn=0
tn=0
for i in range(2708):
    c=judge_data(data_arr[i],p_e,e_f1_arr,e_f2_arr,e_f3_arr,e_f4_arr,e_f5_arr,e_f6_arr,e_f7_arr,e_f8_arr,e_f9_arr,
               e_f10_arr,e_f12_arr,e_f13_arr,e_f14_arr,e_f15_arr,
              e_f16_arr,e_f17_arr,e_f18_arr,e_f19_arr,e_f20_arr,e_f21_arr,e_f22_arr,p_p,p_f1_arr,p_f2_arr,p_f3_arr,
              p_f4_arr,p_f5_arr,p_f6_arr,p_f7_arr,p_f8_arr,p_f9_arr,p_f10_arr,p_f12_arr,p_f13_arr,p_f14_arr,p_f15_arr,p_f16_arr,p_f17_arr,
              p_f18_arr,p_f19_arr,p_f20_arr,p_f21_arr,p_f22_arr)
    if c==data_arr[i][0] and c=='e':
        tp+=1
    elif c==data_arr[i][0] and c=='p':
        tn+=1
    elif c!=data_arr[i][0] and c=='e':
        fn+=1
    elif c!=data_arr[i][0] and c=='p':
        fp+=1
k3_tp=tp
k3_fp=fp
k3_fn=fn
k3_tn=tn
#print('\nHoldout validation without laplace')
#print('tp:',tp,'tn:',tn,'fn:',fn,'fp:',fp)
k3_acc=((tp+tn)/(tp+tn+fp+fn))
k3_sen=(tp/(tp+fn))
k3_pre=(tp/(tp+fp))
print('\nK-fold cross-validation without laplace')
print('confusion matrix:\n',((k1_tp+k2_tp+k3_tp)/3),((k1_fn+k2_fn+k3_fn)/3),'\n',((k1_fp+k2_fp+k3_fp)/3),((k1_tn+k2_tn+k3_tn)/3))
print('Classification accuracy:',(k1_acc+k2_acc+k3_acc)/3)
print('Sensitivity:',(k1_sen+k2_sen+k3_sen)/3)
print('Precision:',(k1_pre+k2_pre+k3_pre)/3)

k1_acc=0.0
k1_sen=0.0
k1_pre=0.0
e_f1_arr,p_f1_arr=data_size_3kfold_laplace(data_arr,f1,1,0,2708,2708)
e_f2_arr,p_f2_arr=data_size_3kfold_laplace(data_arr,f2,2,0,2708,2708)
e_f3_arr,p_f3_arr=data_size_3kfold_laplace(data_arr,f3,3,0,2708,2708)
e_f4_arr,p_f4_arr=data_size_3kfold_laplace(data_arr,f4,4,0,2708,2708)
e_f5_arr,p_f5_arr=data_size_3kfold_laplace(data_arr,f5,5,0,2708,2708)
e_f6_arr,p_f6_arr=data_size_3kfold_laplace(data_arr,f6,6,0,2708,2708)
e_f7_arr,p_f7_arr=data_size_3kfold_laplace(data_arr,f7,7,0,2708,2708)
e_f8_arr,p_f8_arr=data_size_3kfold_laplace(data_arr,f8,8,0,2708,2708)
e_f9_arr,p_f9_arr=data_size_3kfold_laplace(data_arr,f9,9,0,2708,2708)
e_f10_arr,p_f10_arr=data_size_3kfold_laplace(data_arr,f10,10,0,2708,2708)
e_f12_arr,p_f12_arr=data_size_3kfold_laplace(data_arr,f12,12,0,2708,2708)
e_f13_arr,p_f13_arr=data_size_3kfold_laplace(data_arr,f13,13,0,2708,2708)
e_f14_arr,p_f14_arr=data_size_3kfold_laplace(data_arr,f14,14,0,2708,2708)
e_f15_arr,p_f15_arr=data_size_3kfold_laplace(data_arr,f15,15,0,2708,2708)
e_f16_arr,p_f16_arr=data_size_3kfold_laplace(data_arr,f16,16,0,2708,2708)
e_f17_arr,p_f17_arr=data_size_3kfold_laplace(data_arr,f17,17,0,2708,2708)
e_f18_arr,p_f18_arr=data_size_3kfold_laplace(data_arr,f18,18,0,2708,2708)
e_f19_arr,p_f19_arr=data_size_3kfold_laplace(data_arr,f19,19,0,2708,2708)
e_f20_arr,p_f20_arr=data_size_3kfold_laplace(data_arr,f20,20,0,2708,2708)
e_f21_arr,p_f21_arr=data_size_3kfold_laplace(data_arr,f21,21,0,2708,2708)
e_f22_arr,p_f22_arr=data_size_3kfold_laplace(data_arr,f22,22,0,2708,2708)

tp=0
fp=0
fn=0
tn=0
for i in range(2708):
    c=judge_data(data_arr[2708+2708+i],p_e,e_f1_arr,e_f2_arr,e_f3_arr,e_f4_arr,e_f5_arr,e_f6_arr,e_f7_arr,e_f8_arr,e_f9_arr,
               e_f10_arr,e_f12_arr,e_f13_arr,e_f14_arr,e_f15_arr,
              e_f16_arr,e_f17_arr,e_f18_arr,e_f19_arr,e_f20_arr,e_f21_arr,e_f22_arr,p_p,p_f1_arr,p_f2_arr,p_f3_arr,
              p_f4_arr,p_f5_arr,p_f6_arr,p_f7_arr,p_f8_arr,p_f9_arr,p_f10_arr,p_f12_arr,p_f13_arr,p_f14_arr,p_f15_arr,p_f16_arr,p_f17_arr,
              p_f18_arr,p_f19_arr,p_f20_arr,p_f21_arr,p_f22_arr)
    if c==data_arr[2708+2708+i][0] and c=='e':
        tp+=1
    elif c==data_arr[2708+2708+i][0] and c=='p':
        tn+=1
    elif c!=data_arr[2708+2708+i][0] and c=='e':
        fn+=1
    elif c!=data_arr[2708+2708+i][0] and c=='p':
        fp+=1
k1_tp=tp
k1_tn=tn
k1_fp=fp
k1_fn=fn
#print('\nHoldout validation without laplace')
#print('tp:',tp,'tn:',tn,'fn:',fn,'fp:',fp)
k1_acc=((tp+tn)/(tp+tn+fp+fn))
k1_sen=(tp/(tp+fn))
k1_pre=(tp/(tp+fp))

k2_acc=0.0
k2_sen=0.0
k2_pre=0.0
e_f1_arr,p_f1_arr=data_size_3kfold_laplace(data_arr,f1,1,0,5416,2708)
e_f2_arr,p_f2_arr=data_size_3kfold_laplace(data_arr,f2,2,0,5416,2708)
e_f3_arr,p_f3_arr=data_size_3kfold_laplace(data_arr,f3,3,0,5416,2708)
e_f4_arr,p_f4_arr=data_size_3kfold_laplace(data_arr,f4,4,0,5416,2708)
e_f5_arr,p_f5_arr=data_size_3kfold_laplace(data_arr,f5,5,0,5416,2708)
e_f6_arr,p_f6_arr=data_size_3kfold_laplace(data_arr,f6,6,0,5416,2708)
e_f7_arr,p_f7_arr=data_size_3kfold_laplace(data_arr,f7,7,0,5416,2708)
e_f8_arr,p_f8_arr=data_size_3kfold_laplace(data_arr,f8,8,0,5416,2708)
e_f9_arr,p_f9_arr=data_size_3kfold_laplace(data_arr,f9,9,0,5416,2708)
e_f10_arr,p_f10_arr=data_size_3kfold_laplace(data_arr,f10,10,0,5416,2708)
e_f12_arr,p_f12_arr=data_size_3kfold_laplace(data_arr,f12,12,0,5416,2708)
e_f13_arr,p_f13_arr=data_size_3kfold_laplace(data_arr,f13,13,0,5416,2708)
e_f14_arr,p_f14_arr=data_size_3kfold_laplace(data_arr,f14,14,0,5416,2708)
e_f15_arr,p_f15_arr=data_size_3kfold_laplace(data_arr,f15,15,0,5416,2708)
e_f16_arr,p_f16_arr=data_size_3kfold_laplace(data_arr,f16,16,0,5416,2708)
e_f17_arr,p_f17_arr=data_size_3kfold_laplace(data_arr,f17,17,0,5416,2708)
e_f18_arr,p_f18_arr=data_size_3kfold_laplace(data_arr,f18,18,0,5416,2708)
e_f19_arr,p_f19_arr=data_size_3kfold_laplace(data_arr,f19,19,0,5416,2708)
e_f20_arr,p_f20_arr=data_size_3kfold_laplace(data_arr,f20,20,0,5416,2708)
e_f21_arr,p_f21_arr=data_size_3kfold_laplace(data_arr,f21,21,0,5416,2708)
e_f22_arr,p_f22_arr=data_size_3kfold_laplace(data_arr,f22,22,0,5416,2708)

tp=0
fp=0
fn=0
tn=0
for i in range(2708):
    c=judge_data(data_arr[2708+i],p_e,e_f1_arr,e_f2_arr,e_f3_arr,e_f4_arr,e_f5_arr,e_f6_arr,e_f7_arr,e_f8_arr,e_f9_arr,
               e_f10_arr,e_f12_arr,e_f13_arr,e_f14_arr,e_f15_arr,
              e_f16_arr,e_f17_arr,e_f18_arr,e_f19_arr,e_f20_arr,e_f21_arr,e_f22_arr,p_p,p_f1_arr,p_f2_arr,p_f3_arr,
              p_f4_arr,p_f5_arr,p_f6_arr,p_f7_arr,p_f8_arr,p_f9_arr,p_f10_arr,p_f12_arr,p_f13_arr,p_f14_arr,p_f15_arr,p_f16_arr,p_f17_arr,
              p_f18_arr,p_f19_arr,p_f20_arr,p_f21_arr,p_f22_arr)
    if c==data_arr[2708+i][0] and c=='e':
        tp+=1
    elif c==data_arr[2708+i][0] and c=='p':
        tn+=1
    elif c!=data_arr[2708+i][0] and c=='e':
        fn+=1
    elif c!=data_arr[2708+i][0] and c=='p':
        fp+=1
k2_tp=tp
k2_tn=tn
k2_fp=fp
k2_fn=fn
#print('\nHoldout validation without laplace')
#print('tp:',tp,'tn:',tn,'fn:',fn,'fp:',fp)
k2_acc=((tp+tn)/(tp+tn+fp+fn))
k2_sen=(tp/(tp+fn))
k2_pre=(tp/(tp+fp))

k3_acc=0.0
k3_sen=0.0
k3_pre=0.0
e_f1_arr,p_f1_arr=data_size_3kfold_laplace(data_arr,f1,1,2708,5416,2708)
e_f2_arr,p_f2_arr=data_size_3kfold_laplace(data_arr,f2,2,2708,5416,2708)
e_f3_arr,p_f3_arr=data_size_3kfold_laplace(data_arr,f3,3,2708,5416,2708)
e_f4_arr,p_f4_arr=data_size_3kfold_laplace(data_arr,f4,4,2708,5416,2708)
e_f5_arr,p_f5_arr=data_size_3kfold_laplace(data_arr,f5,5,2708,5416,2708)
e_f6_arr,p_f6_arr=data_size_3kfold_laplace(data_arr,f6,6,2708,5416,2708)
e_f7_arr,p_f7_arr=data_size_3kfold_laplace(data_arr,f7,7,2708,5416,2708)
e_f8_arr,p_f8_arr=data_size_3kfold_laplace(data_arr,f8,8,2708,5416,2708)
e_f9_arr,p_f9_arr=data_size_3kfold_laplace(data_arr,f9,9,2708,5416,2708)
e_f10_arr,p_f10_arr=data_size_3kfold_laplace(data_arr,f10,10,2708,5416,2708)
e_f12_arr,p_f12_arr=data_size_3kfold_laplace(data_arr,f12,12,2708,5416,2708)
e_f13_arr,p_f13_arr=data_size_3kfold_laplace(data_arr,f13,13,2708,5416,2708)
e_f14_arr,p_f14_arr=data_size_3kfold_laplace(data_arr,f14,14,2708,5416,2708)
e_f15_arr,p_f15_arr=data_size_3kfold_laplace(data_arr,f15,15,2708,5416,2708)
e_f16_arr,p_f16_arr=data_size_3kfold_laplace(data_arr,f16,16,2708,5416,2708)
e_f17_arr,p_f17_arr=data_size_3kfold_laplace(data_arr,f17,17,2708,5416,2708)
e_f18_arr,p_f18_arr=data_size_3kfold_laplace(data_arr,f18,18,2708,5416,2708)
e_f19_arr,p_f19_arr=data_size_3kfold_laplace(data_arr,f19,19,2708,5416,2708)
e_f20_arr,p_f20_arr=data_size_3kfold_laplace(data_arr,f20,20,2708,5416,2708)
e_f21_arr,p_f21_arr=data_size_3kfold_laplace(data_arr,f21,21,2708,5416,2708)
e_f22_arr,p_f22_arr=data_size_3kfold_laplace(data_arr,f22,22,2708,5416,2708)

tp=0
fp=0
fn=0
tn=0
for i in range(2708):
    c=judge_data(data_arr[i],p_e,e_f1_arr,e_f2_arr,e_f3_arr,e_f4_arr,e_f5_arr,e_f6_arr,e_f7_arr,e_f8_arr,e_f9_arr,
               e_f10_arr,e_f12_arr,e_f13_arr,e_f14_arr,e_f15_arr,
              e_f16_arr,e_f17_arr,e_f18_arr,e_f19_arr,e_f20_arr,e_f21_arr,e_f22_arr,p_p,p_f1_arr,p_f2_arr,p_f3_arr,
              p_f4_arr,p_f5_arr,p_f6_arr,p_f7_arr,p_f8_arr,p_f9_arr,p_f10_arr,p_f12_arr,p_f13_arr,p_f14_arr,p_f15_arr,p_f16_arr,p_f17_arr,
              p_f18_arr,p_f19_arr,p_f20_arr,p_f21_arr,p_f22_arr)
    if c==data_arr[i][0] and c=='e':
        tp+=1
    elif c==data_arr[i][0] and c=='p':
        tn+=1
    elif c!=data_arr[i][0] and c=='e':
        fn+=1
    elif c!=data_arr[i][0] and c=='p':
        fp+=1
k3_tp=tp
k3_tn=tn
k3_fp=fp
k3_fn=fn
#print('\nHoldout validation without laplace')
#print('tp:',tp,'tn:',tn,'fn:',fn,'fp:',fp)
k3_acc=((tp+tn)/(tp+tn+fp+fn))
k3_sen=(tp/(tp+fn))
k3_pre=(tp/(tp+fp))
print('\nK-fold cross-validation with laplace')
print('confusion matrix:\n',((k1_tp+k2_tp+k3_tp)/3),((k1_fn+k2_fn+k3_fn)/3),'\n',((k1_fp+k2_fp+k3_fp)/3),((k1_tn+k2_tn+k3_tn)/3))
print('Classification accuracy:',(k1_acc+k2_acc+k3_acc)/3)
print('Sensitivity:',(k1_sen+k2_sen+k3_sen)/3)
print('Precision:',(k1_pre+k2_pre+k3_pre)/3)