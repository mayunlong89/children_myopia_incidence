# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 15:51:52 2020

"""
#Python script
#Author: Yunlong Ma
#Date:2020-09-02
#E-mail: glb-biotech@zju.edu.cn

#This code was used for formating the data for Cox proportional hazard model on onset of myopia

#--------------Start------------------------------

f1 = open("2.2.model2-common.txt", "r+")

f2 = open("data_for_onset_myopia.txt","w+")

#test example
#f1 = open("test.txt", "r+")
#f2 = open("data_for_onset_myopia_test3.txt","w+")

#collect samples ID for excluding for further analysis
ID_collect=[]
lines=""
for line in f1:
    dd = line.strip().split("\t")
    lines=lines+line
    if dd[4] != "od_result" and int(dd[4])>3:
        ID_collect.append(dd[0])
    if dd[4]=="0" and dd[6]=="0":
        ID_collect.append(dd[0])
      

#obtain unique ID    
remove_id = list(set(ID_collect))

#keep samples we need
#remove od_SE >4 and its related ID
#remove individuals with myopia at baseline time point and its related ID

lines_out=''
new_data=lines.split("\n")
for x in new_data:
    tt = x.strip().split("\t")
    if tt[0] not in remove_id:
        lines_out = lines_out + "\t".join(tt) + "\n"
    
    
f2.write(lines_out)

#---------------End------------------------

