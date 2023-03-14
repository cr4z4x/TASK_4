import cv2
import matplotlib.pyplot as plt
import numpy as np




def gray(arry):
    h=arry.shape[0]
    w=arry.shape[1]
    grey_frame = np.zeros((h, w), dtype=np.uint8)   
    for i in range(h):
        for j in range(w):
           
            blue,green,red=arry[i][j]
            
            gray_value=int(0.299 * red + 0.587 * green + 0.114 * blue)

            grey_frame[i][j]=gray_value
    return grey_frame




def flatten_array(arr):
    flat_array = []

    for item in arr:
        if (type(item) == list):
            # using recursion
            nested_list = flatten_array(item)
            flat_array.extend(nested_list)
        else:
            flat_array.extend(item)

    return flat_array





cap = cv2.VideoCapture(0)   
while(True):

    ret, frame = cap.read()

    light=gray(frame)
    
    
    cv2.imshow("BW",light)

    plt.xlabel("Shade of gray")
    plt.ylabel("Occurourences")
    flat=flatten_array(light)
    plt.hist(flat,256,[0,255])

    plt.title("Histogram")
    plt.draw()
    plt.pause(0000.1)
    plt.clf()

    if cv2.waitKey(1) & 0xFF == ord('/'):
        break