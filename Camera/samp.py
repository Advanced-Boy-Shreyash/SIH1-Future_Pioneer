import cv2
import pickle

width, height = 107, 48

try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []


def drawRectangle(action, x, y, flags, *userdata):
    global top_left_corner, bottom_right_corner, image

    if action == cv2.EVENT_LBUTTONDOWN:
        top_left_corner = [(x, y)]
    elif action == cv2.EVENT_LBUTTONUP:
        bottom_right_corner = [(x, y)]
        cv2.rectangle(image, top_left_corner[0], bottom_right_corner[0], (0, 255, 0), 2)
        cv2.imshow("Image", image)
        posList.append((top_left_corner[0], bottom_right_corner[0]))

    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)


# Read Images
image = cv2.imread('carParkImg.png')
temp = image.copy()
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", drawRectangle)

while True:
    for pos in posList:
        cv2.rectangle(image, pos[0], pos[1], (255, 0, 255), 2)


    cv2.imshow("Image", image)
    k = cv2.waitKey(1)

    if k == 99:  # Clear the rectangles
        image = temp.copy()
        posList = []
        with open('CarParkPos', 'wb') as f:
            pickle.dump(posList, f)
            cv2.imshow("Image", image)
    elif k == 27:  # Press Esc to exit
        break

