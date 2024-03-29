import cv2
import glob
import os.path

#Creates a list of files that has extension jpg, jpeg and png in the current dir.
jpg = glob.glob("*.jpg")
jpeg = glob.glob("*.jpeg")
png = glob.glob("*.png")
images = jpg + png + jpeg

#max image size in bytes
#300 000 is 300kb
#max_size = 300000
max_size = 2000000
factor = 1.5

for image in images:
    while True:
        if (os.path.getsize(image) > max_size):
            curr_img = cv2.imread(image, 1)
            
            #Keep the aspect ration
            re = cv2.resize(curr_img, (int(curr_img.shape[1]/factor), int(curr_img.shape[0]/factor)))
            
            #Just for show..
            cv2.imshow("checking", re)
            cv2.waitKey(500)
            cv2.destroyAllWindows()

            cv2.imwrite(image, re)
        else:
            break