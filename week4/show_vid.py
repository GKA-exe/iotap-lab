import cv2
fw = 640
fh = 480
cap = cv2.VideoCapture("Resources/test_video.mp4")

while True:
    success, img = cap.read()
    img = cv2.resize(img, (fw, fh))
    cv2.imshow("Result", img)
    if cv2.waitkey(1) & 0xFF == ord('q'):
        break