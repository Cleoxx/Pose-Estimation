# Convert videos into pictures  
import cv2
import numpy as np
import os

class Snapshot:
    
    def __init__(self, spec, mod, video_file, save_path):
        self.save_path = save_path
        self.mod = mod
        self.spec = spec
        self.video_file = video_file
        
    def get_video_specs(self):
        self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.length = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = int(self.cap.get(cv2.CAP_PROP_FPS))
    def resize(self, frame):
        frame = frame.view(np.int16).reshape(self.frame_height, self.frame_width)
        frame_roi = frame[1:, :]
        frame_roi = -frame_roi
        frame_roi = frame_roi.cv2.CV_8U
        #norm = np.zeros(self.frame_height, self.frame_width)
        self.normed = cv2.normalize(frame_roi, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    def show_write_video(self, frame, frame_nr, filename):
        cv2.imshow('Video', frame)
        if frame_nr % self.mod == 0:
            cv2.imwrite(self.save_path + filename, frame)
        print(frame_nr)
    def produce_snapshots(self):
        self.cap=cv2.VideoCapture(self.video_file)
        #self.cap.set(cv2.CAP_PROP_FORMAT, -1)
        self.get_video_specs()
        frame_nr = 0
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if frame_nr < self.length:
                frame_nr = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
                #self.resize(frame)
                filename = ("TrainImg_{}.jpg".format(frame_nr))
                if ret:
                    self.show_write_video(frame, frame_nr, filename)
                    #print(frame_nr)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                self.cap.release()
        cv2.destroyAllWindows()
        
        
Video_RGB = Snapshot('RGB', 15, "C:\\Users\\User\\Desktop\\VideosEdited\\071222a.mp4", "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data\\")
Video_IR = Snapshot('IR', 16, "C:\\Users\\User\\Desktop\\VideosEdited\\Ravi_bearbeitet\\Ravi_a_cut.mp4", "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data\\bandw\\")


Video_RGB.produce_snapshots()
Video_IR.produce_snapshots()
