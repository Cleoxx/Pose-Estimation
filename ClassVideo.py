import mediapipe as mp
import cv2
import csv
from sys import argv



class Video:
    body_parts = ('NOSE','LEFT_EYE_INNER','LEFT_EYE','LEFT_EYE_OUTER','RIGHT_EYE_INNER',
                'RIGHT_EYE','RIGHT_EYE_OUTER','LEFT_EAR','RIGHT_EAR','MOUTH_LEFT','MOUTH_RIGHT','LEFT_SHOULDER',
                'RIGHT_SHOULDER','LEFT_ELBOW','RIGHT_ELBOW','LEFT_WRIST','RIGHT_WRIST','LEFT_PINKY','RIGHT_PINKY',
                'LEFT_INDEX','RIGHT_INDEX','LEFT_THUMB','RIGHT_THUMB','LEFT_HIP','RIGHT_HIP','LEFT_KNEE','RIGHT_KNEE',
                'LEFT_ANKLE','RIGHT_ANKLE','LEFT_HEEL','RIGHT_HEEL','LEFT_FOOT_INDEX','RIGHT_FOOT_INDEX')
    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils
    #mp_drawing_styles = mp.solutions.drawing_styles

    def __init__(self, spec, video_file, csvfile):
        self.spec = spec
        self.video_file = video_file
        self.pose = Video.mp_pose.Pose(static_image_mode=False,
                                model_complexity=2,
                                enable_segmentation=True,
                                min_detection_confidence=0.5,
                                smooth_landmarks=True,
                                min_tracking_confidence=0.5)
        self.csvfile = csvfile
        self.CSV_header_generation()
    
    def CSV_header_generation(self):
        bp_csv_prep_fieldnames=[]
        csvfile = open(self.csvfile, 'w', newline='')
        for bp in Video.body_parts:
            # adding selectedcoordinate or visibility values into the .csv file
            bp_csv_prep_fieldnames.extend([bp+"_x", bp+"_y"])
            #bp_csv_prep_fieldnames.extend([bp+"_v"])
        writer = csv.DictWriter(csvfile, fieldnames=bp_csv_prep_fieldnames)
        writer.writeheader()
        self.writer=writer
        
    def draw_landmarks(self, results, frame):
        self.mp_drawing.draw_landmarks(frame, results.pose_landmarks, Video.mp_pose.POSE_CONNECTIONS,
                                self.mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                self.mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                    )
                                    
    def get_video_specs(self):        
        self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.length = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.out = cv2.VideoWriter('C:\\Users\\User\\Desktop\\VideosEdited\\Output_Videos\\{}_Landmarks.mp4'.format(self.spec),
                                    cv2.VideoWriter_fourcc(*'avc1'), 20.0, 
                                    (self.frame_width,self.frame_height))
    def image_detection(self, frame):#, frame
        #self.image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #self.image.flags.writeable = False
        results = self.pose.process(frame)
        #self.image.flags.writeable = True
        #self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
        return results
    def extract_landmarks(self, results):
        landmarks=results.pose_landmarks.landmark
        return landmarks
    def writerow(self, landmarks):
        bp_dict={}
        for bp_string in Video.body_parts:
            bp=getattr(Video.mp_pose.PoseLandmark, bp_string)
            bp_dict[bp_string+"_x"]=landmarks[bp.value].x
            bp_dict[bp_string+"_y"]=landmarks[bp.value].y
            #bp_dict[bp_string+"_z"]=landmarks[bp.value].z
            #bp_dict[bp_string+"_v"]=landmarks[bp.value].visibility
        self.writer.writerow(bp_dict)
    def draw_frame_counter(self, frame, frame_nr):
        # displaying frame counter on the video
        cv2.rectangle(frame, (0,0), (225,73), (245,117,16), -1)
        cv2.putText(frame, 'FRAME', (15,12), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(frame, str(frame_nr), (10,60), 
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
    def show_write_video(self, frame):
        self.out.write(frame)
        cv2.imshow('Mediapipe Feed', frame)
    def close(self):
        self.out.release()
        cv2.destroyAllWindows()
    def process_Video(self):
        self.cap=cv2.VideoCapture(self.video_file)
        frame_nr = 0
        self.get_video_specs()
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if frame_nr<self.length:
                frame_nr+=1
                results = self.image_detection(frame)
                self.draw_landmarks(results, frame)
                try:
                    landmarks = self.extract_landmarks(results)
                    self.writerow(landmarks)
                except Exception as e:
                    print (e)
                    pass
                #self.draw_frame_counter(frame, frame_nr)
                if ret:
                    self.show_write_video(frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                self.cap.release()
        self.close()
######
#select videos 
######

# If cmdline arguments not specified, use default videos
rgb_params = ['RGB', "C:\\Users\\User\\Desktop\\VideosEdited\\071222a.mp4", "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_RGBxy.csv"]
normed_params = ['Norm', "C:\\Users\\User\\Desktop\\VideosEdited\\Ravi_bearbeitet\\Ravi_a.mp4", "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_Normxy.csv"]
if len(argv) != 4:
    Video_RGB = Video(*rgb_params)
    Normalized = Video(*normed_params)
    Video_RGB.process_Video()
    Normalized.process_Video()
else:
    Vid = Video(*argv[1:4])
    Vid.process_Video()


