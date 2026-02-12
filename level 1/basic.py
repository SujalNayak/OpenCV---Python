import cv2
img = cv2.imread('image.jpg')
# cv2.imshow('Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

print(type(img))
print(img.shape)

#(342, 512, 3)
#(height, width, channels(BGR))

#blue channel
blue = img[:,:,0]
#green channel
green = img[:,:,1]
#red channel
red = img[:,:,2]

cv2.imshow('Blue', blue)
cv2.imshow('Green', green)
cv2.imshow('Red', red)
cv2.waitKey(0)
cv2.destroyAllWindows()
