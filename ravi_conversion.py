import cv2
import numpy as np
import os
from sys import argv

########
# This class creates a .ravi - Video Object
# Input is .ravi video with a heathmap 
# Output is a .mp4 video in black and white 
########

class Ravi:
    
    def __init__(self, spec, video_file, save_path):
        self.save_path = save_path
        self.spec = spec
        self.video_file = video_file
        #self.save_file = save_file
        
    def get_video_specs(self):
        self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.length = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_nr = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
        fps = int(self.cap.get(cv2.CAP_PROP_FPS))
        self.out = cv2.VideoWriter(self.save_path + '\\Ravi_{}.mp4'.format(self.spec), 
        cv2.VideoWriter_fourcc(*'avc1'), fps, (self.frame_width,self.frame_height), False)
    def norming (self, frame):
        # Normalizing frame to range [0, 255], and get the result as type uint8 (this part is used just for making the data visible).
        frame = frame.view(np.int16).reshape(self.frame_height, self.frame_width)
        frame_roi = frame[1:, :]
        frame_roi = -frame_roi
        #self.draw_frame_counter()
        self.normed = cv2.normalize(frame_roi, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
        return frame
        #return normed
    def show_write_video(self, frame_nr):
        cv2.imshow('ravi Video', self.normed)
        self.out.write(self.normed)
        print(frame_nr)
    def close(self):
        self.out.release()
        cv2.destroyAllWindows()
    def process_Video(self):
        self.cap=cv2.VideoCapture(self.video_file)
        self.cap.set(cv2.CAP_PROP_FORMAT, -1)
        self.get_video_specs()
        frame_nr = 0
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if frame_nr < self.length:
                frame_nr = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
                self.norming(frame)
                if ret:
                    self.show_write_video(frame_nr)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                self.cap.release()
        self.close()
        
        
params = ['a', "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\Thermoaufnahmen\\Thermoaufnahmen071222\\071222a.ravi", "C:\\Users\\User\\Desktop\\VideosEdited\\Ravi_bearbeitet"]
if len(argv) != 4:
    Video = Ravi(*params)
    Video.process_Video()
else:
    Vid = Ravi(*argv[1:4])
    Vid.process_Video()