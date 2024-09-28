import cv2
#waymo guy told me to use dlib to work with the dataset
import dlib

# trained dataset with face images in the "faces folder" I will email it all to you guys
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('face_data.dat')


# load the picture of the face (this path is to my camera roll from my webcam)
# you can do any picture though just update this
image_path = r'C:\Users\fuent\OneDrive\Pictures\Camera Roll\WIN_20240928_02_18_42_Pro.jpg'
image = cv2.imread(image_path)

# had to resize the window
scale_percent = 40  
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
image_resized = cv2.resize(image, (width, height))

# I had to turn it to grayscale to make plotting and manipulating the points easier
gray = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)

# Detect faces in grayscale image
faces = detector(gray)

# Loop over each face found in the image (in theory we could do multiple but we won't need to test that)
for face in faces:
    # Get the parts for the face
    landmarks = predictor(gray, face)

    # theres 68 landmarks 
    # this just means 68 plotted points on the face to base our program off of 
    # we can add more later with another training epoch if needed

    for n in range(0, 68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        cv2.circle(image_resized, (x, y), 2, (0, 255, 0), -1)  # Draw green dots on the landmarks


cv2.namedWindow('Facial Landmarks', cv2.WINDOW_NORMAL)
screen_width = 1920 
screen_height = 1080  
cv2.moveWindow('Facial Landmarks', (screen_width - width) // 2, (screen_height - height) // 2)
cv2.imshow('Facial Landmarks', image_resized)

#press any key to close the window
cv2.waitKey()
cv2.destroyAllWindows()

#notes from mentor meeting: 
"""
classification model: classify between eyes open / closed

CNN: Convo Neural Network

Kaggle.com

1. Camera Snapchat every few seconds from
a live video feed
(pass to dlib)

2. Send file to model
3. Model will classify
4. model returns result open/close
5. display result


how to train model: Kaggle.com , labeled pictures of eyes closed / open, run pictures through dlib, store processed pictures 

create new landmarked dataset

train classification model on landmarked dataset with CNN

Keras, tensorflow, pytorch could be useful



"""