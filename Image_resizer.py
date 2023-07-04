import cv2

# Image path and name
image_path = "C:/Users/fayis/Desktop/5 py projects/QR Code/img/DHIU_Main_Block_copy.jpg"  

# Read the image file in each pixel.
# This returns set of numpy arrays
img_data = cv2.imread(image_path,cv2.IMREAD_UNCHANGED)

# Percentage of New image to be resized
percent = 60/100

# Resizing the image dimension according to the percentage which is given
new_height = int(img_data.shape[1]*percent)
new_width = int(img_data.shape[0]*percent)
new_dimensions= (new_height,new_width)

new_image = cv2.resize(img_data,new_dimensions,interpolation= cv2.INTER_AREA)

# Show the Resized image 
if new_image is not None:
    cv2.imshow('new_image', new_image)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()
else:
    print("Failed to load the new image. Please check the file path.")

# Save the image as new file
status = cv2.imwrite('C:/Users/fayis/Desktop/5 py projects/QR Code/img/Resized_Image.png',new_image)
if status == True:
    print('Image has been resized and saved succesfully. Thank you for supporting')
else:
    print('Couldn\'t save the image')