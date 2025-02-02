import cv2
import mediapipe as mp
import time #to check frame rate

cap = cv2.VideoCapture(0)

mpHands =mp.solutions.hands
hands = mpHands.Hands() # to check parameters for Hands(), right click on the word hand and ctrl
mpDraw =mp.solutions.drawing_utils #draw red points (joints in hands) and lines between the points in each joint of the hand (the green lines)

pTime = 0
cTime = 0

#the code usually used to run a webcam
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #because the hands object only uses rgb objects
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    #to extract the information of each available hand, if there is more than one hand
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks: #handLms is ONE HAND
            for id, lm in enumerate(handLms.landmark): #get information for the hand (lm gives x and y coordinates, id is joint number)
                #print(id, lm)
                h, w, c=img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                if id == 0:
                    cv2.circle(img, (cx,cy), 12, (255,0,255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime= cTime

    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_ITALIC, 3, (255,0,255),3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
