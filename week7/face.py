import cv2

#Load the photograph
pixels = cv2.imread('test1.jpg')

#Load the pre-trained model
classifier = cv2.CascadeClassifier('train.xml')

#Perform face detection
bboxes = classifier.detectMultiScale(pixels)

#Print bounding box for each detected face
for box in bboxes:
	#Extract box lower left corner coordinates and width and height
	x, y, width, height = box
	x1, y1 = x + width, y + height
	#Draw a rectangle over the pixels
	cv2.rectangle(pixels, (x, y), (x1, y1), (0,0,255), 1)

#Save the image
cv2.imwrite('output.jpg', pixels)
