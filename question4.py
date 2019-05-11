import cv2
import numpy as np


def label_regions(fr, lc, label):
    frontier = [lc[0]]
    lc.remove(lc[0])
    explored = []
    while True:
        loc = frontier[0]
        frontier.remove(loc)
        explored.append(loc)
        up = [loc[0] + 1, loc[1]]
        down = [loc[0] - 1, loc[1]]
        left = [loc[0], loc[1] - 1]
        right = [loc[0], loc[1] + 1]
        up_left = [loc[0] + 1, loc[1] - 1]
        up_right = [loc[0] + 1, loc[1] + 1]
        down_left = [loc[0] - 1, loc[1] - 1]
        down_right = [loc[0] - 1, loc[1] + 1]
        checks = [up, down, left, right, up_left, up_right, down_left, down_right]
        for i in checks:
            if fr.shape[0] > i[0] >= 0 and fr.shape[1] > i[1] >= 0:
                if fr[i[0], i[1]] == 'W':
                    if (i[0], i[1]) not in explored:
                        frontier.append((i[0], i[1]))
                        lc.remove((i[0], i[1]))
                        fr[i[0], i[1]] = str(label)
        if len(frontier) == 0:
            break
    return fr, lc


def bfs(ir):
    white = np.where(ir == 'W')
    white_list = []
    count = 1
    final_regions = np.array(ir.copy())
    for k in range(len(white[0])):
        white_list.append((white[0][k], white[1][k]))
    while True:
        final_regions, white_list = label_regions(final_regions, white_list, count)
        count = count + 1
        if len(white_list) == 0 or count > len(white_list):
            break
    print("Segmentation Complete")
    print('White regions found :', (count-1))
    return final_regions


print("Reading Image")
image = np.array(cv2.imread("binary1.png", 0))
for i in image:
    for j in range(len(i)):
        if i[j] > 170:
            i[j] = 255
        else:
            i[j] = 0
image = cv2.resize(image, (225, 225))
imageRegion = np.array(image.copy())
imageRegion = imageRegion.astype(str)
print("Image Read Complete")
for i in imageRegion:
    for j in range(len(i)):
        if i[j] == '0':
            i[j] = 'B'
        else:
            i[j] = 'W'
print("Starting Segmentation")
final_ans = bfs(imageRegion)

cv2.imshow("Final Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
