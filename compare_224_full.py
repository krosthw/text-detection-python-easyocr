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

fileName224 = "demofile_book_dataset_test_224.txt"
fileNameFull = "demofile_book_dataset_test_full.txt"
with open(fileName224) as file224:
    with open(fileNameFull) as fileFull:
        lines224 = file224.readlines()
        linesFull = fileFull.readlines()
        totalrows224 = len(lines224)
        totalrowsFull = len(linesFull)
        print(totalrows224)
        print(totalrowsFull)
        numm = randints(10,1,totalrowsFull)
        
        eq = 0
        eqA = 0
        eqT = 0
        AwinFull = 0
        Awin224 = 0
        TwinFull = 0
        Twin224 = 0
        #for t2 in numm:
        for t2 in range(0,totalrows224,1):
            if("[" in lines224[t2]):
                v224 = lines224[t2].split("[")[-1].replace("]",",")
                vFull = linesFull[t2].split("[")[-1].replace("]",",")
                author224 = v224.split(",")[0]
                title224 = v224.split(",")[1]
                authorFull = vFull.split(",")[0]
                titleFull = vFull.split(",")[1]
                print(t2,":\t",author224, title224,authorFull,titleFull)
                i_author224  = float(author224 )
                i_title224   = float(title224)
                i_authorFull = float(authorFull)
                i_titleFull  = float(titleFull )
                if(i_author224 ==i_authorFull and i_title224 == i_titleFull):
                    eq +=1
                else:
                    
                    if(i_author224 > i_authorFull):
                        Awin224 +=1
                        print(lines224[t2])
                        print(linesFull[t2])
                    elif(i_author224 == i_authorFull):
                        eqA +=1
                    else:
                        AwinFull +=1
                    if(i_title224 > i_titleFull):
                        Twin224 +=1
                    elif(i_title224 == i_titleFull):
                        eqT +=1
                    else:
                        TwinFull +=1
        print("eq_: ", str(eq))
        print("eqA: ", str(eqA))
        print("eqT: ", str(eqT))
        print("224: ", str(Awin224),str(Twin224))
        print("ful: ", str(AwinFull),str(TwinFull))