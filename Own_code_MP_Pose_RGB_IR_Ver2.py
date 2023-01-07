   #!/usr/bin/env python
# coding: utf-8
# Main Code 
# Computing and saving the lansmarks and difs into csv 

import cv2
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

# For videos
# Variables video file specific
# Enter path to videos here
#VID_FILES = [ r'C:\Users\User\Documents\Masterstudium\Masterarbeit\TestPics\Yoga-ein-Bein.jpg' ]
#video_folder = "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\Thermoaufnahmen\\Skalierung 0-100"
#video_file = "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\Thermoaufnahmen\\Skalierung 0-100\\GK_Squats_Seite_Front.ravi"

video_folder = "C:\\Users\\User\\Desktop\\VideosEdited"
video_file_rgb = "C:\\Users\\User\\Desktop\\VideosEdited\\071222a.mp4"#ir071222ath.mp4
video_file_ir = "C:\\Users\\User\\Desktop\\VideosEdited\\ir071222athBW.mp4" #ir071222ath.mp4"

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

# one selected video to test
#video_location = video_file
# output video path
#out_vid_path = video_folder

#import RGB video
cap_rgb=cv2.VideoCapture(video_file_rgb)
cap_ir=cv2.VideoCapture(video_file_ir)

## Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap_rgb.isOpened() or cap_ir.isOpened():
        retrgb, frame = cap_rgb.read()
        #cv2.imshow('Mediapipe Feed', frame)
        ret_ir, frame_ir = cap_ir.read()
        #cv2.imshow('Mediapipe Feed', frame_ir)
        
        #get frame width and height RGB
        frame_width_rgb = int(cap_rgb.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height_rgb = int(cap_rgb.get(cv2.CAP_PROP_FRAME_HEIGHT))
        length_rgb = int(cap_rgb.get(cv2.CAP_PROP_FRAME_COUNT))
        
        #get frame width and height IR
        frame_width_ir = int(cap_ir.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height_ir = int(cap_ir.get(cv2.CAP_PROP_FRAME_HEIGHT))
        length_ir = int(cap_ir.get(cv2.CAP_PROP_FRAME_COUNT))
        
        #Output video to be saved and compared later 
        #out_rgb = cv2.VideoWriter('C:\\Users\\User\\Desktop\\VideosEdited\\LandmarkRGB.mp4',cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 50, (frame_width_rgb,frame_height_rgb))
        
        while rgb_frame_nr<length_rgb:
            #cap_rgb.release()
            # Recolor image to RGB
            rgb_frame_nr+=1
            ir_frame_nr+=1
            image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image_rgb.flags.writeable = False
            image_ir = cv2.cvtColor(frame_ir, cv2.COLOR_BGR2RGB)
            image_ir.flags.writeable = False
      
            # Make detection RGB and IR
            results_rgb = pose_rgb.process(image_rgb)
            results_ir = pose_ir.process(image_ir)
    
            # Recolor back to BGR
            image_rgb.flags.writeable = True
            image_rgb = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)
            # Recolor back to BGR
            image_ir.flags.writeable = True
            image_ir = cv2.cvtColor(image_ir, cv2.COLOR_RGB2BGR)
        
            # Extract landmarks
            try:
                landmarks_rgb=results_rgb.pose_landmarks.landmark
                landmarks_ir = results_ir.pose_landmarks.landmark
                #print(landmarks_rgb)
                #out.write(image_rgb)
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
            
            #BP_Difs = BodyParts(landmarks_rgb, landmarks_ir)
            if rgb_frame_nr%100==0:
                print(rgb_frame_nr, ir_frame_nr)
            FrameDataAll.append(BodyParts(landmarks_rgb, landmarks_ir, writer))
            #return VideoFileClip(video_folder
            #cv2.imshow('Mediapipe Feed', image_rgb)
            #cv2.imshow('Mediapipe Feed', image_ir)
            #df=pd.DataFrame(dif_bp_dict[bp_string])
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
            
        cap_rgb.release()
        cap_ir.release()
    cv2.destroyAllWindows()
    print(length_rgb, length_ir)
pprint.pprint(FrameDataAll)