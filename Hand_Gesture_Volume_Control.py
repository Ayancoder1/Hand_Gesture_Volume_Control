import cv2
import mediapipe as mp
import pyautogui
import time

x1 = y1 = x2 = y2 = 0
last_action = time.time()

webCam = cv2.VideoCapture(0)
my_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

while True:
    _ , image = webCam.read()
    image = cv2.flip(image,1)
    frame_height, frame_width, _ = image.shape
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = my_hands.process(rgb_image)
    hands = output.multi_hand_landmarks
    
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(image, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                if id == 8:
                    cv2.circle(img=image, center=(x,y), radius=8,color=(0,255,255), thickness=3)
                    x1 = x
                    y1 = y
                if id == 4:
                    cv2.circle(img=image, center=(x,y), radius=8, color=(0,0,255) ,thickness=3)
                    x2 = x
                    y2 = y
                    
        dist = ((x2-x1)**2 + (y2-y1)**2)** (0.5)
        cv2.line(image, (x1,y1),(x2,y2), (0,255,0), 3)   
        
        if time.time() - last_action > 0.225: 
            if dist > 120:
                pyautogui.press("volumeUp")
            elif dist < 60:
                pyautogui.press("volumeDown")
                
            last_action = time.time()
                    
    cv2.imshow("Volume Control by Hand Gesture in Python", image)
    
    key = cv2.waitKey(10)
    if key == 27:
        break
webCam.release()
cv2.destroyAllWindows()
    