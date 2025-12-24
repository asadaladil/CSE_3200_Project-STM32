import numpy as np
k=[]
a=[]
b=[]
with open("image_array.txt",mode="r") as file:
    file=file.readlines()
    for i in file:
        if len(i.split(' '))==1: #for taking y values
            k.append(int(i))
            a.append(b)
            b=[]
            continue
        temp=[]
        for j in i.split(' '):
            try:
                temp.append(int(j))
            except:
                continue
        b.append(temp)

a=np.array(a)
print(a.shape)