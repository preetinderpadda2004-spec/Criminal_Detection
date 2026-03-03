import cv2
import numpy as np
import os

def train_model():
    # Initialize the LBPH face recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Load the face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Create lists to store face images and labels
    faces = []
    labels = []
    label_dict = {}

    # Assign a unique label to each user
    label_id = 0
    dataset_dir = "dataset"

    for user_name in os.listdir(dataset_dir):
        user_dir = os.path.join(dataset_dir, user_name)

        if not os.path.isdir(user_dir):
            continue

        # Assign a label to the user
        label_dict[label_id] = user_name

        for image_name in os.listdir(user_dir):
            image_path = os.path.join(user_dir, image_name)
            img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            if img is None:
                continue

            # Detect faces in the image
            detected_faces = face_cascade.detectMultiScale(img, 1.1, 4)

            for (x, y, w, h) in detected_faces:
                # Add face and label to the lists
                faces.append(img[y:y+h, x:x+w])
                labels.append(label_id)

        label_id += 1

    # Train the recognizer
    recognizer.train(faces, np.array(labels))
    recognizer.write("face_trainer.yml")

    return label_dict

# Example usage
label_dict = train_model()
print("Training complete. Label dictionary:", label_dict)
