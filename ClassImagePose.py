import mediapipe as mp
import cv2
import csv
#import matplotlib.pyplot as plt
#creating landmark csv from images
#IMAGE_FILES = []
class Image:
    body_parts = ('NOSE','LEFT_EYE_INNER','LEFT_EYE','LEFT_EYE_OUTER','RIGHT_EYE_INNER',
                'RIGHT_EYE','RIGHT_EYE_OUTER','LEFT_EAR','RIGHT_EAR','MOUTH_LEFT','MOUTH_RIGHT','LEFT_SHOULDER',
                'RIGHT_SHOULDER','LEFT_ELBOW','RIGHT_ELBOW','LEFT_WRIST','RIGHT_WRIST','LEFT_PINKY','RIGHT_PINKY',
                'LEFT_INDEX','RIGHT_INDEX','LEFT_THUMB','RIGHT_THUMB','LEFT_HIP','RIGHT_HIP','LEFT_KNEE','RIGHT_KNEE',
                'LEFT_ANKLE','RIGHT_ANKLE','LEFT_HEEL','RIGHT_HEEL','LEFT_FOOT_INDEX','RIGHT_FOOT_INDEX')
    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    

    def __init__(self, spec, mod, length, img_file, csvfile):
        self.spec = spec
        self.mod = mod
        self.length = length
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
        bp_csv_prep_fieldnames=[]
        csvfile = open(self.csvfile, 'w', newline='')
        for bp in Image.body_parts:
            bp_csv_prep_fieldnames.extend([bp+"_x", bp+"_y", bp+"_v"])
            #, bp+"_z", bp+"_visibility"
        writer = csv.DictWriter(csvfile, fieldnames=bp_csv_prep_fieldnames)
        #print (bp_csv_prep_fieldnames)
        writer.writeheader()
        self.writer=writer
    def load_image(self):
        #for idx, self.image_name in enumerate(self.img_file):
        #for i in range (0,2):
        self.image_name = self.img_file + '\\TrainImg_a_{}.jpg'.format(i)
        self.img = cv2.imread(self.image_name)
        print(self.img_file)
        print(self.image_name)
        #image_height, image_width, _ = self.img.shape
        #i +=1
        self.results = self.pose.process(self.img)
        #self.results = self.pose.process(self.img)
        #self.results = self.pose.process(cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB))
        #self.length = len([IMAGE_FILES])
        #return results
    def draw_landmarks(self):
        #self.annotated_image = self.img.copy()
        self.mp_drawing.draw_landmarks(self.annotated_image, self.results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS,
                                self.mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                self.mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                    )
        #self.mp_drawing.draw_landmarks(
        #self.annotated_image, self.results.pose_landmarks,
        #self.mp_pose.POSE_CONNECTIONS,
        #landmark_drawing_spec=self.mp_drawing_styles.get_default_pose_landmarks_style())
    def extract_landmarks(self):
        landmarks=self.results.pose_landmarks.landmark
        return landmarks
    def writerow(self, landmarks):
        bp_dict={}
        for bp_string in Image.body_parts:
            bp=getattr(Image.mp_pose.PoseLandmark, bp_string)
            bp_dict[bp_string+"_x"]=landmarks[bp.value].x
            bp_dict[bp_string+"_y"]=landmarks[bp.value].y
            #bp_dict[bp_string+"_z"]=landmarks[bp.value].z
            bp_dict[bp_string+"_v"]=landmarks[bp.value].visibility
            #self.plot([landmarks[bp.value].x, landmarks[bp.value].y, landmarks[bp.value].z])
        self.writer.writerow(bp_dict)
    def show_write_img(self, i):
        #self.out.write(frame)
        self.out = cv2.imwrite('C:/Users/User/Desktop/VideosEdited/Output_Images/{}_{}_Landmarks.png'.format(self.spec, i), self.annotated_image)
        #cv2.imwrite('/tmp/annotated_image' + str(idx) + '.png', annotated_image)
        cv2.imshow('Mediapipe Feed', self.annotated_image)
        #Image.mp_drawing.plot_landmarks(self.results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)
    def process_Image(self):
        #self.length = 10
        for i in range (0, self.length):
            self.image_name = self.img_file + '\\TrainImg_{}_{}.jpg'.format(self.mod, i)
            self.img = cv2.imread(self.image_name)
            self.results = self.pose.process(self.img)
            self.annotated_image = self.img.copy()
            #self.load_image()
            self.draw_landmarks()
            try:
                landmarks = self.extract_landmarks()
                self.writerow(landmarks)
            except Exception as e:
                print (e)
                pass
            self.out = cv2.imwrite('C:/Users/User/Desktop/VideosEdited/Output_Images/{}_{}_Landmarks.png'.format(self.spec, i), self.annotated_image)
            #cv2.imshow('Mediapipe Feed', self.annotated_image)
            i += 1
        
        #return i
        #cv2.destroyAllWindows()


a_artistic_image = Image('artistic', 'a', 134,'C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data1', "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_artisticxy.csv")
a_artistic_image.process_Image()
b_artistic_image = Image('artistic', 'b', 117,'C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data1', "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_artisticxy.csv")
b_artistic_image.process_Image()
c_artistic_image = Image('artistic', 'c', 91,'C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data1', "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_artisticxy.csv")
c_artistic_image.process_Image()
d_artistic_image = Image('artistic', 'd', 82,'C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data1', "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_artisticxy.csv")
d_artistic_image.process_Image()
e_artistic_image = Image('artistic', 'e', 59,'C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data1', "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_artisticxy.csv")
e_artistic_image.process_Image()
f_artistic_image = Image('artistic', 'f', 74,'C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data1', "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_artisticxy.csv")
f_artistic_image.process_Image()

a_norm_image = Image('norm', 'a', 134,'C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data1\\bandw', "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_normimagexy.csv")
a_norm_image.process_Image()
b_norm_image = Image('norm', 'b', 117,'C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data1\\bandw', "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_normimagexy.csv")
b_norm_image.process_Image()
c_norm_image = Image('norm', 'c', 91,'C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data1\\bandw', "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_normimagexy.csv")
c_norm_image.process_Image()
d_norm_image = Image('norm', 'd', 82,'C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data1\\bandw', "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_normimagexy.csv")
d_norm_image.process_Image()
e_norm_image = Image('norm', 'e', 59,'C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data1\\bandw', "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_normimagexy.csv")
e_norm_image.process_Image()
f_norm_image = Image('norm', 'f', 74,'C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data1\\bandw', "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_normimagexy.csv")
f_norm_image.process_Image()

a_rgb_image = Image('rgb', 'a', 134,'C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data1', "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_rgbimagexy.csv")
a_rgb_image.process_Image()
b_rgb_image = Image('rgb', 'b', 117,'C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data1', "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_rgbimagexy.csv")
b_rgb_image.process_Image()
c_rgb_image = Image('rgb', 'c', 91,'C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data1', "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_rgbimagexy.csv")
c_rgb_image.process_Image()
d_rgb_image = Image('rgb', 'd', 82,'C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data1', "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_rgbimagexy.csv")
d_rgb_image.process_Image()
e_rgb_image = Image('rgb', 'e', 59,'C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data1', "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_rgbimagexy.csv")
e_rgb_image.process_Image()
f_rgb_image = Image('rgb', 'f', 74,'C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\TestPics\\train_data1', "C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\Landmark CSV\\Landmarks_rgbimagexy.csv")
f_rgb_image.process_Image()

