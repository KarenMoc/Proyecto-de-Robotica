#!/usr/bin/env python

import os
import numpy as np
import cv2

s = "El respeto al derecho ageno es la paz"

os.system("gnome-terminal -e 'rosrun sound_play soundplay_node.py'")
os.system("gnome-terminal -e 'rosrun sound_play say.py \"Viva mexico cabrones, emiliano come pito\"'")

img = cv2.imread('hidalgo.jpg')
cv2.imshow('image',img)
cv2.waitKey(5000)
cv2.destroyAllWindows()

