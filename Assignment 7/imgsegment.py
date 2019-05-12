import cv2
import copy
image=cv2.imread('image.png')
def search_white(img):
    temp=copy.deepcopy(img)
    temp=temp.tolist()
    for i in range(len(img)):
        for j in range(len(img[i])):
            temp[i][j].append('U')
    for i in range(len(img)):
        for j in range(len(img[i])):
            if(img[i][j][0]==0 and img[i][j][1]==0 and img[i][j][2]==0):
                for k in range(3):
                    temp[i][j][k]='L'

search_white(image)
