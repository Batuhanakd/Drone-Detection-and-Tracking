#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 16:38:57 2021

@author: batuhan
"""

import cv2

objectName = "Drone"
frameWidth = 720
frameHeight = 1080
color = (255,0,255)

cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)

def empty(a):pass

# trackbar
cv2.namedWindow("Sonuc")
cv2.resizeWindow("Sonuc", frameWidth + 50, frameHeight + 100)
cv2.createTrackbar("Scale","Sonuc",400,1000,empty)
cv2.createTrackbar("Neighbor","Sonuc",40,1000,empty)

# cascade classifier
cascade = cv2.CascadeClassifier("cascade.xml")

while True:
    
    # read img
    success, img = cap.read()
    
    if success:
        # convert bgr2gray
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # detection parameters
        scaleVal = 1 + (cv2.getTrackbarPos("Scale","Sonuc")/1000)
        neighbor = cv2.getTrackbarPos("Neighbor","Sonuc")
        # detectiom
        rects = cascade.detectMultiScale(gray, scaleVal, neighbor)
    
        for (x,y,w,h) in rects:
            #en büyük bul
	    #x+w*y+h tan en büyük olan rect gözükecek 
            cv2.rectangle(img, (x,y),(x+w,y+h), color, 3)
            cv2.putText(img, objectName, (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            
        cv2.imshow("Sonuc", img)
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break




