# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# % Resize_annotation_in_xml.py
# % To resize annotation in xml file.
# % 4-7-2018 Created
# % Author:Zhang
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
from __future__ import division
import xml.dom.minidom as minidom
from scipy import misc
import os
from PIL import Image


# target image size
desired_width = 600
desired_height = 600

root_path = "G:\Boeing_reannotated0509"
result_path = "G:\Boeing_reannotated0509"

load_xml_path = os.path.join(root_path, 'Annotations_reannotated0509')
# load_img_path = os.path.join(root_path, 'JPEGImages')

save_xml_path = os.path.join(result_path, 'Annotations_reannotated0509_all_resized')
# save_img_path = os.path.join(result_path, 'JPEGImages_resize')

isExists = os.path.exists(save_xml_path)
if not isExists:
    os.makedirs(save_xml_path)
    print save_xml_path + ' was built'

def caculate_ratio(primary_w, primary_h,
                   desired_w=desired_width, desired_h=desired_height):
    w_ratio = desired_w/primary_w
    h_ratio = desired_h/primary_h
    return w_ratio, h_ratio


def resize_xml_pic(xml_name, desired_w=desired_width, desired_h=desired_height):

    # (shotname, extension) = os.path.splitext(xml_name)
    # img_full_name = shotname + '.jpg'
    # input_img_file_path = os.path.join(load_img_path, img_full_name)
    # output_img_file_path = os.path.join(save_img_path, img_full_name)
    annotation = minidom.parse(os.path.join(load_xml_path, xml_name))

    size = annotation.getElementsByTagName("size")
    width = size[0].getElementsByTagName("width")[0].childNodes[0].nodeValue
    height = size[0].getElementsByTagName("height")[0].childNodes[0].nodeValue
    width = int(str(width))
    height = int(str(height))

    size[0].getElementsByTagName("width")[0].childNodes[0].nodeValue = unicode(str(desired_w), encoding = 'utf-8')
    size[0].getElementsByTagName("height")[0].childNodes[0].nodeValue = unicode(str(desired_h), encoding = 'utf-8')

    w_ratio, h_ratio = caculate_ratio(width, height)

    # isExists = os.path.exists(save_img_path)
    # if not isExists:
    #     os.makedirs(save_img_path)
    #     print save_img_path + ' was built'


    # img = misc.imread(input_img_file_path)
    # image = misc.imresize(img, (desired_w, desired_h))
    # misc.imsave(output_img_file_path, image)

    # img = Image.open(input_img_file_path)
    # image = img.resize((desired_w, desired_h))
    # misc.imsave(output_img_file_path, image)

    object = annotation.getElementsByTagName("object")
    for obj in object:

        # label_name = obj.getElementsByTagName("name")[0].childNodes[0].nodeValue
        # label_name = str(label_name)
        # for one in bndbox:
        xmin = obj.getElementsByTagName("xmin")[0].childNodes[0].nodeValue
        xmin = int(str(xmin))
        obj.getElementsByTagName("xmin")[0].childNodes[0].nodeValue = unicode(str(int(w_ratio * xmin)),
                                                                              encoding='utf-8')
        xmax = obj.getElementsByTagName("xmax")[0].childNodes[0].nodeValue
        xmax = int(str(xmax))
        obj.getElementsByTagName("xmax")[0].childNodes[0].nodeValue = unicode(str(int(w_ratio * xmax)),
                                                                              encoding='utf-8')
        ymin = obj.getElementsByTagName("ymin")[0].childNodes[0].nodeValue
        ymin = int(str(ymin))
        obj.getElementsByTagName("ymin")[0].childNodes[0].nodeValue = unicode(str(int(h_ratio * ymin)),
                                                                              encoding='utf-8')
        ymax = obj.getElementsByTagName("ymax")[0].childNodes[0].nodeValue
        ymax = int(str(ymax))
        obj.getElementsByTagName("ymax")[0].childNodes[0].nodeValue = unicode(str(int(h_ratio * ymax)),
                                                                              encoding='utf-8')


    f = open(os.path.join(save_xml_path, xml_name), 'w')
    annotation.writexml(f, encoding='utf-8')
    f.close()

if __name__ == "__main__":
    xml_files = os.listdir(load_xml_path)
    for one in xml_files:
        resize_xml_pic(one)
        # print(one + ' and jpg has been resized successfully')
        print(one + '  has been resized successfully')
