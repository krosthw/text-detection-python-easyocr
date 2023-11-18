#!/usr/bin/env python3.8
import cv2
import easyocr
import matplotlib.pyplot as plt
from itertools import islice
import numpy as np
import sys
import csv
import os
import torch
from functools import partial
from random import randint
from main import calc2

def randints(count, *randint_args):
    ri = partial(randint, *randint_args)
    return [(ri()) for _ in range(count)]

readerEasyocr = easyocr.Reader(['en','it'], gpu=False,verbose=False)

fileName = "demofile.txt"
if os.path.exists(fileName):
  os.remove(fileName)
f = open(fileName, "w")


#image,name,author,format,book_depository_stars,price,currency,old_price,isbn,category,img_paths
with open("./data/bookCoverDataset/main_dataset.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    
    # for row in islice(reader, 10):
    rows = list(reader)
    totalrows = len(rows)
    numm = randints(20,1,totalrows)

    #for t in numm:
    for t in range(totalrows):
        row =  rows[t]
        author = row['author']
        name = row['name']
        img_paths = row['img_paths']
        
        path = "./data/bookCoverDataset/" + row['img_paths']
        res = calc2(path,readerEasyocr)
        scoreTitle = 0
        scoreAuthor = 0
        for p in res:
            if(p.lower() in author.lower()):
                scoreAuthor+=1
                #print(p)
            if(p.lower() in name.lower()):
                scoreTitle+=1
                #print(p)
        
        
        # print(author," | ", name," | ", img_paths)
        
        nA =len(author.split(" "))
        nN = len(name.split(" "))
        
        pA = (scoreAuthor/nA)*100
        pN = (scoreTitle/nN)*100
        #print(scoreAuthor)
        # print(nA)
        # print(pA)
        
        #print(scoreTitle)
        # print(nN)
        # print(pN)
        final = author +" | "+ name + " => "+ ";".join(res)+ " => ["+"%.2f" % round(pA, 2)+","+ "%.2f" % round(pN, 2)+"]"+ "\n"
        print("["+ str(t) + "/" + str(totalrows) + "]")
        print("\t" + final)
        f.write(final)
#input()              
f.close()