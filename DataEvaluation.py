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
print(df_RGB)

###############
# DIF und Betrag 
################
# von RGB und IR 
df_dif_RGB_IR = df_RGB.subtract(df_IR)
df_dif_RGB_IR = df_dif_RGB_IR.abs()


# von RGB und IR BW 
df_dif_RGB_IR_BW = df_RGB.subtract(df_IR_BW)
df_dif_RGB_IR_BW = df_dif_RGB_IR_BW.abs()