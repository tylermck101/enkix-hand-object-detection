
import cv2
import json
import os

json_file = "coffee_det.json"
with open(json_file, 'r') as json_file:
    data = json.load(json_file)

image_dir = '/home/tylermckenzie/hand_object_detector/6-1-coffee_1/rgb'

output_dir = 'output_images/'  # Directory to save modified images
os.makedirs(output_dir, exist_ok=True)

current_frame = 0

def play_frames():
    global current_frame
    while True:
        image_filename = data[current_frame]['image_filename']
        object_detections = data[current_frame]['object_detections']

        image_path = os.path.join(image_dir, f'frame_{image_filename}.jpg')
        image = cv2.imread(image_path)

        for detection in object_detections:
            box = detection['box']
            left_right = detection['left_right']
            object_label = detection['object_label'] if 'object_label' in detection else "Unknown"

            x, y, w, h = int(box[0]), int(box[1]), int(box[2] - box[0]), int(box[3] - box[1])
            color = (0, 255, 0) if left_right == 1 else (0, 0, 255)  # Green for left, Red for right

            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
            cv2.putText(image, f'{object_label}, {"Left" if left_right == 0 else "Right"}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        cv2.imshow('Image with Detections', image)
        key = cv2.waitKey(0)
        if key == ord('s'):
            current_frame += 10  # Skip forward by 10 frames
        elif key == ord('b'):
            current_frame -= 1  # Move backward by 10 frames
        elif key == ord('d'):
            current_frame -= 10  # Move backward by 10 frames
        elif key == ord('a'):
            current_frame += 1  # Move backward by 10 frames
        elif key == ord('q'):
           cv2.destroyAllWindows()
           break
        if current_frame < 0:
            current_frame = 0
        if current_frame >= len(data):
            current_frame = len(data) - 1

play_frames()

# Close all OpenCV windows when finished
cv2.destroyAllWindows()

