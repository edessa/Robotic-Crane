/usr/bin/python

import sys
import time
import socket
import cv2.cv as cv
import cv2
import numpy as np
import pickle

#initialize UDP socket
IP = "127.0.0.1"
PORT = 5010

send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    ret, frame2 = cap2.read()
    resized_img = cv2.resize(frame, (80, 60))
    resized_img2 = cv2.resize(frame2, (80,60))
    cv2.imshow('small', resized_img)
    cv2.imshow('other', resized_img2)
    cv2.waitKey(10)

    send.sendto(resized_img, (IP, PORT))
    send.sendto(resized_img2, (IP, PORT))
    
    time.sleep(.01)
