import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened(): #Test whether webcam works perfectly or not
    print("Cannot open camera")
    exit()

cv.namedWindow("Capture for dataset")
image_counter = 0 #counter for naming captured images

while True:
    ret, frame = cap.read()

    if not ret:
        print("Problem in capturing frame")
        break

    cv.imshow("Capturing Window", frame)

    k = cv.waitKey(1) #waitkey(1) allows continous capture, waitkey(0) allows for a still photograph
    if (k%256 == 27):
        print("Closing the window...") #always press esc to exit and not close the window
        break
    elif (k%256 == 32):
        img_name = "webcam_opencv_no_1_{}.jpg".format(image_counter)
        cv.imwrite(img_name, frame)
        print("Captured!")
        image_counter += 1


#release all windows
cap.release()
cv.destroyAllWindows()