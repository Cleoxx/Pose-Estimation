import cv2 as cv
import mediapipe as mp
import numpy as np
import os
import math
import pandas as pd
from time import time
import matplotlib.pyplot as plt
from cmath import inf
from BodyParts import BodyParts
import pprint
import csv 






df = pd.read_csv('C:\\Users\\User\\Documents\\Masterstudium\\Masterarbeit\\Pose-Estimation_own\\BodyPartsDifs.csv')
print(df)