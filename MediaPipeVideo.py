# MediaPipe initialization
# Showing landmark videos
# Saving video with landmarks to a separate file 


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

# For videos
# Variables video file specific
# Enter path to videos here
#VID_FILES = [ r'C:\Users\User\Documents\Masterstudium\Masterarbeit\TestPics\Yoga-ein-Bein.jpg' ]
#video_folder = "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\Thermoaufnahmen\\Skalierung 0-100"
#video_file = "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\Thermoaufnahmen\\Skalierung 0-100\\GK_Squats_Seite_Front.ravi"

#all_videos = False # True means that you want to process all videos in the folder
#video_type = ".avi", ".ravi", ".mp4", ".wmv", ".mov" # Only files with this ending will be processed
#test_img = cv2.imread(video_file)
#BG_COLOR = (8,14,75) # blue
#BG_COLOR = (192,192,192) # gray
#video_location = 

#cv2.imshow('Test Image',test_img )
# use this to "cut" the video by setting start and end frame
#relevant_frame_list = [[0, inf] for i in range(len(list_of_names))]

out = cv.VideoWriter('C:\\Users\\User\\Desktop\\VideosEdited\\RGBLandmarks.wmv', cv.VideoWriter_fourcc('m', 'j', 'p', 'g'), 20.0, (640,480))

video_folder = "C:\\Users\\User\\Desktop\\VideosEdited"
video_file_rgb = "C:\\Users\\User\\Desktop\\VideosEdited\\071222a.mp4"#ir071222ath.mp4
video_file_ir = "C:\\Users\\User\\Desktop\\VideosEdited\\ir071222ath.mp4"

rgb_frame_nr=0
ir_frame_nr=0

#pose_rgb = mp_pose.Pose(static_image_mode=False,model_complexity=2,enable_segmentation=True,min_detection_confidence=0.5,smooth_landmarks=True,min_tracking_confidence=0.5)
#pose_ir = mp_pose.Pose(static_image_mode=False,model_complexity=2,enable_segmentation=True,min_detection_confidence=0.5,smooth_landmarks=True,min_tracking_confidence=0.5)
pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=2,
    enable_segmentation=True,
    min_detection_confidence=0.5,
    smooth_landmarks=True,
    min_tracking_confidence=0.5)
    
################
# Read Video
# https://docs.opencv.org/3.4/dd/d43/tutorial_py_video_display.html
################
cap_rgb=cv.VideoCapture(video_file_rgb)
cap_ir=cv.VideoCapture(video_file_ir)


#######################################
# Setup mediapipe instance
# Run mediapipe on rgb an ir videos
#######################################

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap_rgb.isOpened() or cap_ir.isOpened():
        retrgb, frame = cap_rgb.read()
        ret_ir, frame_ir = cap_ir.read()
         
        #get frame width and height RGB
        frame_width_rgb = int(cap_rgb.get(cv.CAP_PROP_FRAME_WIDTH))
        frame_height_rgb = int(cap_rgb.get(cv.CAP_PROP_FRAME_HEIGHT))
        length_rgb = int(cap_rgb.get(cv.CAP_PROP_FRAME_COUNT))
        
        #get frame width and height IR
        frame_width_ir = int(cap_ir.get(cv.CAP_PROP_FRAME_WIDTH))
        frame_height_ir = int(cap_ir.get(cv.CAP_PROP_FRAME_HEIGHT))
        length_ir = int(cap_ir.get(cv.CAP_PROP_FRAME_COUNT))
        ######################
        # Output Preparation
        # Output video to be saved and used as target
        # https://docs.opencv.org/3.4/dd/d43/tutorial_py_video_display.html
        # https://softron.zendesk.com/hc/en-us/articles/207695697-List-of-FourCC-codes-for-video-codecs 
        ######################
        #fourcc = cv.VideoWriter_fourcc(*'mp4v')
        #out = cv.VideoWriter('C:\\Users\\User\\Desktop\\VideosEdited\\RGBLandmarks.wmv', cv.VideoWriter_fourcc('w', 'm', 'v', '2'), 20.0, (frame_width_rgb,frame_height_rgb))
        #while rgb_frame_nr<2028:
            # Recolor image to RGB
        rgb_frame_nr+=1
        ir_frame_nr+=1
        image_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        image_rgb.flags.writeable = False
        image_ir = cv.cvtColor(frame_ir, cv.COLOR_BGR2RGB)
        image_ir.flags.writeable = False
      
            # Make detection RGB and IR
        results_rgb = pose.process(image_rgb)
        results_ir = pose.process(image_ir) 
    
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
        cv.rectangle(image_rgb, (0,0), (225,73), (245,117,16), -1)
        
        # Rep data
        cv.putText(image_rgb, 'FRAME', (15,12), 
                    cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv.LINE_AA)
        cv.putText(image_rgb, str(rgb_frame_nr), 
                    (10,60), 
                    cv.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv.LINE_AA)
        cv.imshow('Mediapipe Feed RGB', image_rgb)
        cv.imshow('Mediapipe Feed IR', image_ir)
        if cv.waitKey(10) & 0xFF == ord('q'):
           break
        out.write(frame)       
    cap_rgb.release()
    cap_ir.release()
    cv.destroyAllWindows()
    print(length_rgb, length_ir)
