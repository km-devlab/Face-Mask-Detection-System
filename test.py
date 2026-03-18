import cv2
import imutils
cap = cv2.VideoCapture(0)
#cap.set(5,20)
print(cap.get(5))

while(cap.isOpened()):
    #read the frame
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=400)
    frame = cv2.flip(frame,1)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()




