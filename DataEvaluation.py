import cv2 as cv
import mediapipe as mp
import numpy as np
import pandas as pd
#from sklearn.metrics import r2_score, mean_squared_error

###################
# READ Landmark FILES
###################
body_parts = ('NOSE','LEFT_EYE_INNER','LEFT_EYE','LEFT_EYE_OUTER','RIGHT_EYE_INNER',
            'RIGHT_EYE','RIGHT_EYE_OUTER','LEFT_EAR','RIGHT_EAR','MOUTH_LEFT','MOUTH_RIGHT','LEFT_SHOULDER',
            'RIGHT_SHOULDER','LEFT_ELBOW','RIGHT_ELBOW','LEFT_WRIST','RIGHT_WRIST','LEFT_PINKY','RIGHT_PINKY',
            'LEFT_INDEX','RIGHT_INDEX','LEFT_THUMB','RIGHT_THUMB','LEFT_HIP','RIGHT_HIP','LEFT_KNEE','RIGHT_KNEE',
            'LEFT_ANKLE','RIGHT_ANKLE','LEFT_HEEL','RIGHT_HEEL','LEFT_FOOT_INDEX','RIGHT_FOOT_INDEX')

df_RGB = pd.read_csv('C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_RGB.csv')
#df_IR = pd.read_csv('C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_IR.csv')
#df_IR_BW = pd.read_csv('C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_IR_BW.csv')
#df_IR_RED = pd.read_csv('C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_IR_RED.csv')
#df_IR_HC = pd.read_csv('C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_IR_HC.csv')

df_raw = pd.read_csv('C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_Raw.csv')

print(df_RGB)

###############
# DIF und Betrag 
################
# von RGB und IR 
#df_dif_RGB_IR = df_RGB.subtract(df_IR)
df_dif_RGB_raw = df_RGB.subtract(df_raw)

for bp in body_parts:
    header = bp+"_x", bp+"_y", bp+"_z"
#Normed Difference

for i in range(0,99):
    #np.sqrt(np.sum(df_dif_RGB_IR[['NOSE_x','NOSE_y']]**2,axis=1))
    for bp in body_parts:
        df_rmse = np.sqrt(np.sum(df_dif_RGB_raw[[bp+"_x", bp+"_y", bp+"_z"]]**2,axis=i))
        pd.df_rmse.to_csv (path_or_buf="C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\PD_DF_{}.csv".format(i)) 
    i+=1
    #, na_rep = '0', columns=99, header = header
    #, bp+"_visibility"
"""
# von RGB und IR BW 
df_dif_RGB_IR_BW = df_RGB.subtract(df_IR_BW)
df_dif_RGB_IR_BW = df_dif_RGB_IR_BW.abs()
"""

#################
# Auswertung
#################
#min = print(df_dif_RGB_IR.min(0))
#imin = print(df_dif_RGB_IR.idxmin(0))
#imax = print(df_dif_RGB_IR.idxmax())
#nlargest = print(df_dif_RGB_IR.nlargest(5, "NOSE_x", "all"))
# hist = df_dif_RGB_IR.plot.hist()
#max = print(df_dif_RGB_IR.max())
#T_RGB = df_dif_RGB_IR.T
T_rmse = df_rmse.T
print(T_rmse)

#max_RGB = T_RGB.max()
#print(max_RGB)
