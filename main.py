#!/usr/bin/env python3.8
import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np
import sys
 
def calc(image_path):
    
    # total arguments
    #print("using image: "+ image_path)

    img = cv2.imread(image_path)

    # instance text detector
    reader = easyocr.Reader(['en','it'], gpu=False,verbose=False)

    # detect text on image
    text_ = reader.readtext(img)

    threshold = 0.25
    # draw bbox and text

    res = enumerate(text_)
    areas = []
    phrases = []
    for t_, t in res:
        if(t[2] > threshold):
            c1 = t[0][2]
            c2 = t[0][0]
            l = c1[0]- c2[0]
            h = c1[1]- c2[1]
            area = l *h
            #print(h)
            #print(t[1])
            phrases.append(t[1])
            #areas.append([h,t[1]])
    #     bbox, text, score = t
    #     if score > threshold:
    #         cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 5)
    #         cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

    # plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # plt.show(block=False)
    # areas.sort(key = lambda x: x[0] );
    # print(areas)
    # for t1 in areas:
    #     print(str(t1[0]) + " " +t1[1])
    return phrases    
        
def calc2(image_path,reader):
    img = cv2.imread(image_path)
    
    text_ = reader.readtext(img)
    threshold = 0.25
    res = enumerate(text_)
    areas = []
    phrases = []
    for t_, t in res:
        if(t[2] > threshold):
            c1 = t[0][2]
            c2 = t[0][0]
            l = c1[0]- c2[0]
            h = c1[1]- c2[1]
            area = l *h
            phrases.append(t[1])
    return phrases    
        
                
        
        
        
if __name__ == "__main__":
    image_path = 'C:\\Devel\\Experiment\\text-detection-python-easyocr\\data\\'
    n = len(sys.argv)
    image_path += "test4.png"
    if(n == 2):
        image_path += sys.argv[1]
    calc(image_path)