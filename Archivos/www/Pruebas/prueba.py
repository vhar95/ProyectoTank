import cv2
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)
rval, frame = vc.read()
while rval:
	cv2.imshow("preview", frame)
	rval, frame = vc.read()
 	key = cv2.waitKey(20)
	if key == 27:
		break
cv2.destroyWindow("preview")



