#!/usr/bin/python3
def find_peak(inArray):
    newArray=[]
    lenArray = len(inArray)
    if lenArray != 0:
        for i in range(1,lenArray-1):
            newArray.append(inArray[i])
        searchPeak=newArray[0]
        for j in range(len(newArray)):
            if newArray[j] >= searchPeak:
                searchPeak = newArray[j]
        return searchPeak
    else:
        return "None"
