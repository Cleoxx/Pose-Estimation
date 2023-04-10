import mediapipe as mp
import cv2
import csv
from pathlib import Path
import os 
from os import listdir
from sys import argv

#creating landmark csv from images instead of videos 
#training image for DeOldify are used 

class Image:
    body_parts = ('NOSE','LEFT_EYE_INNER','LEFT_EYE','LEFT_EYE_OUTER','RIGHT_EYE_INNER',
                'RIGHT_EYE','RIGHT_EYE_OUTER','LEFT_EAR','RIGHT_EAR','MOUTH_LEFT','MOUTH_RIGHT','LEFT_SHOULDER',
                'RIGHT_SHOULDER','LEFT_ELBOW','RIGHT_ELBOW','LEFT_WRIST','RIGHT_WRIST','LEFT_PINKY','RIGHT_PINKY',
                'LEFT_INDEX','RIGHT_INDEX','LEFT_THUMB','RIGHT_THUMB','LEFT_HIP','RIGHT_HIP','LEFT_KNEE','RIGHT_KNEE',
                'LEFT_ANKLE','RIGHT_ANKLE','LEFT_HEEL','RIGHT_HEEL','LEFT_FOOT_INDEX','RIGHT_FOOT_INDEX')
    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles

    

    def __init__(self, spec, img_file, csvfile):
        self.spec = spec
        self.img_file = img_file
        self.pose = Image.mp_pose.Pose(static_image_mode=True,
                                model_complexity=2,
                                enable_segmentation=True,
                                min_detection_confidence=0.5,
                                smooth_landmarks=True,
                                min_tracking_confidence=0.5)
        self.csvfile = csvfile
        self.CSV_header_generation()
    
    def CSV_header_generation(self):
        self.bp_csv_prep_fieldnames=[]
        csvfile = open(self.csvfile, 'w', newline='')
        for bp in Image.body_parts:
            self.bp_csv_prep_fieldnames.extend([bp+"_v"])
            #bp+"_x", bp+"_y"
        writer = csv.DictWriter(csvfile, fieldnames=self.bp_csv_prep_fieldnames)
        writer.writeheader()
        self.writer=writer
    def draw_landmarks(self):
        self.mp_drawing.draw_landmarks(self.annotated_image, self.results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS,
                                self.mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                self.mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                    )
    def extract_landmarks(self):
        landmarks=self.results.pose_landmarks.landmark
        return landmarks
    def show_write_img(self, i):
        self.out = cv2.imwrite('C:/Users/User/Desktop/VideosEdited/Output_Images/{}_{}_Landmarks.png'.format(self.spec, i), self.annotated_image)
        cv2.imshow('Mediapipe Feed', self.annotated_image)
    def process_Image(self):
        i = 0
        path = self.img_file
        files = os.listdir(path)
        bp_dict={}
        for image in files:
            if image.endswith(('.jpg')):
                img_name = path + image
                img = cv2.imread(img_name)
                self.results = self.pose.process(img)
                self.annotated_image = img.copy()
                self.draw_landmarks()
                try:
                    landmarks = self.extract_landmarks()
                    for bp_string in Image.body_parts:
                        bp=getattr(Image.mp_pose.PoseLandmark, bp_string)
                        #bp_dict[bp_string+"_x"]=landmarks[bp.value].x
                        #bp_dict[bp_string+"_y"]=landmarks[bp.value].y
                        bp_dict[bp_string+"_v"]=landmarks[bp.value].visibility
                except:
                    if self.results.pose_landmarks == False:
                        for bp_string in Image.body_parts:
                            bp=getattr(Image.mp_pose.PoseLandmark, bp_string)
                            #bp_dict[bp_string+"_x"]=0
                            #bp_dict[bp_string+"_y"]=0
                            bp_dict[bp_string+"_v"]=0
                finally:
                    self.writer.writerow(bp_dict) 
                    i += 1

######
#select videos 
######

# If cmdline arguments not specified, use default videos
art_image = ['art',"C:/Users/User/Documents/Masterstudium/Masterarbeit/Pose-Estimation_own/DeOldify/result_images/Artistic3/", "C:/Users/User/Documents/Masterstudium/Masterarbeit/Pose-Estimation_own/Landmark CSV/Landmarks_artv.csv"]
if len(argv) != 4:
    art_image = Image(*art_image)
    art_image.process_Image()
else:
    Im = Image(*argv[1:4])
    Im.process_Image()