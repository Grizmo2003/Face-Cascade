import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

for i in range (1,4):
    # Read the input image
    img = cv2.imread("input" + str(i) + ".jpg")
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
    count = 0
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        count += 1
    print("Face on input" + str(i) + ".jpg",count)
    cv2.imwrite("output" + str(i) + ".jpg", img)

# Display the output
cv2.waitKey()
