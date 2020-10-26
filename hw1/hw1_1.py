import matplotlib.pyplot as plt
import numpy as np 

#%matplotlib inline

name=['cap_shape','cap_surface','cap_color','bruises','odor','gill_attachment','gill_spacing','gill_size','gill_color','stalk_shape','stalk_root','stalk_surface_above_ring'
,'stalk_surface_below_ring','stalk_color_above_ring','stalk_color_below_ring','veil_type','veil_color','ring_number','ring_type','spore_print_color','population','habitat']

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
d11= ['bulbous','club','cup','equal', 'rhizomorphs','rooted', 'missing']
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
f11 = ['b','c','u','e','z','r','?']
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

def data_size(data_arr,feature_arr,feature_num):
    num1=[]
    num2=[]
    for i in range(len(feature_arr)):
        num1.append(0)
        num2.append(0)
    for i in range(len(data_arr)):
        for k in range(len(feature_arr)):
            if feature_arr[k]==data_arr[i][feature_num]:
                if data_arr[i][0]=='e':
                    num1[k]+=1
                else:
                    num2[k]+=1
                break
    return num1,num2

def data_size_single(data_arr,feature_arr,feature_num):
    num1=[]
    for i in range(len(feature_arr)):
        num1.append(0)
    for i in range(len(data_arr)):
        for k in range(len(feature_arr)):
            if feature_arr[k]==data_arr[i][feature_num]:
                num1[k]+=1
                break
    return num1

def visual_data(data_arr,feature_arr,feature_num,name_arr,ite):
    plt.figure(figsize=(10,8))
    index=np.arange(len(name_arr))
    arr=[]
    for i in range(len(name_arr)):
        arr.append(i)
    num1,num2= data_size(data_arr,feature_arr,feature_num)
    #print(num1,num2)
    plt.bar(index, num1,width=0.2, label = 'edible' )
    for item,num1 in zip(index,num1):
    #print(index)
        x=item-0.25
        plt.text(
            x, 
            num1+1.05, 
            str(num1),
        )
    plt.bar(index+0.2, num2,width=0.2,label = 'poisonous')
  #print(index[:])
    for index,num2 in zip(index,num2):
    #print(index)
        item=index+0.2
        plt.text(
            item, 
            num2+1.20, 
            str(num2),
        )
    #print(arr)
    plt.ylabel("counts")
    plt.xticks(arr,name_arr)  
    plt.title(name[ite])
    plt.legend(prop = {'size':9})
    
def visual_data_single(data_arr,feature_arr,feature_num,name_arr,ite):
    plt.figure(figsize=(10,8))
    index=np.arange(len(name_arr))
    arr=[]
    for i in range(len(name_arr)):
        arr.append(i)
    num1= data_size_single(data_arr,feature_arr,feature_num)
    #print(num1,num2)
    plt.bar(index, num1,width=0.2 )
    for item,num1 in zip(index,num1):
        x=item-0.25
        plt.text(
            x, 
            num1+1.05, 
            str(num1),
        )
    #print(arr)
    plt.ylabel("counts")
    plt.xticks(arr,name_arr)  
    plt.title(name[ite])
    
    
#print(len(arr))
fp = open('agaricus-lepiota.data', "r")
arr=[]
line = fp.readline()
while line:
    line = line.strip('\n').split(',')  
    arr.append(line)
    line = fp.readline()
#print(arr[:]) 
fp.close()
#print(len(arr))
ite2=0
visual_data_single(arr,f1,1,d1,ite2)
ite2+=1
visual_data_single(arr,f2,2,d2,ite2)
ite2+=1
visual_data_single(arr,f3,3,d3,ite2)
ite2+=1

visual_data_single(arr,f4,4,d4,ite2)
ite2+=1

visual_data_single(arr,f5,5,d5,ite2)
ite2+=1

visual_data_single(arr,f6,6,d6,ite2)
ite2+=1

visual_data_single(arr,f7,7,d7,ite2)
ite2+=1

visual_data_single(arr,f8,8,d8,ite2)
ite2+=1

visual_data_single(arr,f9,9,d9,ite2)
ite2+=1

visual_data_single(arr,f10,10,d10,ite2)
ite2+=1

visual_data_single(arr,f11,11,d11,ite2)
ite2+=1

visual_data_single(arr,f12,12,d12,ite2)
ite2+=1

visual_data_single(arr,f13,13,d13,ite2)
ite2+=1

visual_data_single(arr,f14,14,d14,ite2)
ite2+=1

visual_data_single(arr,f15,15,d15,ite2)
ite2+=1

visual_data_single(arr,f16,16,d16,ite2)
ite2+=1

visual_data_single(arr,f17,17,d17,ite2)
ite2+=1

visual_data_single(arr,f18,18,d18,ite2)
ite2+=1

visual_data_single(arr,f19,19,d19,ite2)
ite2+=1

visual_data_single(arr,f20,20,d20,ite2)
ite2+=1

visual_data_single(arr,f21,21,d21,ite2)
ite2+=1

visual_data_single(arr,f22,22,d22,ite2)
#************************************************
ite=0
visual_data(arr,f1,1,d1,ite)
ite+=1
visual_data(arr,f2,2,d2,ite)
ite+=1
visual_data(arr,f3,3,d3,ite)
ite+=1

visual_data(arr,f4,4,d4,ite)
ite+=1

visual_data(arr,f5,5,d5,ite)
ite+=1

visual_data(arr,f6,6,d6,ite)
ite+=1

visual_data(arr,f7,7,d7,ite)
ite+=1

visual_data(arr,f8,8,d8,ite)
ite+=1

visual_data(arr,f9,9,d9,ite)
ite+=1

visual_data(arr,f10,10,d10,ite)
ite+=1

visual_data(arr,f11,11,d11,ite)
ite+=1

visual_data(arr,f12,12,d12,ite)
ite+=1

visual_data(arr,f13,13,d13,ite)
ite+=1

visual_data(arr,f14,14,d14,ite)
ite+=1

visual_data(arr,f15,15,d15,ite)
ite+=1

visual_data(arr,f16,16,d16,ite)
ite+=1

visual_data(arr,f17,17,d17,ite)
ite+=1

visual_data(arr,f18,18,d18,ite)
ite+=1

visual_data(arr,f19,19,d19,ite)
ite+=1

visual_data(arr,f20,20,d20,ite)
ite+=1

visual_data(arr,f21,21,d21,ite)
ite+=1

visual_data(arr,f22,22,d22,ite)



