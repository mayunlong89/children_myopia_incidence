# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 15:51:52 2020

"""
#Python script
#Author: Yunlong Ma
#Date:2020-09-02
#E-mail: glb-biotech@zju.edu.cn

#This code was used for formating the data for Cox proportional hazard model on onset of myopia


#--------------------Start----------------------------------

import time #used for monitoring the time of script operating


f1 = open("2.2.model2-common.txt", "r+")
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
    if dd[4] != "od_result" and int(dd[4])>3:
        ID_collect[dd[0]] = 1
    if dd[4]=="0" and dd[6]=="0":
        ID_collect[dd[0]] = 1

#obtain unique ID    
#remove_id = set(ID_collect)
#
 
end = time.clock()
print('Running time1: %s Seconds'%(end-start))



#keep samples we need
#remove od_SE >4 and its related ID
#remove individuals with myopia at baseline time point and its related ID
start =time.clock()
#lines_out=''
#new_data=lines.split("\n")
for x in open("2.2.model2-common.txt", "r+"):
    tt = x.strip().split("\t")
    if tt[0] not in ID_collect:
        f2.write("\t".join(tt) + "\n")
        #lines_out = lines_out + "\t".join(tt) + "\n" # too waste time
f2.write("\t".join(tt) + "\n")    
#out_file = lines_out
#f2.write(out_file)
end = time.clock()
print('Running time2: %s Seconds'%(end-start))

f1.close() 
f2.close



#--------------------End----------------------------------







