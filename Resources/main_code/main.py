## let me try a new code where the window will be open even after 10 seconds

import os
import cv2
import cvzone
from cvzone.ClassificationModule import Classifier
import serial
import time

# Initialize serial communication with Arduino
ser = serial.Serial('COM8', 9600)  # Change 'COM3' to the appropriate port

time.sleep(2)  # Allow time for Arduino to initialize

classifier = Classifier('C:/Users/Aitha pranith/Downloads/Resources/Resources/Model/keras_model.h5', 'C:/Users/Aitha pranith/Downloads/Resources/Resources/Model/labels.txt')
imgArrow = cv2.imread('C:/Users/Aitha pranith/Downloads/Resources/Resources/arrow.png', cv2.IMREAD_UNCHANGED)
classIDBin = 0

# Import all the waste images
imgWasteList = []
pathFolderWaste = 'C:/Users/Aitha pranith/Downloads/Resources/Resources/Waste'
pathList = os.listdir(pathFolderWaste)
for path in pathList:
    imgWasteList.append(cv2.imread(os.path.join(pathFolderWaste, path), cv2.IMREAD_UNCHANGED))

# Import all the waste images
imgBinsList = []
pathFolderBins = 'C:/Users/Aitha pranith/Downloads/Resources/Resources/Bins'
pathList = os.listdir(pathFolderBins)
for path in pathList:
    imgBinsList.append(cv2.imread(os.path.join(pathFolderBins, path), cv2.IMREAD_UNCHANGED))

# 1 = recyclable
# 2 = organic
# 3 = hazardous

classDic = {0: None,
            1: 2,
            2: 2,
            3: 3,
            4: 3,
            5: 1,
            6: 3,
            7: 1}

# Open the camera for 10 seconds
cap = cv2.VideoCapture(0)
start_time = time.time()
object_detected = False
while time.time() - start_time < 10:
    ret, img = cap.read()
    if not ret:
        break

    imgResize = cv2.resize(img, (454, 340))

    imgBackground = cv2.imread('C:/Users/Aitha pranith/Downloads/Resources/Resources/CALI TECHNI.png')

    predection = classifier.getPrediction(img)

    classID = predection[1]
    print(classID)
    if classID != 0:
        # imgBackground = cvzone.overlayPNG(imgBackground, imgWasteList[classID - 1], (909, 127))
        imgBackground = cvzone.overlayPNG(imgBackground, imgArrow, (978, 320))

        classIDBin = classDic[classID]
        object_detected = True

    imgBackground = cvzone.overlayPNG(imgBackground, imgBinsList[classIDBin], (895, 374))

    imgBackground[148:148 + 340, 159:159 + 454] = imgResize

    # Display the image
    cv2.imshow("Output", imgBackground)
    cv2.waitKey(1)

# After the loop ends, send waste type classification to Arduino if an object was detected
if object_detected:
    waste_type = str(classIDBin)
    ser.write(waste_type.encode())

cap.release()
cv2.destroyAllWindows()
