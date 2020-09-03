# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 15:51:52 2020

"""
#Python script
#Author: Yunlong Ma
#Date:2020-09-02
#E-mail: glb-biotech@zju.edu.cn

#This code was used for formating the data for Cox proportional hazard model on onset of myopia.
#remove od_SE >4 and its related ID.
#remove individuals with myopia (od_result = 1,2) at baseline time point and its related ID.
#generate a file of data_for_onset_myopia.txt for further Cox proportional hazard regression analysis by using the script of onset_myopia.r.

import time #used for monitoring the time of script operating

#------------Start-----------------------------

f1 = open("2.2.model2-common.txt", "r+")
f1_1=open("2.2.model2-common.txt", "r+")
f2 = open("data_for_onset_myopia.txt","w+")

#test example
#f1 = open("test.txt", "r+")
#f2 = open("data_for_onset_myopia_test663.txt","w+")

#collect samples ID for excluding from further analysis
start =time.clock()
ID_collect={}
#lines=""
for line in f1:
    dd = line.strip().split("\t")
    #lines=lines+line
    if dd[4] == "od_result":
        print("good, continue")
    else:
        if int(dd[4])>3:
            ID_collect[dd[0]] = 1
        if dd[6]=="0" and int(dd[4])>0:
            ID_collect[dd[0]] = 1
        
#obtain unique ID    
#remove_id = set(ID_collect)
#
 
end = time.clock()
print('Running time1: %s Seconds'%(end-start))



#keep samples we need
start =time.clock()
#lines_out=''
#new_data=lines.split("\n")
for x in f1_1:
    tt = x.strip().split("\t")
    if tt[0] not in ID_collect:
        f2.write("\t".join(tt) + "\n")
        #lines_out = lines_out + "\t".join(tt) + "\n" # too waste time
f2.write("\t".join(tt) + "\n")    
#out_file = lines_out
#f2.write(out_file)
end = time.clock()
print('Running time3: %s Seconds'%(end-start))

f1.close() 
f2.close



#------------End-----------------------------




