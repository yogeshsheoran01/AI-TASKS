import cv2

# Load Haar cascade classifier for face detection
face_cap = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Open the webcam (0 is default camera)
video_cap = cv2.VideoCapture(0)

# Check if webcam opened successfully
if not video_cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, video_data = video_cap.read()
    
    if not ret:
        print("Failed to capture video frame.")
        break

    # Convert frame to grayscale for face detection
    gray = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cap.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(video_data, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Show the video feed
    cv2.imshow("Live Face Detection", video_data)

    # Exit when 'a' key is pressed
    if cv2.waitKey(10) & 0xFF == ord('a'):
        break

# Release resources
video_cap.release()
cv2.destroyAllWindows()
