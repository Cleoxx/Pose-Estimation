import mediapipe as mp
import cv2

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles


class Video:

    def __init__(self, spec, video_file):
        self.spec = spec
        self.video_file = video_file
        self.pose = mp_pose.Pose(static_image_mode=False,
                                model_complexity=2,
                                enable_segmentation=True,
                                min_detection_confidence=0.5,
                                smooth_landmarks=True,
                                min_tracking_confidence=0.5)
        #pose.append("_", spec)
        self.image = image #.append("_", spec)
        self.cap = cap.append("_", spec)
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.ret = ret
        self.length = length
        self.frame_nr = frame_nr
        self.results = results
        

    def draw_landmarks(self, spec):
        mp_drawing.draw_landmarks(image.append("_", spec), results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                    )
    def get_video_specs():
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    def image_detection():
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = pose.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    def extract_landmarks():
        try:
            landmarks=results.pose_landmarks.landmark
        except:
            pass
        
    def draw_frame_counter():
        cv2.rectangle(image, (0,0), (225,73), (245,117,16), -1)
        cv2.putText(image, 'FRAME', (15,12), 
                cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(image, str(frame_nr), (10,60), 
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
    def show_write_video():
        if ret_rgb:
            out.write(image_rgb)
            cv.imshow('Mediapipe Feed RGB', image_rgb)
            cv.imshow('Mediapipe Feed IR', image_ir)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    def 
    def play_Video(self):
        cap=cv2.VideoCapture(video_file)
        while cap.isOpened():
            ret, frame = cap.read()
            get_video_specs()
            if rgb_frame_nr<length_rgb:
                frame_nr+=1
                image_detection()
                extract_landmarks()
                draw_frame_counter()
                show_write_video()
            else:
                cap.release()
        out.release()
        cv2.destroyAllWindows()
        #print(length)
        #pprint.pprint(FrameDataAll)       
    def 
Video_RGB = Video('RGB', "C:\\Users\\User\\Desktop\\VideosEdited\\TEST_RGBa.mp4")
Video_IR = Video('IR', "C:\\Users\\User\\Desktop\\VideosEdited\\TEST_IRa.mp4")
Video_IR_BW = Video('IR_BW', "C:\\Users\\User\\Desktop\\VideosEdited\\TEST_BW.mp4")

  