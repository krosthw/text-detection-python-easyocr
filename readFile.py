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

fileName = "demofileFull.txt"
with open(fileName) as file:
    lines = file.readlines()
    totalrows = len(lines)
    numm = randints(10,1,totalrows)
    # for t in numm:
    #     print(str(t) + " : " + lines[t])
    # for t1 in range(0,totalrows,1):
    #     if("100" in lines[t1]):
    #         print(str(t1) + " : " + lines[t1])
    i = 0
    for t2 in range(0,totalrows,1):
        if("100.00" in lines[t2]):
            print(str(t2) + " : " + lines[t2])            
            i+=1
    print(i)
    print(i/totalrows*100)