import cv2
import matplotlib.pyplot as plt

path = 'images/val/images\ILSVRC2012_val_00000001.JPEG'
img = cv2.imread(path, 3)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

