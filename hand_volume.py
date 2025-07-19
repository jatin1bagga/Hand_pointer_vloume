import cv2 as cv
import mediapipe as mp
import pyautogui

x1 = x2 = y1 = y2 = 0
webcam = cv.VideoCapture(0)
my_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
while True:
    _, image = webcam.read()
    image = cv.flip(image,1)
    rgbimage = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    output = my_hands.process(rgbimage)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(image, hand)
            landmarks = hand.landmark
            for id,landmark in enumerate(landmarks):
                x = int(landmark.x * image.shape[1])
                y = int(landmark.y * image.shape[0])

                if id == 8:
                    cv.circle(image,(x,y),8,(0,255,255),3)
                    x1 = x
                    y1 = y
                if id == 4:
                    cv.circle(image,(x,y),8,(0,0,255),3)
                    x2 = x
                    y2 = y

        distance = ((x2-x1)**2 + (y2 - y1)**2)**0.5//4
        cv.line(image,(x1,y1), (x2,y2),(0,255,0),5)
        if distance > 50:
            pyautogui.press("volumeup")
        else:
            pyautogui.press("volumedown")
                
    cv.imshow("hand volume control using python", image)
    key = cv.waitKey(10)
    if key == 27:
        break
webcam.release()
cv.destroyAllWindows()