#!/usr/bin/env python
# coding: utf-8

# In[24]:


import csv

if __name__ == "__main__":
    f = open('2022_Seoul_Temp.csv','r', encoding='cp949')
    data = csv.reader(f)
    header = next(data)
    min = 999
    max = -999
    sum =0
    sum1 =0
    sum2 =0
    count =0
    for row in data : 
        if row[2] == '' or row[3] == '' or row[4] =='':
            continue
        temp = float(row[2])
        temp1 = float(row[3])
        temp2 = float(row[4])
        sum += temp
        sum1 += temp1
        sum2 += temp2
        count +=1
    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print("Average Temperature:",round(sum/count,2),"Celsius")
    print("Average Minimum Temperature:",round(sum1/count,2),"Celsius")
    print("Average Maximum Temperature:",round(sum2/count,2),"Celsius")
    f.close()


# In[ ]:




