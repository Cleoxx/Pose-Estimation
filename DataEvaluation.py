import cv2 as cv
import mediapipe as mp
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
#from sklearn.metrics import r2_score, mean_squared_error

###################
# READ Landmark FILES
###################
body_parts = ('NOSE','LEFT_EYE_INNER','LEFT_EYE','LEFT_EYE_OUTER','RIGHT_EYE_INNER',
            'RIGHT_EYE','RIGHT_EYE_OUTER','LEFT_EAR','RIGHT_EAR','MOUTH_LEFT','MOUTH_RIGHT','LEFT_SHOULDER',
            'RIGHT_SHOULDER','LEFT_ELBOW','RIGHT_ELBOW','LEFT_WRIST','RIGHT_WRIST','LEFT_PINKY','RIGHT_PINKY',
            'LEFT_INDEX','RIGHT_INDEX','LEFT_THUMB','RIGHT_THUMB','LEFT_HIP','RIGHT_HIP','LEFT_KNEE','RIGHT_KNEE',
            'LEFT_ANKLE','RIGHT_ANKLE','LEFT_HEEL','RIGHT_HEEL','LEFT_FOOT_INDEX','RIGHT_FOOT_INDEX')
'''
df_RGB = pd.read_csv('C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_RGBxy.csv')
df_raw = pd.read_csv('C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_Rawxy.csv')
df_norm = pd.read_csv('C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_Normxy.csv')
df_mask = pd.read_csv('C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_Maskxy.csv')

#print(df_RGB)
'''

#df_rgb_image = pd.read_csv('C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_rgbimagexyv.csv')
#df_OArt = pd.read_csv('C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_Oartisticxyv.csv')

df_rgb_image = pd.read_csv('C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_rgbimagexy.csv')
df_art = pd.read_csv('C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_art2xy.csv')
df_norm = pd.read_csv('C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_normxy.csv')
df_stable = pd.read_csv('C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_stablexy.csv')
df_Oart = pd.read_csv('C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_Oartxy.csv')
df_bad_art = pd.read_csv('C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_bad_art2xy.csv')
###############
# Dif and Norm 
################
'''
df_dif_RGB_raw = df_RGB.subtract(df_raw)
df_dif_RGB_norm = df_RGB.subtract(df_norm)
df_dif_RGB_mask= df_RGB.subtract(df_mask)
'''
df_dif_RGB_art= df_rgb_image.subtract(df_bad_art)

#print(df_dif_RGB_raw)
#print(df_dif_RGB_raw)


###############
#column wise rmse
###############
#df_rmse_xy_mask = np.sqrt(np.sum(np.square(df_dif_RGB_mask)))
df_rmse_xy_art = np.sqrt(np.sum(np.square(df_dif_RGB_art)))
#df_rmse_xy_raw = np.sqrt(np.sum(np.square(df_dif_RGB_raw)))

#mean_mask = df_rmse_xy_mask.mean()
mean_art = df_rmse_xy_art.mean()
#mean_norm = df_rmse_xyv_raw.mean()

#################
#Display
################



print(df_rmse_xy_art.to_markdown())
print(mean_art)



###############