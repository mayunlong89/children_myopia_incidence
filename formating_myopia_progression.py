# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 16:28:27 2020

"""
#Python script
#Author: Yunlong Ma
#Date:2020-09-02
#E-mail: glb-biotech@zju.edu.cn

#This code was used for formating the data for Generalized mixed linear regression model on myopia progression

#----------------Start------------------------------------------------

f3 = open("2.1.model1-common.txt", "r+")
f4 = open("data_for_myopia_progression.txt","w+")

import time #used for monitoring the time of script operating

#test example
#f3 = open("test_model1.txt", "r+")
#f3_1 = open("test_model1.txt", "r+")
#f4 = open("data_for_onset_myopia_test663.txt","w+")


#collect samples ID for excluding from further analysis
start =time.clock()
ID_collect={}
#lines=""
for line in f3:
    dd = line.strip().split("\t")
    #lines=lines+line
    if dd[4] != "od_result" and int(dd[4])>3:
        ID_collect[dd[0]] = 1
    #if  dd[6]=="0":
      #  ID_collect[dd[0]] =1
      

#obtain unique ID    
#remove_id = list(set(ID_collect)) # using list is too waste time
#remove_id = set(ID_collect)
     
end = time.clock()
print('Running time1: %s Seconds'%(end-start))



#keep samples we need
#remove od_SE >4 and its related ID
#remove individuals with myopia at baseline time point and its related ID
start =time.clock()
#lines_out=''
#new_data=lines.split("\n")
for x in open("2.1.model1-common.txt", "r+"):
    tt = x.strip().split("\t")
    if tt[0] not in ID_collect:
        #lines_out = lines_out + "\t".join(tt) + "\n" #too waste time
        f4.write("\t".join(tt) + "\n")
    
    
#f2.write(lines_out)
end = time.clock()
print('Running time3: %s Seconds'%(end-start))

f3.close()
f4.close()



#----------------End------------------------------------------------




