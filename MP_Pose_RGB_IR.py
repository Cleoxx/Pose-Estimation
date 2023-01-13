   #!/usr/bin/env python
# coding: utf-8
# Main Code 
# Computing and saving the lansmarks and difs into csv 

import cv2 as cv
import mediapipe as mp
import numpy as np
import os
import math
import pandas as pd
from time import time
import matplotlib.pyplot as plt
from cmath import inf
from BodyParts import BodyParts
import pprint
import csv 

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

video_folder = "C:\\Users\\User\\Desktop\\VideosEdited"
video_file_rgb = "C:\\Users\\User\\Desktop\\VideosEdited\\TEST_RGBa.mp4" #ir071222ath.mp4 #071222a
video_file_ir = "C:\\Users\\User\\Desktop\\VideosEdited\\TEST_IRa.mp4" #ir071222athBW.mp4"

FrameDataAll = []
rgb_frame_nr=0
ir_frame_nr=0


#########################
# CSV Preparation
#########################
#Splitting X, Y and Z coordinates of each body part to be dsaved in a csv file
# TODO: CLOSE CSV FILE
def CSV_header_generation():
    body_parts = ('NOSE','LEFT_EYE_INNER','LEFT_EYE','LEFT_EYE_OUTER','RIGHT_EYE_INNER',
                'RIGHT_EYE','RIGHT_EYE_OUTER','LEFT_EAR','RIGHT_EAR','MOUTH_LEFT','MOUTH_RIGHT','LEFT_SHOULDER',
                'RIGHT_SHOULDER','LEFT_ELBOW','RIGHT_ELBOW','LEFT_WRIST','RIGHT_WRIST','LEFT_PINKY','RIGHT_PINKY',
                'LEFT_INDEX','RIGHT_INDEX','LEFT_THUMB','RIGHT_THUMB','LEFT_HIP','RIGHT_HIP','LEFT_KNEE','RIGHT_KNEE',
                'LEFT_ANKLE','RIGHT_ANKLE','LEFT_HEEL','RIGHT_HEEL','LEFT_FOOT_INDEX','RIGHT_FOOT_INDEX')
    bp_csv_prep_fieldnames=[]
    csvfile = open('BodyPartsDifs.csv', 'w', newline='')
    for bp in body_parts:
        bp_csv_prep_fieldnames.extend([bp+"_x", bp+"_y", bp+"_z"])
    writer = csv.DictWriter(csvfile, fieldnames=bp_csv_prep_fieldnames)
    print (bp_csv_prep_fieldnames)
    writer.writeheader()
    return writer

writer = CSV_header_generation()

#############################################
#Output video to be saved and compared later 
#############################################
out = cv.VideoWriter('C:\\Users\\User\\Desktop\\VideosEdited\\RGBLandmarks.mp4', cv.VideoWriter_fourcc(*'avc1'), 20.0, (1920,1080))

pose_rgb = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=2,
    enable_segmentation=True,
    min_detection_confidence=0.5,
    smooth_landmarks=True,
    min_tracking_confidence=0.5)
pose_ir = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=2,
    enable_segmentation=True,
    min_detection_confidence=0.5,
    smooth_landmarks=True,
    min_tracking_confidence=0.5)
pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=2,
    enable_segmentation=True,
    min_detection_confidence=0.5,
    smooth_landmarks=True,
    min_tracking_confidence=0.5)

#import RGB video
cap_rgb=cv.VideoCapture(video_file_rgb)
cap_ir=cv.VideoCapture(video_file_ir)

## Setup mediapipe instance
# pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
while cap_rgb.isOpened():
    ret_rgb, frame = cap_rgb.read()
    ret_ir, frame_ir = cap_ir.read()

    #get frame width and height RGB
    frame_width_rgb = int(cap_rgb.get(cv.CAP_PROP_FRAME_WIDTH))
    frame_height_rgb = int(cap_rgb.get(cv.CAP_PROP_FRAME_HEIGHT))
    length_rgb = int(cap_rgb.get(cv.CAP_PROP_FRAME_COUNT))
    #get frame width and height IR
    frame_width_ir = int(cap_ir.get(cv.CAP_PROP_FRAME_WIDTH))
    frame_height_ir = int(cap_ir.get(cv.CAP_PROP_FRAME_HEIGHT))
    length_ir = int(cap_ir.get(cv.CAP_PROP_FRAME_COUNT))
    if rgb_frame_nr<length_rgb:
        print(rgb_frame_nr)
        #print(length_rgb)
        # Recolor image to RGB
        rgb_frame_nr+=1
        ir_frame_nr+=1

        image_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        image_rgb.flags.writeable = False
        image_ir = cv.cvtColor(frame_ir, cv.COLOR_BGR2RGB)
        image_ir.flags.writeable = False

        # Make detection RGB and IR
        results_rgb = pose_rgb.process(image_rgb)
        results_ir = pose_ir.process(image_ir)

        # Recolor back to BGR
        image_rgb.flags.writeable = True
        image_rgb = cv.cvtColor(image_rgb, cv.COLOR_RGB2BGR)
        
        # Recolor back to BGR
        image_ir.flags.writeable = True
        image_ir = cv.cvtColor(image_ir, cv.COLOR_RGB2BGR)

        # Extract landmarks
        try:
            landmarks_rgb=results_rgb.pose_landmarks.landmark
            landmarks_ir = results_ir.pose_landmarks.landmark
        except:
            pass

        # Render detections RGB
        mp_drawing.draw_landmarks(image_rgb, results_rgb.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                    )  
        # Render detections IR
        mp_drawing.draw_landmarks(image_ir, results_ir.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                    )
        #if rgb_frame_nr%100==0:
        #    print(rgb_frame_nr, ir_frame_nr)
        FrameDataAll.append(BodyParts(landmarks_rgb, landmarks_ir, writer))
        #return VideoFileClip(video_folder
        cv.rectangle(image_rgb, (0,0), (225,73), (245,117,16), -1)
        
        # Rep data
        cv.putText(image_rgb, 'FRAME', (15,12), 
                cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv.LINE_AA)
        cv.putText(image_rgb, str(rgb_frame_nr), 
                (10,60), 
                cv.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv.LINE_AA)
            
        if ret_rgb:
        #out.write(image_rgb)
            out.write(image_rgb)
            cv.imshow('Mediapipe Feed RGB', image_rgb)
            cv.imshow('Mediapipe Feed IR', image_ir)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        cap_rgb.release()
        cap_ir.release()
out.release()
cv.destroyAllWindows()
print(length_rgb, length_ir)
pprint.pprint(FrameDataAll)
df = pd.read_csv('C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\BodyPartsDifs.csv')
print(df)