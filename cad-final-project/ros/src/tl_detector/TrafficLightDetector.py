from styx_msgs.msg import TrafficLight
from ultralytics import YOLO
import rospy
import cv2

class TrafficLightDetector():
    def __init__(self):
        self.model = YOLO("./yolo_model/best.pt")
    
    def detect_state(self, camera_frame):
        #Make predictions
        predictions = self.model.predict(camera_frame, verbose=False)
               
        all_labels = ["Green","Yellow","Red"]

        #Get the prediction label
        label = all_labels[int(predictions[0].boxes[0].cls[0])]
        rospy.logwarn("Traffic Light is: " + label)

        if label == 'Green':
            return TrafficLight.GREEN
        elif label == 'Yellow':
            return TrafficLight.YELLOW
        elif label == 'Red':
            return TrafficLight.RED
        else:
            return TrafficLight.UNKNOWN

