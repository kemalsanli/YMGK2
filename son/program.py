import emine
import fatih
import cv2
import numpy as np
gelendeger=[207,192,0,74,230,6,155,195,0,118,210,155,250,83,184,194,112,220,68,126,12,7,185,255,89,234,249,47,216,148,125,165,111,120,199,249,219,61,78,88,18,11,169,206,23,125,40,42,75,43,183,72,144,38,77,183,162,189,171,214,208,144,248,169]
y=emine.randomsayi(gelendeger)
demo = cv2.imread("koala.jpeg")

fatih.resim(y,demo)