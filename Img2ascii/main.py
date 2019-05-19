import sys
import cv2

step_x_size=2
step_y_size=4
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

#calculate the mean of an area in the imge



if __name__ == "__main__":

    rimg_path=sys.argv[1]
    #rimg_path="./test/img/fish.jpg"
    #we should check if the file exit
    #
    # get a img
    rimg=cv2.imread(rimg_path)
    timg=cv2.cvtColor(rimg,cv2.COLOR_RGB2GRAY)
    #timg = cv2.equalizeHist(timg)
    #ret,timg = cv2.threshold(timg,127,255,cv2.THRESH_BINARY)
    # timg = cv2.Canny(timg,100,200)

    x=0
    y=0
    mean=0
    while y<timg.shape[0]:
        if y+step_y_size>timg.shape[0]:
            break
        x=0
        while x<timg.shape[1]:
            if x+step_x_size>timg.shape[1]:
                break
            mean=0
            for i in range(step_y_size):
                for j in  range(step_x_size):
                    mean+=timg[y+i,x+j]
            print(ascii_char[int(mean/(step_y_size*step_x_size)/255*(len(ascii_char)-1))],end="")
            x+=step_x_size
        print()
        y+=step_y_size

    #shold the img
    print(timg.shape)
    print(len(ascii_char))
    cv2.imshow("Test",timg)
    cv2.waitKey(0)