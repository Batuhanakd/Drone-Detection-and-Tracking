#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 09:13:55 2021

@author: batuhan
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

#resmi içe aktar
img = cv2.imread("sudoku.png",0)
img = np.float32(img)
print(img.shape)
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off")

#harris corner detection
dst = cv2.cornerHarris(img, blockSize = 12, ksize = 5, k = 0.02)
plt.figure(), plt.imshow(dst, cmap = "gray"), plt.axis("off")

