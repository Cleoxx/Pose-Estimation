User Instructions 


ClassVideo.py:
- this class performs landmark detection and display on videos
- the landmark coordinates are saved in a separate csv file
- enter video spec, video path and CSV file path, all separated by spaces when starting the program
- if no parameters are entered, the default videos will be processed


ClassImagePose.py:
- landmark detection on images instead of videos
- the landmark coordinates are saved in a separate csv file
- training image for DeOldify are used 
- enter video spec, video path and CSV file path, all separated by spaces when starting the program
- if no parameters are entered, the default videos will be processed


CreateTrainImg.py:
- videos are cut and individual frames saved as images
- Parameters to be entered with the videos:
1. start_frame: starting frame for the video to be cut from 
2. end_frame: last frame for the video to be cut to
3. spec: specification or name of the video to be distinguished from the other videos, if multiple are being processed
4. mod: depending on the fps. 15 for the RGB-video, 16 for the IR-video due to the different fps rate of the video recording (30 and 32 fps), to ensure equivalent frames.
5. video_file: path of the video
6. save_path: path to the folder, where resulting images will be saved


DataEvaluation.py:
- two pandas dataframes are loaded from two CSV files 
- differences between the coordinates of two dataframes are built
- RSME of these differences is calculated over each column 
- a mean value is displayed along with the RSME
