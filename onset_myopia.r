#Rscript
#date:2020-08-31
#Author: Yunlong Ma
#E-mail: glb-biotech@zju.edu.cn

#This script was used to perform Cox proportional hazard regression model on the incidence of myopia in Chinese children.


#------------Start-----------------------------

#set the directory for the present script
getwd()
setwd("C:\\Users\\Administrator\\Desktop\\2020-9-1-final")

#check the packages used in this script
if(!require("survival"))install.packages("survival")
if(!require("survminer"))install.packages("survminer")


#loading the packages
library("survival")
library("survminer")
#all dataset
#data_onset<- read.table("d",header = TRUE)

#common dataset
data_onset<- read.table("data_for_onset_myopia.txt",header = TRUE)

summary(data_onset$od_result)
max(data_onset$od_result)

#myopia status should be integer
data_onset$myopia <- data_onset$od_result #create a collumn for myopia
data_onset$myopia[which(data_onset$myopia > 0)] <- 1 # status: 0 represents normal, 1 represent myopia
#data_onset3 <- data_onset2[-which(data_onset2$interval == 0 & data_onset2$status == 1),] #remove all the myopia in the start time point


data_onset3 <- na.omit(data_onset)
 
#educational level
data_onset3$education_level<- data_onset3$grade
data_onset3$education_level[which(data_onset3$grade<7)]<-1
data_onset3$education_level[which(data_onset3$grade<10 & data_onset3$grade>6)]<-2
data_onset3$education_level[which(data_onset3$grade>9)]<-3
data_onset3$education_level<-as.factor(data_onset3$education_level)

data_onset3$sex<-as.factor(data_onset3$sex)

data_onset3$myopia<-as.numeric(data_onset3$myopia) 


#Cox proprtional hazard regression model
res.cox1 <- coxph(Surv(interval, myopia) ~ grade , data = data_onset3)
#res.cox4 <- coxph(Surv(interval, status) ~ education_level+ birth_month+school_key+school_town, data = data_onset3)
res.cox5 <- coxph(Surv(interval, myopia) ~ education_level+age, data = data_onset3)
summary(res.cox1)
summary(res.cox5)


#-----------important----------------
res.cox2 <- coxph(Surv(interval, myopia) ~ grade+age+sex+birth_month+school_key+school_town, data = data_onset3)
res.cox3 <- coxph(Surv(interval, myopia) ~ education_level+age+sex+birth_month+school_key+school_town, data = data_onset3)

#-----------no birth month----------------
res.cox2_2 <- coxph(Surv(interval, myopia) ~ grade+age+sex+school_key+school_town, data = data_onset3)
res.cox3_2 <- coxph(Surv(interval, myopia) ~ education_level+age+sex+school_key+school_town, data = data_onset3)

summary(res.cox2)
summary(res.cox3)
summary(res.cox2_2)
summary(res.cox3_2)



#---------End-----------------------------


