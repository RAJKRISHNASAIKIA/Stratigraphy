#!/usr/bin/env python
# coding: utf-8


import json

file_strati = open("E:\Raj Petro\stratigraphy.json")
file_wellpath = open("E:\Raj Petro\wellpath.json")
stratigraphy = json.load(file_strati)
wellpath = json.load(file_wellpath)


# Converting feet to meters
for i in stratigraphy:
    i["pickDepth"] = round(i["pickDepth"] * 0.3048)
    


#Adding 'top' sub-dictionary to the key 'depth'
for i in range(len(stratigraphy)):
    for j in wellpath:
        if(stratigraphy[i]["pickDepth"] == j["md"]):
            top = {}
            depth = {}
            top["md"] = j["md"]
            top["tvd"] = round(j["tvd"], 2)
            depth["top"] = top
            stratigraphy[i]['depth'] = depth  
        


#Adding 'bottom' to 'depth'
for i in range(len(stratigraphy)):
    bottom = {}
    if(i == len(stratigraphy)-1):
        bottom['md'] = round(wellpath[len(wellpath)-1]['md'], 2)
        bottom['tvd'] = round(wellpath[len(wellpath)-1]['tvd'], 2)
        stratigraphy[i]['depth']['bottom'] = bottom
        
    else:
        bottom['md'] = stratigraphy[i+1]['depth']['top']['md']
        bottom['tvd'] = round(stratigraphy[i+1]['depth']['top']['tvd'], 2)
        stratigraphy[i]['depth']['bottom'] = bottom
        
        
    
#Removing 'pickDepth'
for i in stratigraphy:
    i.pop('pickDepth')



#Renaming to 'undifferentiated'
for i in stratigraphy:
    if('base' in i['pickName']):
        i.update(pickName = 'undifferentiated')


#Final result
for i in stratigraphy:
    print(i)



#convert to json and save file
with open("output.json", "w") as write_file:
    json.dump(stratigraphy, write_file, indent=4)
