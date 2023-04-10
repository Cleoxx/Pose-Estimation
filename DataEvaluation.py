import cv2 as cv
import mediapipe as mp
import numpy as np
import pandas as pd

###################
# READ Landmark FILES
###################
body_parts = ('NOSE','LEFT_EYE_INNER','LEFT_EYE','LEFT_EYE_OUTER','RIGHT_EYE_INNER',
            'RIGHT_EYE','RIGHT_EYE_OUTER','LEFT_EAR','RIGHT_EAR','MOUTH_LEFT','MOUTH_RIGHT','LEFT_SHOULDER',
            'RIGHT_SHOULDER','LEFT_ELBOW','RIGHT_ELBOW','LEFT_WRIST','RIGHT_WRIST','LEFT_PINKY','RIGHT_PINKY',
            'LEFT_INDEX','RIGHT_INDEX','LEFT_THUMB','RIGHT_THUMB','LEFT_HIP','RIGHT_HIP','LEFT_KNEE','RIGHT_KNEE',
            'LEFT_ANKLE','RIGHT_ANKLE','LEFT_HEEL','RIGHT_HEEL','LEFT_FOOT_INDEX','RIGHT_FOOT_INDEX')
            
df_rgb_image = pd.read_csv('C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_rgbimagev.csv')
df_art = pd.read_csv('C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_art3v.csv')
###############
# Build difference and normalize 
###############
df_dif_RGB_art= df_rgb_image.subtract(df_art)
###############
# Column-wise rsme
###############
df_rsme_xy_art = np.sqrt(np.sum(np.square(df_dif_RGB_art)))
mean_art = df_rmse_xy_art.mean()
################
# Display
################
print(df_rmse_xy_art.to_markdown())
print(mean_art)


###############