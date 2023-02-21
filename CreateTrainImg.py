# Convert videos into pictures  
import cv2
import numpy as np
import os

class Snapshot:
    
    def __init__(self, start_frame, end_frame, spec, mod, video_file, save_path):
        self.start_frame = start_frame
        self.end_frame = end_frame
        self.save_path = save_path
        self.mod = mod
        self.spec = spec
        self.video_file = video_file
        
    def get_video_specs(self):
        self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.length = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = int(self.cap.get(cv2.CAP_PROP_FPS))
    def show_write_video(self, frame, frame_nr, filename):
        cv2.imshow('Video', frame)
        if frame_nr % self.mod == 0:
            self.counter +=1
            cv2.imwrite(self.save_path + filename, frame)
        #print(frame_nr)
    def produce_snapshots(self):
        self.cap=cv2.VideoCapture(self.video_file)
        #self.cap.set(cv2.CAP_PROP_FORMAT, -1)
        self.get_video_specs()
        frame_nr = 0
        self.counter = 0
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if frame_nr < self.length:
                frame_nr = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
                if (self.start_frame < frame_nr) and (frame_nr < self.end_frame): 
                    #frame_nr = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES))
                    filename = ("TrainImg_{}_{}.jpg".format(self.spec, self.counter))
                    self.show_write_video(frame, frame_nr, filename)
                    print(frame_nr)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                self.cap.release()
                frame_nr = 0
        cv2.destroyAllWindows()
        
        
Video_RGB_a = Snapshot(606 , 2637, 'a', 15, "C:\\Users\\User\\Desktop\\VideosEdited\\071222a.mp4", "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data\\")
Video_IR_a = Snapshot(448, 2601, 'a', 16, "C:\\Users\\User\\Desktop\\VideosEdited\\Ravi_bearbeitet\\Ravi_a.mp4", "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data\\bandw\\")
Video_RGB_b = Snapshot(308 , 2072, 'b', 15, "C:\\Users\\User\\Desktop\\VideosEdited\\071222b.mp4", "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data\\")
Video_IR_b = Snapshot(355, 2225, 'b', 16, "C:\\Users\\User\\Desktop\\VideosEdited\\Ravi_bearbeitet\\Ravi_b.mp4", "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data\\bandw\\")
Video_RGB_c = Snapshot(378 , 1748, 'c', 15, "C:\\Users\\User\\Desktop\\VideosEdited\\071222c.mp4", "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data\\")
Video_IR_c = Snapshot(304, 1763, 'c', 16, "C:\\Users\\User\\Desktop\\VideosEdited\\Ravi_bearbeitet\\Ravi_c.mp4", "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data\\bandw\\")
Video_RGB_d = Snapshot(393 , 1621, 'd', 15, "C:\\Users\\User\\Desktop\\VideosEdited\\071222d.mp4", "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data\\")
Video_IR_d = Snapshot(447, 1756, 'd', 16, "C:\\Users\\User\\Desktop\\VideosEdited\\Ravi_bearbeitet\\Ravi_d.mp4", "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data\\bandw\\")
Video_RGB_e = Snapshot(204 , 1094, 'e', 15, "C:\\Users\\User\\Desktop\\VideosEdited\\071222e.mp4", "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data\\")
Video_IR_e = Snapshot(263, 1207, 'e', 16, "C:\\Users\\User\\Desktop\\VideosEdited\\Ravi_bearbeitet\\Ravi_e.mp4", "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data\\bandw\\")
Video_RGB_f = Snapshot(285 , 1403, 'f', 15, "C:\\Users\\User\\Desktop\\VideosEdited\\071222f.mp4", "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data\\")
Video_IR_f = Snapshot(280, 1457, 'f', 16, "C:\\Users\\User\\Desktop\\VideosEdited\\Ravi_bearbeitet\\Ravi_f.mp4", "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data\\bandw\\")

Video_RGB_a.produce_snapshots()
Video_IR_a.produce_snapshots()
Video_RGB_b.produce_snapshots()
Video_IR_b.produce_snapshots()
Video_RGB_c.produce_snapshots()
Video_IR_c.produce_snapshots()
Video_RGB_d.produce_snapshots()
Video_IR_d.produce_snapshots()
Video_RGB_e.produce_snapshots()
Video_IR_e.produce_snapshots()
Video_RGB_f.produce_snapshots()
Video_IR_f.produce_snapshots()