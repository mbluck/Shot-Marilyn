import cv2 
import numpy as np
import pandas as pd
import itertools as it

#import images
og = cv2.imread('assets/original.png')
orange = cv2.imread('assets/orange.png')
blue = cv2.imread('assets/blue.jpg')
red = cv2.imread('assets/red.png')
turq = cv2.imread('assets/turq.png')
sage = cv2.imread('assets/sage.png')

#cv2.imread() does NOT throw errors
for file in [og, orange, blue, red, turq, sage]:
    if np.shape(file) == ():
        print(f'ERROR: {file} not found on import')

#convert rgb to hsv
hsv_og = cv2.cvtColor(og, cv2.COLOR_BGR2HSV)
hsv_orange = cv2.cvtColor(orange, cv2.COLOR_BGR2HSV)
hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
hsv_turq = cv2.cvtColor(turq, cv2.COLOR_BGR2HSV)
hsv_sage = cv2.cvtColor(sage, cv2.COLOR_BGR2HSV)

'''
ORGANIZE DATA
above, each image has been converted to a 3d array
the third dimension contains the hsv values in the form [h, s, v]
slice the arrays to extract these values, as below:
'''
og_df = pd.DataFrame({'Color':it.repeat('original', len(og[:,:,0].flatten())),
                        'Hue':og[:,:,0].flatten(),
                        'Saturation':og[:,:,1].flatten(),
                        'Value':og[:,:,2].flatten()})
orange_df = pd.DataFrame({'Color':it.repeat('orange', len(orange[:,:,0].flatten())),
                          'Hue':orange[:,:,0].flatten(),
                          'Saturation':orange[:,:,1].flatten(),
                          'Value':orange[:,:,2].flatten()})
red_df = pd.DataFrame({'Color':it.repeat('red', len(red[:,:,0].flatten())),
                        'Hue':red[:,:,0].flatten(),
                        'Saturation':red[:,:,1].flatten(),
                        'Value':red[:,:,2].flatten()})
turq_df = pd.DataFrame({'Color':it.repeat('turq', len(turq[:,:,0].flatten())),
                        'Hue':turq[:,:,0].flatten(),
                        'Saturation':turq[:,:,1].flatten(),
                        'Value':turq[:,:,2].flatten()})
blue_df = pd.DataFrame({'Color':it.repeat('blue', len(blue[:,:,0].flatten())),
                        'Hue':blue[:,:,0].flatten(),
                        'Saturation':blue[:,:,1].flatten(),
                        'Value':blue[:,:,2].flatten()})
sage_df = pd.DataFrame({'Color':it.repeat('sage', len(sage[:,:,0].flatten())),
                        'Hue':sage[:,:,0].flatten(),
                        'Saturation':sage[:,:,1].flatten(),
                        'Value':sage[:,:,2].flatten()})
all_data = pd.concat([og_df, orange_df, red_df, turq_df, blue_df, sage_df])

all_data.to_csv('data/hsv_data.csv', index=False)


