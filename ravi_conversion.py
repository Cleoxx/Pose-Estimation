

import cv2
import numpy as np
import os



class Ravi:

    
    
    def __init__(self, spec, video_file, save_file):
        self.spec = spec
        #self.palette = palette
        self.video_file = video_file
        self.save_file = save_file
        
    def get_video_specs(self):        
        self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.length = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.frame_nr = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
        self.out = cv2.VideoWriter('C:\\Users\\User\\Desktop\\VideosEdited\\Ravi_bearbeitet\\ravi_{}.mp4'.format(self.spec),
                                    cv2.VideoWriter_fourcc(*'avc1'), 20.0, 
                                    (self.frame_width,self.frame_height))
    def norming (self):
        # Normalizing frame to range [0, 255], and get the result as type uint8 (this part is used just for making the data visible).
        self.frame = self.frame.view(np.int16).reshape(self.frame_height, self.frame_width)
        self.frame_roi = self.frame[1:, :]
        self.frame_roi = -self.frame_roi
        #self.draw_frame_counter()
        print(int(self.cap.get(cv2.CAP_PROP_POS_FRAMES)))
        normed = cv2.normalize(self.frame_roi, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
        cv2.imshow('rAVI Video', normed)
        self.out.write(self.frame)
    def draw_frame_counter(self):
        cv2.rectangle(self.frame, (0,0), (225,73), (245,117,16), -1)
        cv2.putText(self.frame, 'FRAME', (15,12), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(self.frame, str(self.frame_nr), (10,60), 
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
    
    def process_Video(self):
        self.cap=cv2.VideoCapture(self.video_file)
        self.cap.set(cv2.CAP_PROP_FORMAT, -1)
        self.get_video_specs()
        while self.cap.isOpened():
            ret, self.frame = self.cap.read()
            if self.frame_nr<self.length:
                if ret:
                    self.norming()
                    self.draw_frame_counter()
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                self.cap.release()
        self.close()
        cv2.destroyAllWindows()
        
ravi_a = Ravi('a', "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\Thermoaufnahmen\\Thermoaufnahmen071222\\071222a.ravi", "C:\\Users\\User\\Desktop\\VideosEdited\\Ravi_bearbeitet\\ravi_a.csv")

ravi_a.process_Video()

