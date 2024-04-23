#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


harcascade = "haarcascade_russian_plate_number.xml"


# In[3]:


min_area = 500


# In[4]:


cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, frame = cap.read()
    plate_cascade = cv2.CascadeClassifier(harcascade)
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    plate = plate_cascade.detectMultiScale(gray_img, 1.2, 5)

    for (x,y,w,h) in plate:
        area = w*h
        if area > min_area:
            cv2.rectangle(frame , (x,y), (x+w,y+h), (0,255,0), 2)
            cv2.putText(frame, "Number Plate", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,(255,0,0),2)

            image_roi = frame[y:y+h, x:x+w]
            cv2.imshow("ROI", image_roi)

    cv2.imshow("Result", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('v'):
        cv2.imwrite("plates/detected_plate" + str(count) + ".jpg", image_roi)
        cv2.rectangle(frame, (0,200), (640,300), (0,255,0), cv2.FILLED)
        cv2.putText(frame, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 0, 0), 2)
        cv2.imshow("Results",frame)
        cv2.waitKey(500)
        count += 1

cap.release()
cv2.destroyAllWindows()


# In[ ]:




