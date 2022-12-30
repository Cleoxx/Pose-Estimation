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



def BodyParts(landmarks_rgb,landmarks_ir):
	mp_drawing = mp.solutions.drawing_utils
	mp_drawing_styles = mp.solutions.drawing_styles
	mp_pose = mp.solutions.pose 

	body_parts = ('NOSE','LEFT_EYE_INNER','LEFT_EYE','LEFT_EYE_OUTER','RIGHT_EYE_INNER',
				'RIGHT_EYE','RIGHT_EYE_OUTER','LEFT_EAR','RIGHT_EAR','MOUTH_LEFT','MOUTH_RIGHT',
				'LEFT_SHOULDER','RIGHT_SHOULDER','LEFT_ELBOW','RIGHT_ELBOW','LEFT_WRIST',
				'RIGHT_WRIST','LEFT_PINKY','RIGHT_PINKY','LEFT_INDEX','RIGHT_INDEX','LEFT_THUMB',
				'RIGHT_THUMB','LEFT_HIP','RIGHT_HIP','LEFT_KNEE','RIGHT_KNEE','LEFT_ANKLE',
				'RIGHT_ANKLE','LEFT_HEEL','RIGHT_HEEL','LEFT_FOOT_INDEX','RIGHT_FOOT_INDEX')

	#mpPL = mp_pose.PoseLandmark
	#rgb_bp=getattr(body_parts)
	rgb_bp_dict = {}
	ir_bp_dict = {}
	dif_bp_dict = {}
	rgb_frame_nr=0
	ir_frame_nr=0
	
	with open('BodyPartsDifs.csv', 'w') as csvfile:
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
			print(dif_bp_dict[bp_string],bp_string)
			print(rgb_frame_nr, ir_frame_nr)
			
			writer = csv.DictWriter(csvfile, fieldnames=bp_string)
			writer.writeheader(bp_string)
			writer.writerows(frame_rgb)
	
	
	
	
	