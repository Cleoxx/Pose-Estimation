class Video:

    def __init__(self, spec):
        self.spec = spec
        self.pose = pose.append("_", spec)
        self.image = image.append("_", spec)
        self.cap = cap.append("_", spec)
        self.frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        self.ret = ret
        self.length = int(cap_rgb.get(cv.CAP_PROP_FRAME_COUNT))
        self.frame_nr = frame_nr
        

    def draw_landmarks(self, spec):
        #self.tricks.append(trick)
        mp_drawing.draw_landmarks(image.append("_", spec), results_rgb.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                    )
    def 
Video_RGB = Video('RGB')
Video_IR = Video('IR')
Video_BW = Video('BW')

  