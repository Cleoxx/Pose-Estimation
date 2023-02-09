# Convert videos into pictures  
import cv2
import numpy as np
import os

class Snaphot:
    
    def __init__(self, spec, video_file, save_path, mod):
        self.save_path = save_path
        self.mod = mod
        self.spec = spec
        self.video_file = video_file
        
    def get_video_specs(self):
        self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.length = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.frame_nr = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
        fps = int(self.cap.get(cv2.CAP_PROP_FPS))
        
    def show_write_video(self, frame):
        cv2.imshow('Video', frame)
        if self.frame_nr%self.mod = 0:
            cv2.imwrite(self.save_path,frame)
        print(self.frame_nr)
    def produce_snapshots(self):
        self.cap=cv2.VideoCapture(self.video_file_rgb)
        self.cap.set(cv2.CAP_PROP_FORMAT, -1)
        self.get_video_specs()
        #self.frame_nr = 0
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if self.frame_nr<self.length: 
                self.frame_nr = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
                self.norming(frame)
                #self.draw_frame_counter()
                if ret:
                    self.show_write_video()
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                self.cap.release()
        cv2.destroyAllWindows()
        
        
Video_RGB = Snaphot('RGB', 'C:\Users\User\Documents\Masterstudium\Masterarbeit\TestPics\Thermoaufnahmen\Kameraaufnahmen\Handy\IMG_8290.MOV', 'C:\Users\User\Documents\Masterstudium\Masterarbeit\TestPics\train_data\TrainImg_{}_{}.jpg'.format(self.spec, self.frame_nr), 15)#071222a.mp4, TEST_RGBa.mp4
Video_IR = Snaphot('IR', 'C:\Users\User\Desktop\VideosEdited\Ravi_bearbeitet\ravi_a.mp4', 'C:\Users\User\Documents\Masterstudium\Masterarbeit\TestPics\train_data\bandw\TrainImg_{}_{}.jpg'.format(self.spec, self.frame_nr), 16)#ir071222ath.mp4, TEST_IRa.mp4


Video_RGB.produce_snaphots()
Video_IT.produce_snaphots()
