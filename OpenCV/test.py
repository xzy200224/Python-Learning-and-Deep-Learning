import cv2
import numpy as np

# 读取图像
image = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)

# 定义Sobel算子
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# 应用Sobel算子
edges_x = cv2.filter2D(image, -1, sobel_x)
edges_y = cv2.filter2D(image, -1, sobel_y)

# 显示结果
cv2.imshow('Original Image', image)
cv2.imshow('Horizontal Edges', edges_x)
cv2.imshow('Vertical Edges', edges_y)
cv2.waitKey(0)
cv2.destroyAllWindows()
