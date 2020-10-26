{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "confusion matrix:\n",
      " 12 0 0 \n",
      " 0 16 0 \n",
      " 0 1 16\n",
      "\n",
      "Classification accuracy: 0.9777777777777777\n",
      "setosa_sensitivity: 1.0\n",
      "versicolor_sensitivity: 1.0\n",
      "virginica_sensitivity: 0.9411764705882353\n",
      "setosa_precession: 1.0\n",
      "versicolor_precession: 0.9411764705882353\n",
      "virginica_precession: 1.0\n",
      "\n",
      "confusion matrix:\n",
      " 16.666666666666668 0.0 0.0 \n",
      " 0.0 15.666666666666666 1.0 \n",
      " 0.0 1.3333333333333333 1.3333333333333333\n",
      "\n",
      "Classification accuracy: 0.6733333333333335\n",
      "setosa_sensitivity: 1.0\n",
      "versicolor_sensitivity: 0.9400000000000001\n",
      "virginica_sensitivity: 0.5\n",
      "setosa_precession: 1.0\n",
      "versicolor_precession: 0.9215686274509803\n",
      "virginica_precession: 0.5714285714285715\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import random\n",
    "import math\n",
    "PI=3.14159\n",
    "target_arr=['Iris-setosa','Iris-versicolor','Iris-virginica']\n",
    "attribute_num=4\n",
    "def arr_sep(l,data_arr):\n",
    "    num=[]\n",
    "    num.append([])\n",
    "    num.append([])\n",
    "    num.append([])\n",
    "    for i in range(l):\n",
    "        for k in range(len(target_arr)):\n",
    "            if data_arr[i][4]==target_arr[k]:\n",
    "                num[k].append(data_arr[i])\n",
    "                break\n",
    "    return num\n",
    "def arr_mean_and_std(data_arr):\n",
    "    mean_arr=[]\n",
    "    for i in range(len(target_arr)):\n",
    "        mean_arr.append([])\n",
    "    std_arr=[]\n",
    "    for i in range(len(target_arr)):\n",
    "        std_arr.append([])\n",
    "    arr=[]\n",
    "    for i in range(len(target_arr)):\n",
    "        for j in range(attribute_num):\n",
    "            for k in range(len(data_arr[i])):\n",
    "                arr.append(float(data_arr[i][k][j]))\n",
    "            mean_arr[i].append(np.mean(arr))\n",
    "            std_arr[i].append(np.std(arr))\n",
    "            arr.clear()\n",
    "    return mean_arr ,std_arr\n",
    "'''def arr_sep(l,data_arr):\n",
    "    num=[]\n",
    "    num.append([])\n",
    "    num.append([])\n",
    "    num.append([])\n",
    "    for i in range(l):\n",
    "        for k in range(len(target_arr)):\n",
    "            if data_arr[i][4]==target_arr[k]:\n",
    "                num[k].append(data_arr[i])\n",
    "                break\n",
    "    return num'''\n",
    "def arr_sep_kfold(data_arr,st1,st2,end):\n",
    "    num=[]\n",
    "    num.append([])\n",
    "    num.append([])\n",
    "    num.append([])\n",
    "    for i in range(end):\n",
    "        for k in range(len(target_arr)):\n",
    "            if data_arr[st1+i][4]==target_arr[k]:\n",
    "                num[k].append(data_arr[st1+i])\n",
    "                break\n",
    "    for i in range(end):\n",
    "        for k in range(len(target_arr)):\n",
    "            if data_arr[st2+i][4]==target_arr[k]:\n",
    "                num[k].append(data_arr[st2+i])\n",
    "                break\n",
    "    return num\n",
    "def arr_mean_and_std_kfold(data_arr,st1,st2,end):\n",
    "    mean_arr=[]\n",
    "    for i in range(len(target_arr)):\n",
    "        mean_arr.append([])\n",
    "    std_arr=[]\n",
    "    for i in range(len(target_arr)):\n",
    "        std_arr.append([])\n",
    "    arr=[]\n",
    "    for i in range(len(target_arr)):\n",
    "        for j in range(attribute_num):\n",
    "            for k in range(len(data_arr[i])):\n",
    "                arr.append(float(data_arr[i][k][j]))\n",
    "            mean_arr[i].append(np.mean(arr))\n",
    "            std_arr[i].append(np.std(arr))\n",
    "            arr.clear()\n",
    "    return mean_arr ,std_arr\n",
    "\n",
    "def judge_data(data_arr,sep_arr,train_num,mean_arr,std_arr):\n",
    "    p_seto=len(sep_arr[0])/train_num\n",
    "    p_vers=len(sep_arr[1])/train_num\n",
    "    p_virg=len(sep_arr[2])/train_num\n",
    "    for i in range(attribute_num):\n",
    "        x=float(data_arr[i])\n",
    "        p_seto+=math.log(math.exp(-math.pow(x-mean_arr[0][i],2)/(2*(std_arr[0][i]**2)))/(std_arr[0][i]*math.sqrt(2)*PI))\n",
    "    for i in range(attribute_num):\n",
    "        x=float(data_arr[i])\n",
    "        p_vers+=math.log(math.exp(-math.pow(x-mean_arr[1][i],2)/(2*(std_arr[1][i]**2)))/(std_arr[1][i]*math.sqrt(2)*PI))\n",
    "    for i in range(attribute_num):\n",
    "        x=float(data_arr[i])\n",
    "        p_virg+=math.log(math.exp(-math.pow(x-mean_arr[2][i],2)/(2*(std_arr[2][i]**2)))/(std_arr[2][i]*math.sqrt(2)*PI))\n",
    "    if p_seto>p_vers:\n",
    "        if p_seto>p_virg:\n",
    "            return target_arr[0]\n",
    "        else:\n",
    "            return target_arr[2]\n",
    "    else:\n",
    "        if p_vers>p_virg:\n",
    "            return target_arr[1]\n",
    "        else:\n",
    "            return target_arr[2]\n",
    "fp = open('bezdekIris.data', \"r\")\n",
    "arr=[]\n",
    "line = fp.readline()\n",
    "while line:\n",
    "    line = line.strip('\\n').split(',')  \n",
    "    arr.append(line)\n",
    "    line = fp.readline()\n",
    "#print(arr[:]) \n",
    "fp.close()\n",
    "random.shuffle(arr)\n",
    "#print(len(arr))\n",
    "#print(arr[:])\n",
    "train_len=math.ceil(len(arr)*0.7)\n",
    " \n",
    "s_s=0\n",
    "s_ver=0\n",
    "s_vir=0\n",
    "ver_s=0\n",
    "ver_ver=0\n",
    "ver_vir=0\n",
    "vir_s=0\n",
    "vir_ver=0\n",
    "vir_vir=0\n",
    "sep_arr=arr_sep(train_len,arr)\n",
    "(mean_arr,std_arr)=arr_mean_and_std(sep_arr)\n",
    "#print(len(sep_arr[0]))\n",
    "for i in range(len(arr)-train_len):\n",
    "    p=judge_data(arr[train_len+i],sep_arr,len(arr)-train_len,mean_arr,std_arr)\n",
    "    if arr[train_len+i][4]==target_arr[0]:\n",
    "        if p==target_arr[0]:\n",
    "            s_s+=1\n",
    "        elif p==target_arr[1]:\n",
    "            s_ver+=1\n",
    "        elif p==target_arr[2]:\n",
    "            s_vir+=1\n",
    "    elif arr[train_len+i][4]==target_arr[1]:\n",
    "        if p==target_arr[0]:\n",
    "            ver_s+=1\n",
    "        elif p==target_arr[1]:\n",
    "            ver_ver+=1\n",
    "        elif p==target_arr[2]:\n",
    "            ver_vir+=1\n",
    "    elif arr[train_len+i][4]==target_arr[2]:\n",
    "        if p==target_arr[0]:\n",
    "            vir_s+=1\n",
    "        elif p==target_arr[1]:\n",
    "            vir_ver+=1\n",
    "        elif p==target_arr[2]:\n",
    "            vir_vir+=1\n",
    "print('confusion matrix:\\n',s_s,\n",
    "s_ver,\n",
    "s_vir,'\\n',\n",
    "ver_s,\n",
    "ver_ver,\n",
    "ver_vir,'\\n',\n",
    "vir_s,\n",
    "vir_ver,\n",
    "vir_vir)\n",
    "print('\\nClassification accuracy:',(s_s+ver_ver+vir_vir)/(len(arr)-train_len))\n",
    "print('setosa_sensitivity:',s_s/(s_s+s_ver+s_vir))        \n",
    "print('versicolor_sensitivity:',ver_ver/(ver_s+ver_ver+ver_vir))  \n",
    "print('virginica_sensitivity:',vir_vir/(vir_s+vir_ver+vir_vir))\n",
    "print('setosa_precession:',s_s/(s_s+ver_s+vir_s))        \n",
    "print('versicolor_precession:',ver_ver/(s_ver+ver_ver+vir_ver))  \n",
    "print('virginica_precession:',vir_vir/(s_vir+ver_vir+vir_vir))\n",
    "random.shuffle(arr)\n",
    "k_len=math.ceil(len(arr)/3)\n",
    "#print(k_len)\n",
    "s_s=[0,0,0]\n",
    "s_ver=[0,0,0]\n",
    "s_vir=[0,0,0]\n",
    "ver_s=[0,0,0]\n",
    "ver_ver=[0,0,0]\n",
    "ver_vir=[0,0,0]\n",
    "vir_s=[0,0,0]\n",
    "vir_ver=[0,0,0]\n",
    "vir_vir=[0,0,0]\n",
    "sep_arr=arr_sep_kfold(arr,1*k_len,2*k_len,k_len)\n",
    "(mean_arr,std_arr)=arr_mean_and_std_kfold(sep_arr,1*k_len,2*k_len,k_len)\n",
    "#print(mean_arr[:],std_arr[:])\n",
    "for i in range(k_len):\n",
    "    p=judge_data(arr[i],sep_arr,2*k_len,mean_arr,std_arr)\n",
    "    if arr[i][4]==target_arr[0]:\n",
    "        if p==target_arr[0]:\n",
    "            s_s[0]+=1\n",
    "        elif p==target_arr[1]:\n",
    "            s_ver[0]+=1\n",
    "        elif p==target_arr[2]:\n",
    "            s_vir[0]+=1\n",
    "    elif arr[i][4]==target_arr[1]:\n",
    "        if p==target_arr[0]:\n",
    "            ver_s[0]+=1\n",
    "        elif p==target_arr[1]:\n",
    "            ver_ver[0]+=1\n",
    "        elif p==target_arr[2]:\n",
    "            ver_vir[0]+=1\n",
    "    elif arr[i][4]==target_arr[2]:\n",
    "        if p==target_arr[0]:\n",
    "            vir_s[0]+=1\n",
    "        elif p==target_arr[1]:\n",
    "            vir_ver[0]+=1\n",
    "        elif p==target_arr[2]:\n",
    "            vir_vir[0]+=1\n",
    "sep_arr=arr_sep_kfold(arr,0*k_len,2*k_len,k_len)\n",
    "(mean_arr,std_arr)=arr_mean_and_std_kfold(sep_arr,0*k_len,2*k_len,k_len)\n",
    "#print(len(sep_arr[0]))\n",
    "for i in range(k_len):\n",
    "    p=judge_data(arr[k_len+i],sep_arr,2*k_len,mean_arr,std_arr)\n",
    "    #print(p)\n",
    "    if arr[k_len+i][4]==target_arr[0]:\n",
    "        if p==target_arr[0]:\n",
    "            s_s[1]+=1\n",
    "        elif p==target_arr[1]:\n",
    "            s_ver[1]+=1\n",
    "        elif p==target_arr[2]:\n",
    "            s_vir[1]+=1\n",
    "    elif arr[k_len+i][4]==target_arr[1]:\n",
    "        if p==target_arr[0]:\n",
    "            ver_s[1]+=1\n",
    "        elif p==target_arr[1]:\n",
    "            ver_ver[1]+=1\n",
    "        elif p==target_arr[2]:\n",
    "            ver_vir[1]+=1\n",
    "    elif arr[k_len+i][4]==target_arr[2]:\n",
    "        if p==target_arr[0]:\n",
    "            vir_s[1]+=1\n",
    "        elif p==target_arr[1]:\n",
    "            vir_ver[1]+=1\n",
    "        elif p==target_arr[2]:\n",
    "            vir_vir[1]+=1\n",
    "sep_arr=arr_sep_kfold(arr,0*k_len,1*k_len,k_len)\n",
    "(mean_arr,std_arr)=arr_mean_and_std_kfold(sep_arr,0*k_len,1*k_len,k_len)\n",
    "#print(len(sep_arr[0]))\n",
    "for i in range(k_len):\n",
    "    p=judge_data(arr[2*k_len+i],sep_arr,2*k_len,mean_arr,std_arr)\n",
    "    if arr[2*k_len+i][4]==target_arr[0]:\n",
    "        if p==target_arr[0]:\n",
    "            s_s[2]+=1\n",
    "        elif p==target_arr[1]:\n",
    "            s_ver[2]+=1\n",
    "        elif p==target_arr[2]:\n",
    "            s_vir[2]+=1\n",
    "    elif arr[2*k_len+i][4]==target_arr[1]:\n",
    "        if p==target_arr[0]:\n",
    "            ver_s[2]+=1\n",
    "        elif p==target_arr[1]:\n",
    "            ver_ver[2]+=1\n",
    "        elif p==target_arr[2]:\n",
    "            ver_vir[2]+=1\n",
    "    elif arr[2*k_len+i][4]==target_arr[2]:\n",
    "        if p==target_arr[0]:\n",
    "            vir_s[2]+=1\n",
    "        elif p==target_arr[1]:\n",
    "            vir_ver[2]+=1\n",
    "        elif p==target_arr[2]:\n",
    "            vir_vir[2]+=1\n",
    "#print(s_s)\n",
    "f_s_s=np.mean(s_s)\n",
    "f_s_ver=np.mean(s_ver)\n",
    "f_s_vir=np.mean(s_vir)\n",
    "f_ver_s=np.mean(ver_s)\n",
    "f_ver_ver=np.mean(ver_ver)\n",
    "f_ver_vir=np.mean(ver_vir)\n",
    "f_vir_s=np.mean(vir_s)\n",
    "f_vir_ver=np.mean(vir_ver)\n",
    "f_vir_vir=np.mean(vir_ver)\n",
    "print('\\nconfusion matrix:\\n',f_s_s,\n",
    "f_s_ver,\n",
    "f_s_vir,'\\n',\n",
    "f_ver_s,\n",
    "f_ver_ver,\n",
    "f_ver_vir,'\\n',\n",
    "f_vir_s,\n",
    "f_vir_ver,\n",
    "f_vir_vir)\n",
    "print('\\nClassification accuracy:',(f_s_s+f_ver_ver+f_vir_vir)/(len(arr)-(2*k_len)))\n",
    "print('setosa_sensitivity:',f_s_s/(f_s_s+f_s_ver+f_s_vir))        \n",
    "print('versicolor_sensitivity:',f_ver_ver/(f_ver_s+f_ver_ver+f_ver_vir))  \n",
    "print('virginica_sensitivity:',f_vir_vir/(f_vir_s+f_vir_ver+f_vir_vir))\n",
    "print('setosa_precession:',f_s_s/(f_s_s+f_ver_s+f_vir_s))        \n",
    "print('versicolor_precession:',f_ver_ver/(f_s_ver+f_ver_ver+f_vir_ver))  \n",
    "print('virginica_precession:',f_vir_vir/(f_s_vir+f_ver_vir+f_vir_vir))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
