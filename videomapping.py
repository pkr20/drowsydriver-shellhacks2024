import cv2
import dlib


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('face_data.dat') # these 2 calls are carrying

##cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(1)


while True:
    
    ret, frame = cap.read()
    if not ret:
        break

  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    faces = detector(gray)

    # Loop over each face found in the frame
    for face in faces:
        # Get the landmarks/parts for the face
        landmarks = predictor(gray, face)

        # Loop over each of the 68 facial landmarks and draw them on the frame
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1) #color

    cv2.imshow('Facial Landmarks', frame)

    # q to quit out
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#DO NOT DELETE THIS
cap.release()
cv2.destroyAllWindows()
