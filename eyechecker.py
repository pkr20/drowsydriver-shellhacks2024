import cv2
import dlib
from scipy.spatial import distance as dist

# ear = eye aspect ratio 
# most every example I saw of tracking eyes closing or opening used this approach
def calculate_ear(eye):
    A = dist.euclidean(eye[1], eye[5])  
    B = dist.euclidean(eye[2], eye[4])  
    C = dist.euclidean(eye[0], eye[3])  
    ear = (A + B) / (2.0 * C)
    return ear


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('face_data.dat')

# Threshold for detecting closed eyes
EYE_AR_THRESHOLD = 0.23  # this could be fine tuned but chatgpt said .23 works best
WINK_DIFF_THRESHOLD = 0.08  # idk wink feature was cool and easy to add
eye_closed_counter = 0 # un used as of now


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break


    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

   
    faces = detector(gray_frame)

 
    gray_frame_colored = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)

    for face in faces:
        landmarks = predictor(gray_frame, face)

       
        left_eye = [(landmarks.part(n).x, landmarks.part(n).y) for n in range(42, 48)]
        right_eye = [(landmarks.part(n).x, landmarks.part(n).y) for n in range(36, 42)]

        #reminder ear isn't ear its eye to aspect ratio
        left_ear = calculate_ear(left_eye)
        right_ear = calculate_ear(right_eye)

        # Check if both eyes are closed (both EAR values below threshold)
        if left_ear < EYE_AR_THRESHOLD and right_ear < EYE_AR_THRESHOLD:
            eye_status = "Both Closed"
        # Check for winking (one eye closed and the other open with a significant EAR difference)
        # I found this to be necessary because the closed / open feature needs tuning
        elif abs(left_ear - right_ear) > WINK_DIFF_THRESHOLD:
            if left_ear < right_ear:
                eye_status = "Winking Left"
            else:
                eye_status = "Winking Right"
        else:
            eye_status = "Open"

        # Draw the landmarks for both eyes in color on the grayscale frame
        for (x, y) in left_eye:
            cv2.circle(gray_frame_colored, (x, y), 2, (0, 255, 0), -1)  
        for (x, y) in right_eye:
            cv2.circle(gray_frame_colored, (x, y), 2, (255, 0, 0), -1)  

        
        avg_ear = (left_ear + right_ear) / 2.0 # this could removed later it was for debugging
        cv2.putText(gray_frame_colored, f"EAR: {avg_ear:.2f}", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        cv2.putText(gray_frame_colored, f"Eye Status: {eye_status}", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)


    cv2.imshow('Facial Landmarks', gray_frame_colored) # gray frame so the colors stand out


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
