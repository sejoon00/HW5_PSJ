#!/usr/bin/env python
# coding: utf-8

# In[10]:


import csv
f = open('2022_Seoul_Temp.csv','r', encoding='cp949')
data = csv.reader(f)
header = next(data)
min = 999
max = -999
sum =0
count =0
for row in data : 
    temp = float(row[2])
    if min > temp:
        min = temp
    if max < temp:
        max = temp
    sum += temp
    count +=1
average = float(max/count)
print("*** Annual Temperature Report for Seoul in 2022 ***")
print("Average Temperature:",round(average,2),"Celsius")
print("Average Minimum Temperature:",round(min,2),"Celsius")
print("Average Maximum Temperature:",round(max,2),"Celsius")
f.close()


# In[ ]:




