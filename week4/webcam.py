import cv2
fw = 640
fh = 480
cap = cv2.VideoCapture(0)
cap.set(3, fw)
cap.set(4, fh)
cap.set(10, 150)

while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitkey(1) & 0xFF == ord('q'):
        break
    if cv2.waitkey(5):
        cv2.imwrite("Desktop/IoTAP/week5/Hello.jpg")