from PIL import Image
import os,sys
import numpy as np
import time


def convert(read_dir, save_dir, image_format):
    file_list = os.listdir(read_dir)
    # print(file_list)
    for filename in file_list:
        path = read_dir + filename
        Image.open(path).save(save_dir + filename[:-4] + image_format)
        # print "%s has been changed!" % filename


def Image2Numpy(img_dir):
    file_list = os.listdir(img_dir)
    len_images = len(file_list)
    imgs_matrix = np.zeros((len_images, 600, 600, 3))
    img_index = 0
    total_fsize = 0
    for filename in file_list:
        path = img_dir + filename
        img = np.array(Image.open(path))
        fsize = os.path.getsize(path)
        fsize = fsize / float(1024 * 1024) # B-->KB-->MB
        total_fsize += fsize
        imgs_matrix[img_index] = img
    return round(total_fsize, 2)


def timeandspace(img_dir):
    time_start = time.time()
    space = Image2Numpy(img_dir)
    images_len = len(os.listdir(img_dir))
    time_end = time.time()
    print('Number of images: ' + str(images_len))
    print("Image Totally takes %.2f MB " % space)
    print('Totally takes %.3fs for Converting to numpy' % (time_end - time_start))

if __name__ == '__main__':
   read_dir = 'C:\Users\Hancy\Desktop\Boeing\VR\ALL_VR_IMAGE\\'
   save_dir = 'C:\Users\Hancy\Desktop\Boeing\VR\ALL_VR_IMAGE_convert\\'
   Image_format = '.bmp'

   if not os.path.exists(save_dir):
       os.makedirs(save_dir)
       print (save_dir + ' was built')

   convert(read_dir, save_dir, Image_format)
   print('#1 JPEG')
   timeandspace(read_dir)

   print('#2 BMP')
   timeandspace(save_dir)



