#!/usr/bin/env python
# coding: utf-8

# In[19]:


import csv
if __name__ == "__main__":
    f = open('202303_Seoul_Subway.csv','r', encoding='UTF-8')
    data = csv.reader(f)
    header = next(data)
    curLineNum = 0
    print("*** Subway Report for Seoul on March 2023 ***")
    max =0
    maxStation = ''
    min = 9999999999999
    minStation = ''
    for row in data :
        lineName = row[1]
        
        if(lineName[0] <='5' and lineName[0] >= '1'):
            if(lineName[0] >'4'):
                break;
            lineNum = int(lineName[0])
            if curLineNum != lineNum and curLineNum !=0:
                print("Line ",curLineNum,":")
                print("Busiest Station",maxStation,"(",max,")")
                print("Least Station",minStation,"(",min,")")
                max =0
                min =9999999999999
                curLineNum = lineNum
            else:
                curLineNum = lineNum
            
            userNum = int(row[4]) + int(row[5])
            if max < userNum:
                max = userNum
                maxStation = row[3]
            if min > userNum:
                min = userNum
                minStation = row[3]
        else :
            continue
    print("Line ",curLineNum,":")
    print("Busiest Station",maxStation,"(",max,")")
    print("Least Station",minStation,"(",min,")")


# In[ ]:




