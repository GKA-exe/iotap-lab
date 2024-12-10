import time
import cv2

start = time.time()
# Load the cascade model
face_cascade = cv2.CascadeClassifier("train.xml")

# Capture video from the webcam (0 is usually the default camera)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Read the frame
    ret, frame = cap.read()
    
    # Break out of loop if no frame is captured
    if not ret:
        print("End of stream")
        break
        
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # Draw rectangles over the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
    # Display the resulting frame
    cv2.imshow('Webcam Feed', frame)
    
    # Stop if 's' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
        
# Release the VideoCapture Object
cap.release()
cv2.destroyAllWindows()

end = time.time()
print("Time taken: ", (end - start))
