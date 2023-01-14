import mediapipe as mp
import cv2


mp_pose = mp.solutions.pose


class Video:

    mp_drawing = mp.solutions.drawing_utils
    #mp_drawing_styles = mp.solutions.drawing_styles

    def __init__(self, spec, video_file):
        self.spec = spec
        self.video_file = video_file
        self.pose = mp_pose.Pose(static_image_mode=False,
                                model_complexity=2,
                                enable_segmentation=True,
                                min_detection_confidence=0.5,
                                smooth_landmarks=True,
                                min_tracking_confidence=0.5)

    def draw_landmarks(self, results):
        self.mp_drawing.draw_landmarks(self.image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                self.mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                self.mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                    )
                                    
    def get_video_specs(self):        
        self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.length = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.out = cv2.VideoWriter('C:\\Users\\User\\Desktop\\VideosEdited\\{}_Landmarks.mp4'.format(self.spec),
                                    cv2.VideoWriter_fourcc(*'avc1'), 20.0, 
                                    (self.frame_width,self.frame_height))
    def image_detection(self, frame):
        self.image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.image.flags.writeable = False
        results = self.pose.process(self.image)
        self.image.flags.writeable = True
        self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
        return results
    def extract_landmarks(self, results):
        try:
            landmarks=results.pose_landmarks.landmark
        except:
            pass
        
    def draw_frame_counter(self, frame_nr):
        cv2.rectangle(self.image, (0,0), (225,73), (245,117,16), -1)
        cv2.putText(self.image, 'FRAME', (15,12), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(self.image, str(frame_nr), (10,60), 
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
    def show_write_video(self):
            self.out.write(self.image)
            cv2.imshow('Mediapipe Feed', self.image)
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
                self.draw_landmarks(results)
                self.extract_landmarks(results)
                self.draw_frame_counter(frame_nr)
                if ret:
                    self.show_write_video()
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                self.cap.release()
        self.close()
        #print(length)
        #pprint.pprint(FrameDataAll)       



Video_RGB = Video('RGB', "C:\\Users\\User\\Desktop\\VideosEdited\\TEST_RGBa.mp4")
#Video_IR = Video('IR', "C:\\Users\\User\\Desktop\\VideosEdited\\TEST_IRa.mp4")
#Video_IR_BW = Video('IR_BW', "C:\\Users\\User\\Desktop\\VideosEdited\\TEST_BW.mp4")


Video_RGB.process_Video()

