#pip install opencv-python
#pip install numpy

from cv2 import cv2
import numý as np
#carregando a imagem

img = cv2.imread(r'imperia.png')

cinza = cv2.ctColor(img, cv2.COLOR_GRAY)
