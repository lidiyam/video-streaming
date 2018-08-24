# producer.py
from __future__ import print_function

import time
import cv2
from kafka import KafkaProducer, KafkaClient
#  connect to Kafka
#kafka = KafkaClient('localhost:9092')
#producer = KafkaProducer(kafka)
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Assign a topic
topic = 'my-topic'

def video_emitter(video):
    # Open the video
    video = cv2.VideoCapture(video)
    print(' emitting.....')

    # read the file
    while (video.isOpened):
        # read the image in each frame
        success, image = video.read()
        # check if the file has read to the end
        if not success:
            break
        # convert the image png
        ret, jpeg = cv2.imencode('.png', image)
        # Convert the image to bytes and send to kafka
        producer.send(topic, jpeg.tobytes())
        # To reduce CPU usage create sleep time of 0.2sec  
        time.sleep(0.2)
    # clear the capture
    video.release()
    print('done emitting')

if __name__ == '__main__':
    video_emitter('video.mp4')

