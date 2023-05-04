#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
if __name__ == "__main__":
    f = open('q3.csv','r', encoding='UTF-8')
    data = csv.reader(f)
    header = next(data)
    sum =0;
    totalUserForLine = [0 for i in range(10)]
    curLineNum = 0
    for row in data :
        lineName = row[1]
        if(lineName[0] <='9' and lineName[0] >= '1'):
            lineNum = int(lineName[0])
            
            if curLineNum != lineNum:
                totalUserForLine[curLineNum] = sum
                sum =0
                curLineNum = lineNum
            else:
                curLineNum = lineNum
            
        else :
            continue
        if(row[1] == "9호선2~3단계"):
            continue;
        else:
            sum += int(row[4]) + int(row[5])
    totalUserForLine[curLineNum] = sum
    max1Idx = 0
    max1User = 0
    max2Idx = 0
    max2User = 0
    for idx,num in enumerate(totalUserForLine):
        if max1User < num:
            max1Idx =idx
            max1User = num
    for idx, num in enumerate(totalUserForLine):
        if max2User < num and idx != max1Idx :
            max2Idx =idx
            max2User = num
            
    min1Idx = 999
    min1User = 9999999999999
    min2Idx = 999
    min2User = 9999999999999
    for idx,num in enumerate(totalUserForLine):
        if(idx ==0):
            continue
        if min1User > num:
            min1Idx =idx
            min1User = num
    for idx, num in enumerate(totalUserForLine):
        if(idx ==0):
            continue
        if min2User > num and idx != min1Idx :
            min2Idx =idx
            min2User = num
    
    print("*** Subway Report for Seoul on March 2023 ***")
    print("1st Busiest Line: Line ",max1Idx,"(",max1User,")")
    print("2st Busiest Line: Line ",max2Idx,"(",max2User,")")
    print("1st Least Line: Line ",min1Idx,"(",min1User,")")
    print("2st Least Line: Line ",min2Idx,"(",min2User,")")


# In[ ]:




