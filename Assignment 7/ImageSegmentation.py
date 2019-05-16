import cv2

imgray = cv2.imread('C:/Users/Administrator/Desktop/AI/BinaryImage1.png',cv2.IMREAD_GRAYSCALE)
thresh = 127
img = cv2.threshold(imgray, thresh, 255, cv2.THRESH_BINARY)[1]

def neighbour_search(img, pioneer_point, counter_value):
    queue = [pioneer_point]
    traversed_segment = []
    while queue != []:
        current_point = queue.pop(0)
        img[current_point[0]][current_point[1]] = counter_value + 1
        if current_point not in traversed_segment:
            traversed_segment.append(current_point)
        for i in range(current_point[0]-1,current_point[0]+2):
            for j in range(current_point[1]-1, current_point[1]+2):
                if ([i,j] not in traversed_segment) and img[i][j]>counter_value:
                    queue.append([i,j])
                    traversed_segment.append([i,j])

def white_pixel(img, counter_value):
    m = len(img)
    n = len(img[0])
    flag = 0
    for i in range (1, m):
        for j in range (1, n):
            if img[i][j]> counter_value:
                flag = 1

    if flag == 1:
        return True
    else:
        return False


def img_seg(img):
    counter_value = 0
    m = len (img)
    n = len (img[0])
    while white_pixel(img, counter_value) == True:
        for i in range (1, m):
            flag = 0
            for j in range (1, n):
                if img[i][j]>counter_value:
                    flag = 1
                    pioneer_point = [i, j]
                    break
            if flag != 0:
                break

        neighbour_search(img, pioneer_point, counter_value)
        counter_value += 1

    print (counter_value)

img_seg(img)

