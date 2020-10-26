import matplotlib.pyplot as plt
import numpy as np
import math

neurons_num=2
layer_num=2

class neuron_node:
    def __init__(self):
        self.weights=[]
        self.bias=1.0
        self.a_z=None
        self.input=[]
        self.output=-1.0
        self.weight_deriv=[]
        self.sig_deriv=0.0
        self.errfun_deriv=0.0
        self.forward_coefficient=[]
        self.backward_coefficient=[]    

def sigmoid(x):
    return 1.0/(1.0+np.exp(-x))

def sigmoid_deriv(x):
    return sigmoid(x)*(1.0-sigmoid(x))

def erron_fun(out1,truth):
    
    return 1/2*np.power(out1-truth,2)
        

def err_sum(feature_arr,label_arr,network):
    sum=0
    for i in range(len(label_arr)):
        compute_output_and_deriv(feature_arr[i],network)
        #print(feature_arr[i][:])
        #print("label:",label_arr[i],"pos_0",network[-1][0].output)
        sum+=erron_fun(network[-1][0].output,label_arr[i])
    return sum

def compute_output_and_deriv(in_list,network):

    for j in range(len(network[0])):
        for i in range(len(in_list)):
            network[0][j].input[i]=in_list[i]
    
    for i in range(len(network)):
        for j in range(len(network[i])) :
            sum=0
            for k in range(len(network[i][j].weights)):
                sum+=network[i][j].weights[k]*network[i][j].input[k]
            sum+=network[i][j].bias

            network[i][j].output=sigmoid(sum)
            network[i][j].sig_deriv=sigmoid_deriv(sum)

            if (i+1)<len(network):
                for z in range(len(network[i+1])):
                    network[i+1][z].input[j]=network[i][j].output
    return 


def forward_pass(network):

    for index1 in range(len(network)):
        for ind2 in range(len(network[index1])):
            for i in range(len(network[index1][ind2].input)):
                network[index1][ind2].forward_coefficient[i]=network[index1][ind2].input[i]
            network[index1][ind2].forward_coefficient[-1]=1
            
    return

def backward_pass(network,label):
    
    network[1][0].errfun_deriv=network[1][0].output-label
  
    network[0][0].errfun_deriv =network[1][0].errfun_deriv*network[1][0].weights[0]*network[1][0].sig_deriv
    network[0][1].errfun_deriv =network[1][0].errfun_deriv*network[1][0].weights[1]*network[1][0].sig_deriv

    return

def weight_deriv_add(network):

    for i in range(len(network)):
        for j in range(len(network[i])):

            for k in range(len(network[i][j].weights)):
                
                network[i][j].weight_deriv[k] += network[i][j].input[k]*network[i][j].errfun_deriv*network[i][j].sig_deriv
            
            network[i][j].weight_deriv[-1] += network[i][j].errfun_deriv*network[i][j].sig_deriv
    
    return

def update_weight(network,learn_rate):

    for i in range(len(network)):
        for j in range(len(network[i])):
            for k in range(len(network[i][j].weights)):
                network[i][j].weights[k] -= learn_rate*network[i][j].weight_deriv[k]
                #print(network[i][j].weights[k])
            network[i][j].bias -= learn_rate*network[i][j].weight_deriv[-1]

    return

def init_network_weight(network):
    for i in range(len(network)):
        for j in range(len(network[i])):
            for k in range(len(network[i][j].weight_deriv)):
                network[i][j].errfun_deriv=0 
                network[i][j].weight_deriv[k]=0
    return

def backpropagation(feature_arr,network,label_arr,out_err,learn_rate):

    init_network_weight(network)

    for i in range(len(feature_arr)):
        
        compute_output_and_deriv(feature_arr[i],network)
        forward_pass(network)
        backward_pass(network,label_arr[i])
        weight_deriv_add(network)

    update_weight(network,learn_rate)
    #print("output",network[-1][0].output)
    return

def create_layer(neuron_num,input_num):
   
    layer=[]

    for _ in range(neuron_num):
        neuron=neuron_node()
        neuron.bias=1.0
        neuron.sig_deriv=0.0
        for _ in range(input_num):
            neuron.weights.append(0.0)
            neuron.input.append(0.0)
            neuron.weight_deriv.append(0.0)
            neuron.forward_coefficient.append(0.0)
            neuron.backward_coefficient.append(0.0)
        #for bias
        neuron.weight_deriv.append(0.0)
        neuron.forward_coefficient.append(0.0)
        neuron.backward_coefficient.append(0.0)
        #*****
        neuron.errfun_deriv=0.0
        neuron.output= -1.0
        layer.append(neuron)


    return layer

def predict(feature_arr,network):
    result=[]
    for data in feature_arr:
        compute_output_and_deriv(data,network)
        if((network[-1][0].output)<0.5):
            result.append(0)
        else:
            result.append(1)
    return result

#handle data input
fp=open("data.txt","r")
data_arr=[]
line=fp.readline()
while line:
    line=line.strip('\n').split(',')
    data_arr.append(line)
    line=fp.readline()
#print(data_arr[:])
#handle input end

#plot ground truth
pos_x_arr=[float(num[0]) for num in data_arr if num[-1]=='0']
pos_y_arr=[float(num[1]) for num in data_arr if num[-1]=='0']
neg_x_arr=[float(num[0]) for num in data_arr if num[-1]=='1']
neg_y_arr=[float(num[1]) for num in data_arr if num[-1]=='1']
line_x_arr=[num for num in range(1,100)]
line_y_arr=[num for num in range(1,100)]

plt.title("ground truth:")
plt.plot(pos_x_arr,pos_y_arr,'o',color='red')
plt.plot(neg_x_arr,neg_y_arr,'o',color='blue') 
plt.plot(line_x_arr,line_y_arr,color='green')
plt.show()
# ground truth end



#handle neuron layers
# and update the weight
network=[]
network.append( create_layer(2,2))
network.append(create_layer(1,2))

feature_arr=[ [ float(data[0]), float(data[1]) ] for data in data_arr]
label_arr=[ float(data[-1]) for data in data_arr]
output_err=[0,0]
learn_rate=0.02

reord=[]
#backpropagation
for i in range(100002):
    backpropagation(feature_arr,network,label_arr,output_err,learn_rate)
    #print("error sum",err_sum(feature_arr,label_arr,network))
    if  (i%10000)==0 and i>1:
        result_arr=predict(feature_arr,network)
        reord.append(result_arr)
        print('epochs ',i,' loss: ',err_sum(feature_arr,label_arr,network))
   
acc_table=[]
for i in range(len(reord)):
    count=0
    for j in range(len(label_arr)):
        if(reord[i][j]==label_arr[j]):
            count+=1
    print("epochs",((i+1)*10000),'accuracy:',len(label_arr)/count)


pre_pos_x_arr=[]
pre_pos_y_arr=[]
pre_neg_x_arr=[]
pre_neg_y_arr=[]

for i in range(len(result_arr)):
    if(result_arr[i]==0):
        pre_pos_x_arr.append(feature_arr[i][0])
        pre_pos_y_arr.append(feature_arr[i][1])
    else:
        pre_neg_x_arr.append(feature_arr[i][0])
        pre_neg_y_arr.append(feature_arr[i][1])


plt.title("predict result:")
plt.plot(pre_pos_x_arr,pre_pos_y_arr,'o',color='red')
plt.plot(pre_neg_x_arr,pre_neg_y_arr,'o',color='blue') 
plt.plot(line_x_arr,line_y_arr,color='green')
plt.show()
#handle ploting predict result

