import cv2 as cv
import mediapipe as mp
import numpy as np
import pandas as pd

###################
# READ Landmark FILES
###################


df_RGB = pd.read_csv('C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_RGB.csv')
df_IR = pd.read_csv('C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_IR.csv')
df_IR_BW = pd.read_csv('C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_IR_BW.csv')
df_IR_RED = pd.read_csv('C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_IR_RED.csv')

#print(df_RGB)

###############
# DIF und Betrag 
################
# von RGB und IR 
df_dif_RGB_IR = df_RGB.subtract(df_IR)
df_dif_RGB_IR = df_dif_RGB_IR.abs()


# von RGB und IR BW 
df_dif_RGB_IR_BW = df_RGB.subtract(df_IR_BW)
df_dif_RGB_IR_BW = df_dif_RGB_IR_BW.abs()


#################
# Auswertung
#################
#min = print(df_dif_RGB_IR.min(0))
#imin = print(df_dif_RGB_IR.idxmin(0))
#imax = print(df_dif_RGB_IR.idxmax())
#nlargest = print(df_dif_RGB_IR.nlargest(5, "NOSE_x", "all"))
# hist = df_dif_RGB_IR.plot.hist()
#max = print(df_dif_RGB_IR.max())
T_RGB = df_dif_RGB_IR.T
print(T_RGB)
#max_RGB = T_RGB.max()
#print(max_RGB)
