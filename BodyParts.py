#Body Parts Dif
#Gets all bodypart coordinates, calculates difference and saves the calculated dif in a dictionary
#dictionary then gets saved in CSV file

import cv2
import mediapipe as mp
import numpy as np
import os
import math
import csv
import pandas as pd
from time import time
import matplotlib.pyplot as plt
from cmath import inf



def BodyParts(landmarks_rgb,landmarks_ir, writer = None):
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_pose = mp.solutions.pose 

    body_parts = ('NOSE','LEFT_EYE_INNER','LEFT_EYE','LEFT_EYE_OUTER','RIGHT_EYE_INNER',
                'RIGHT_EYE','RIGHT_EYE_OUTER','LEFT_EAR','RIGHT_EAR','MOUTH_LEFT','MOUTH_RIGHT','LEFT_SHOULDER',
                'RIGHT_SHOULDER','LEFT_ELBOW','RIGHT_ELBOW','LEFT_WRIST','RIGHT_WRIST','LEFT_PINKY','RIGHT_PINKY',
                'LEFT_INDEX','RIGHT_INDEX','LEFT_THUMB','RIGHT_THUMB','LEFT_HIP','RIGHT_HIP','LEFT_KNEE','RIGHT_KNEE',
                'LEFT_ANKLE','RIGHT_ANKLE','LEFT_HEEL','RIGHT_HEEL','LEFT_FOOT_INDEX','RIGHT_FOOT_INDEX')

    #mpPL = mp_pose.PoseLandmark
    #rgb_bp=getattr(body_parts)
    rgb_bp_dict = {}
    ir_bp_dict = {}
    dif_bp_dict = {}
    rgb_frame_nr=0
    ir_frame_nr=0
    bp_csv_prep={}
    bp_csv_prep_fieldnames=[]

    for bp_string in body_parts:
            bp=getattr(mp_pose.PoseLandmark, bp_string)
            rgb_bp_dict[bp_string]=[landmarks_rgb[bp.value].x, landmarks_rgb[bp.value].y, landmarks_rgb[bp.value].z] 
            #rgb_bp_dict[bp_string].append()
            #print(rgb_bp_dict[bp_string])
            ir_bp_dict[bp_string]=[landmarks_ir[bp.value].x, landmarks_ir[bp.value].y, landmarks_ir[bp.value].z]
            #ir_bp_dict[bp_string].append()
            #print(ir_bp_dict[bp_string])
            #for key in rgb_bp_dict and ir_bp_dict
            dif_bp_dict[bp_string]=np.subtract(rgb_bp_dict[bp_string], ir_bp_dict[bp_string])
            #dif_bp_dict[bp_string].append()
            #out.write(image_rgb)
            #print(dif_bp_dict[bp_string],bp_string)
            
            #########################
            # CSV Preparation
            #########################
            #Splitting X, Y and Z coordinates of each body part to be dsaved in a csv file
            for idx, pos in enumerate (dif_bp_dict[bp_string]):
                pos_string=None
                if idx == 0:
                    pos_string = "x"
                elif idx == 1:
                    pos_string = "y"
                elif idx == 2:
                    pos_string = "z"
                fieldname = "{}_{}".format(bp_string, pos_string)
                bp_csv_prep_fieldnames.append(fieldname)
                bp_csv_prep[fieldname]=pos
    writer.writerow(bp_csv_prep)
    return dif_bp_dict
