#Rscript
#date:2020-08-31
#Author: Yunlong Ma
#E-mail: glb-biotech@zju.edu.cn

#This script was used to perform Cox proportional hazard regression model on the incidence of high myopia in Chinese children.

#----------Start----------------------------

#set the directory for the present script
getwd()
setwd("C:\\Users\\Administrator\\Desktop\\2020-9-1-final")

#check the packages used in this script
if(!require("survival"))install.packages("survival")
if(!require("survminer"))install.packages("survminer")


#loading the packages
library("survival")
library("survminer")

#common dataset
data_high_onset<- read.table("data_for_onset_high_myopia.txt",header = TRUE)

# high myopia status should be integer
data_high_onset$high_myopia <- data_high_onset$od_result

data_high_onset$high_myopia[which(data_high_onset$od_result < 3)] <- 0 # high_myopia: 0 represents normal, 1 represent high myopia
data_high_onset$high_myopia[which(data_high_onset$od_result == 3)] <- 1 #high_myopia: 0 represents normal, 1 represent high myopia

data_high_onset3 <- na.omit(data_high_onset)

summary(data_high_onset3$high_myopia)

#educational level
data_high_onset3$education_level<- data_high_onset3$grade
data_high_onset3$education_level[which(data_high_onset3$grade<7)]<-1
data_high_onset3$education_level[which(data_high_onset3$grade<10 & data_high_onset3$grade>6)]<-2
data_high_onset3$education_level[which(data_high_onset3$grade>9)]<-3

#three time points
data_high_onset3$time <- data_high_onset3$interval

#as.factor for several predictors
data_high_onset3$education_level<-as.factor(data_high_onset3$education_level)
data_high_onset3$sex<-as.factor(data_high_onset3$sex)
data_high_onset3$school_key<-as.factor(data_high_onset3$school_key)
data_high_onset3$school_town<-as.factor(data_high_onset3$school_town)



#-----------important----------------
res_high.cox2 <- coxph(Surv(time, high_myopia) ~ grade+age+ birth_month+school_key+school_town, data = data_high_onset3)
res_high.cox3 <- coxph(Surv(time, high_myopia) ~ education_level+age+ birth_month+school_key+school_town, data = data_high_onset3)

summary(res_high.cox2)
summary(res_high.cox3)


#-----------non birth month----------------
res_high.cox2_2 <- coxph(Surv(time, high_myopia) ~ grade+age+school_key+school_town, data = data_high_onset3)
res_high.cox3_2 <- coxph(Surv(time, high_myopia) ~ education_level+age+school_key+school_town, data = data_high_onset3)

summary(res_high.cox2_2)
summary(res_high.cox3_2)


#---------------End----------------------------




