import cv2

def image_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread('image.jpg')
h,w,c = img.shape
print(f"Height: {h}, Width: {w}, Channels: {c}")
# image_show("Image", img)


#resized img
resized = cv2.resize(img,(200,200))
# image_show("Resized", resized)

#crop img
cropped = img[100:300, 100:300]
# image_show("Cropped", cropped)

#rotate img
center = (w//2, h//2)
rotation_matrix = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated = cv2.warpAffine(img, rotation_matrix, (w,h))
# image_show("Rotated", rotated)

#flip img
flipped = cv2.flip(img, -1) # 0: vertical, 1: horizontal, -1: both
image_show("Flipped", flipped)
cv2.imwrite('flipped_image.jpg', flipped)