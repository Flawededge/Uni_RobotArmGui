import math
import numpy as np
import cv2

L1 = 220
L2 = 190


# def calculate_angle(x, y):
#     theta1 = math.atan2(y, x)
#     L = math.sqrt(x**2 + y**2)
#     theta1 += math.acos((L ** 2 + L1 ** 2 - L2 ** 2) / (2 * L1 * L2))
#
#     theta2 = math.acos((L2 ** 2 + L1**2 - L**2) / (2*L1*L2))
#
#     return math.degrees(theta1), math.degrees(theta2)

def calculate_angle(x, y):
    Q2 = math.acos((x**2 + y**2 - L1**2 - L2**2) / (2*L1*L2))
    Q1 = math.atan2(y, x) - math.atan((L2 * math.sin(L2)) / (L1 + L2*math.cos(Q2)))
    return math.degrees(Q1), math.degrees(Q2)

workingImage = np.zeros((1000, 1000, 3), np.uint8)  # Create the empty image (y, x)

for x in range(-500, 500):
    for y in range(-500, 500):
        try:
            theta1, theta2 = calculate_angle(x, y)
            if 195 > theta1 > -15:
                workingImage[x+500, y+500] = (255, 255, 255)
            else:
                # print(theta1, theta2)
                workingImage[x+500, y+500] = (0, 0, 0)
        except:
            workingImage[x+500, y+500] = (0, 0, 255)

        if x%50 == 0 or y%50 == 0:
            workingImage[x+500, y+500] = (0, 255, 0)

cv2.imshow("Disp", workingImage)
cv2.waitKey(0)