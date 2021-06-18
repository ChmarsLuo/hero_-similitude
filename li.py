import cv2
import os
from PIL import Image
import glob
from siamese import Siamese



if  __name__ == "__main__":
    model = Siamese()
    testA_path = r"C:\Users\yeluo\Desktop\li\ZhouYu\A"
    testB_path = r"C:\Users\yeluo\Desktop\li\ZhouYu\B"
    save_path = r"C:\Users\yeluo\Desktop\ZhouYu_result"
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    images = os.listdir(testA_path)
    for im in images:
        name1 = os.path.join(testA_path, im)
        name2 = os.path.join(testB_path, im)
        image1 = Image.open(name1)
        image2 = Image.open(name2)
        # print(image1, image2)
        probability = model.detect_image(image1, image2,save_path=os.path.join(save_path,im))
        print("name and probability:",im,probability)
        # if probability < 0.98:
        #     image1.save(os.path.join(save_path,image1))
        #     image2.save(os.path.join(save_path,image2))