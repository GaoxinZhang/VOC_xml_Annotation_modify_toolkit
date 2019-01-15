# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# % severity_level.py
# % The Output is the severity level of object in annotation.
# % 4-8-2018 Created
# % Author:Zhang
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
from __future__ import division
import xml.dom.minidom as minidom
import os
import cv2 as cv


src_path = "C:\Users\Hancy\Desktop\Scratch_level"
result_path = "C:\Users\Hancy\Desktop\Scratch_level"
load_xml_path = os.path.join(src_path, 'Annotations')
load_img_path = os.path.join(src_path, 'JPEGImages')
save_xml_path = os.path.join(result_path, 'Annotations_severity_level')
save_img_path = os.path.join(result_path, 'JPEGImages_severity_level')

if not os.path.exists(save_xml_path):
    os.makedirs(save_xml_path)
    print save_xml_path + ' was built'

if not os.path.exists(save_img_path):
    os.makedirs(save_img_path)
    print save_img_path + ' was built'

def severity_level(xml_name):

    (shotname, extension) = os.path.splitext(xml_name)
    img_full_name = shotname + '.jpg'
    input_img_file_path = os.path.join(load_img_path, img_full_name)
    annotation = minidom.parse(os.path.join(load_xml_path, xml_name))

    object = annotation.getElementsByTagName("object")
    image = cv.imread(input_img_file_path)

    for obj in object:
        label_name = obj.getElementsByTagName("name")[0].childNodes[0].nodeValue
        label_name = str(label_name)
        cropImg = img_crop(image, obj)
        edg_level = edge_detection(cropImg,img_full_name)
        new_label_name = label_name + str(edg_level)
        obj.getElementsByTagName("name")[0].childNodes[0].nodeValue = unicode(str(new_label_name), encoding='utf-8')
        print 'xml_name: ' + xml_name + 'label_name: ' + label_name + ' severity level is ' + str(edg_level)

    f = open(os.path.join(save_xml_path, xml_name), 'w')
    annotation.writexml(f, encoding='utf-8')
    f.close()


def edge_detection(image,img_full_name):

    blurred = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_RGB2GRAY)
    # gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    edge_output = cv.Canny(xgrad, ygrad, 50, 150)
    cv.imshow("edge", edge_output)


    mean = edge_output.mean()
    crop_img_name = str(int(mean)) + img_full_name
    crop_img_file_path = os.path.join(save_img_path, crop_img_name)
    cv.imwrite(crop_img_file_path, edge_output)
    print mean
    if mean >= 0 and mean < 128:
        edg_level = 0
    if mean >= 128 and mean <= 255:
        edg_level = 1
    else:
        print('mean error')
    return edg_level

def img_crop(image,object):

    xmin = object.getElementsByTagName("xmin")[0].childNodes[0].nodeValue
    xmin = int(str(xmin))
    xmax = object.getElementsByTagName("xmax")[0].childNodes[0].nodeValue
    xmax = int(str(xmax))
    ymin = object.getElementsByTagName("ymin")[0].childNodes[0].nodeValue
    ymin = int(str(ymin))
    ymax = object.getElementsByTagName("ymax")[0].childNodes[0].nodeValue
    ymax = int(str(ymax))
    bdn_width = xmax - xmin
    bdn_height = ymax - ymin
    cropImg = image[ymin:ymin + bdn_height, xmin:xmin + bdn_width]
    return cropImg

if __name__ == "__main__":
    xml_files = os.listdir(load_xml_path)
    for one in xml_files:
        print(one)
        severity_level(one)
