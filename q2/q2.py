#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv
if __name__ == "__main__":
    f = open('q2.csv','r', encoding='cp949')
    data = csv.reader(f)
    header = next(data)
    min = 999
    max = -999
    minDate =0
    maxDate =0
    for row in data :
        if row[3] == '' or row[4] =='':
            continue
        tempLow = float(row[3])
        tempHigh = float(row[4])
        subTemp = tempHigh - tempLow
        if min > subTemp:
            min = subTemp
            minDate = row[0]
        if max < subTemp:
            max = subTemp
            maxDate = row[0]
            
    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print("Day with the Largest Temparature Variation:",maxDate)
    print("Maximum Temperature Difference:",round(max,2),"Celsius")
    print("Day with the Smallest Temparature Variation:",minDate)
    print("Minimum Temperature Difference:",round(min,2),"Celsius")
    f.close()


# In[ ]:




