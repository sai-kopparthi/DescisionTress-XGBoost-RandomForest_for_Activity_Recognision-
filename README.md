# DescisionTress-XGBoost-RandomForest_for_Activity_Recognision
#Data
  
The dataset is taken from UCI Repository named as Heterogeneity Activity Recognition
Data Set. The data is characterized as Multivariate and is used for associated task like
Clustering and classification.
The dataset contains the readings of two motion sensors commonly found in smartphones.
Reading were recorded while users executed activities scripted in no specific
order carrying smartwatches and smartphones.

##1.1 Goal
We need to recognize the human activities of different user by using Classification and
clustering techniques.

1.2 Total Activities
Biking, Sitting, Standing, Walking, Stair Up and Stair down.

1.3 Total Sensors
Two embedded sensors, i.e., Accelerometer and Gyroscope, sampled at the highest frequency
the respective device allows.

1.4 Total Devices
4 smartwatches (2 LG watches, 2 Samsung Galaxy Gears) 8 smartphones (2 Samsung
Galaxy S3 mini, 2 Samsung Galaxy S3, 2 LG Nexus 4, 2 Samsung Galaxy S+)

1.5 Used Devices
nexus_2b, nexus_1c, nexus_2c, s3_1, s3_2, s3_mini_1

1.6 Recordings
9 users data recordings but we considered only 3 users data for this project.

2 Filtering data
We got the data with 128 features which is not required for the present classification
so firstly for all the below models we filtered the data such that it contains only (4
parameters) sensor outputs and its corresponding output label, and instead of data with
char labels we modify the labels with integers such itâAZs flexible for us to do operations
faster. We wrote this code in R programming and submitted in the zip file.
