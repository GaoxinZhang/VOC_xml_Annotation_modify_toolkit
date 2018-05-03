# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# % modify_crack.py
# % To modify xml include type 'crack' or any type we want.
# % 4-7-2018 Created
# % Author:Zhang
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
from __future__ import division
import xml.dom.minidom as minidom
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import numpy as np
import cv2
from PIL import Image

plt.rcParams['figure.figsize'] = (10, 10)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

# root_path is a folder where original xml files stored
root_path = "C:\Users\Hancy\Desktop\Boeing_data\Rivets"
# result_path is a folder where converted xml files stored
result_path = "C:\Users\Hancy\Desktop\Boeing_data\Rivets"

load_xml_path = os.path.join(root_path, 'Annotations_N+Rivets_1000')
load_img_path = os.path.join(root_path, 'JPEGImages_N+Rivets_1000')

save_xml_path = os.path.join(result_path, 'Annotations_rivets_trans')
save_img_path = os.path.join(result_path, 'JPEGImages_rivets_trans_ploted')
save_img_path2 = os.path.join(result_path, 'JPEGImages_rivets_trans')

isExists = os.path.exists(save_xml_path)
if not isExists:
    os.makedirs(save_xml_path)
    print save_xml_path + ' was built'

isExists = os.path.exists(save_img_path)
if not isExists:
    os.makedirs(save_img_path)
    print save_img_path + ' was built'

isExists = os.path.exists(save_img_path2)
if not isExists:
    os.makedirs(save_img_path2)
    print save_img_path2 + ' was built'


def rad(x):
    return x * np.pi / 180


def transformPoint(pointToTransform_x, pointToTransform_y, trans_matrix):

    originVector = np.array([[pointToTransform_x], [pointToTransform_y], [1]], dtype='float32')
    # originVector = np.array([pointToTransform_x, pointToTransform_y, 1], dtype='float32')
    transformedVector = trans_matrix.dot(originVector)
    transformed_x = int(transformedVector[0] / transformedVector[2])
    transformed_y = int(transformedVector[1] / transformedVector[2])
    # transformed_x = int(transformedVector[0])
    # transformed_y = int(transformedVector[1])
    # dst = cv2.perspectiveTransform(originVector, trans_matrix)
    return transformed_x, transformed_y
    # return dst

def modify_xml(xml_name):

    (shotname, extension) = os.path.splitext(xml_name)
    img_full_name = shotname + '.jpg'
    input_img_file_path = os.path.join(load_img_path, img_full_name)
    img = cv2.imread(input_img_file_path)
    img = cv2.copyMakeBorder(img, 20, 20, 0, 0, cv2.BORDER_CONSTANT, 0)
    w, h = img.shape[0:2]
    anglex = 0
    angley = 30
    anglez = 0
    fov = 21
    z = np.sqrt(w ** 2 + h ** 2) / 2 / np.tan(rad(fov / 2))

    rx = np.array([[1, 0, 0, 0],
                   [0, np.cos(rad(anglex)), -np.sin(rad(anglex)), 0],
                   [0, -np.sin(rad(anglex)), np.cos(rad(anglex)), 0, ],
                   [0, 0, 0, 1]], np.float32)

    ry = np.array([[np.cos(rad(angley)), 0, np.sin(rad(angley)), 0],
                   [0, 1, 0, 0],
                   [-np.sin(rad(angley)), 0, np.cos(rad(angley)), 0, ],
                   [0, 0, 0, 1]], np.float32)

    rz = np.array([[np.cos(rad(anglez)), np.sin(rad(anglez)), 0, 0],
                   [-np.sin(rad(anglez)), np.cos(rad(anglez)), 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]], np.float32)

    r = rx.dot(ry).dot(rz)

    pcenter = np.array([h / 2, w / 2, 0, 0], np.float32)

    p1 = np.array([0, 0, 0, 0], np.float32) - pcenter
    p2 = np.array([w, 0, 0, 0], np.float32) - pcenter
    p3 = np.array([0, h, 0, 0], np.float32) - pcenter
    p4 = np.array([w, h, 0, 0], np.float32) - pcenter

    dst1 = r.dot(p1)
    dst2 = r.dot(p2)
    dst3 = r.dot(p3)
    dst4 = r.dot(p4)

    list_dst = [dst1, dst2, dst3, dst4]

    org = np.array([[0, 0],
                    [w, 0],
                    [0, h],
                    [w, h]], np.float32)

    dst = np.zeros((4, 2), np.float32)

    for i in range(4):
        dst[i, 0] = list_dst[i][0] * z / (z - list_dst[i][2]) + pcenter[0]
        dst[i, 1] = list_dst[i][1] * z / (z - list_dst[i][2]) + pcenter[1]

    warpR = cv2.getPerspectiveTransform(org, dst)
    print warpR

    annotation = minidom.parse(os.path.join(load_xml_path, xml_name))
    objects = annotation.getElementsByTagName("object")

    for obj in objects:
        label_name = obj.getElementsByTagName("name")[0].childNodes[0].nodeValue
        label_name = str(label_name)

        # for every object:
        xmin = obj.getElementsByTagName("xmin")[0].childNodes[0].nodeValue
        xmax = obj.getElementsByTagName("xmax")[0].childNodes[0].nodeValue
        ymin = obj.getElementsByTagName("ymin")[0].childNodes[0].nodeValue
        ymax = obj.getElementsByTagName("ymax")[0].childNodes[0].nodeValue
        xmin = int(str(xmin))
        xmax = int(str(xmax))
        ymin = int(str(ymin))
        ymax = int(str(ymax))

        xmin_trans, ymin_trans = transformPoint(xmin, ymin, warpR)
        xmax_trans, ymax_trans = transformPoint(xmax, ymax, warpR)

        obj.getElementsByTagName("xmin")[0].childNodes[0].nodeValue = unicode(str(xmin_trans), encoding='utf-8')
        obj.getElementsByTagName("ymin")[0].childNodes[0].nodeValue = unicode(str(ymin_trans + 20), encoding='utf-8')
        obj.getElementsByTagName("xmax")[0].childNodes[0].nodeValue = unicode(str(xmax_trans), encoding='utf-8')
        obj.getElementsByTagName("ymax")[0].childNodes[0].nodeValue = unicode(str(ymax_trans + 20), encoding='utf-8')


    f = open(os.path.join(save_xml_path, xml_name), 'w')
    annotation.writexml(f, encoding='utf-8')
    f.close()
    return warpR


def trans_plot_xml(xml_name, warpR):

    (shotname, extension) = os.path.splitext(xml_name)
    img_full_name = shotname + '.jpg'
    input_img_file_path = os.path.join(load_img_path, img_full_name)
    output_img_file_path = os.path.join(save_img_path, img_full_name)
    output_img_file_path2 = os.path.join(save_img_path2, img_full_name)
    annotation = minidom.parse(os.path.join(save_xml_path, xml_name))
    image = mpimg.imread(input_img_file_path)
    image = cv2.copyMakeBorder(image, 20, 20, 0, 0, cv2.BORDER_CONSTANT, 0)
    w, h = image.shape[0:2]
    image = cv2.warpPerspective(image, warpR, (h, w))
    cv2.imwrite(output_img_file_path2, image)
    image = mpimg.imread(output_img_file_path2)
    plt.switch_backend('agg')
    currentAxis = plt.gca()
    objects = annotation.getElementsByTagName("object")
    for obj in objects:
        label_name = obj.getElementsByTagName("name")[0].childNodes[0].nodeValue
        label_name = str(label_name)

        # for every object:
        xmin = obj.getElementsByTagName("xmin")[0].childNodes[0].nodeValue
        xmax = obj.getElementsByTagName("xmax")[0].childNodes[0].nodeValue
        ymin = obj.getElementsByTagName("ymin")[0].childNodes[0].nodeValue
        ymax = obj.getElementsByTagName("ymax")[0].childNodes[0].nodeValue
        xmin = int(str(xmin))
        xmax = int(str(xmax))
        ymin = int(str(ymin))
        ymax = int(str(ymax))

        # colors = plt.cm.hsv(np.linspace(0, 1, 21)).tolist()
        display_txt = '%s' % label_name
        # display_bbox_value = '%d %d %d %d' % (xmin, ymin, xmax, ymax)
        coords = (xmin, ymin), xmax - xmin + 1, ymax - ymin + 1
        currentAxis.add_patch(plt.Rectangle(*coords, fill=False, linewidth=0.5))
        # plt.Rectangle(*coords, fill=False, edgecolor=color, linewidth=2))
        # currentAxis.text(xmin, ymin, display_txt, bbox={'facecolor': color,'alpha': 0.5})
        currentAxis.text(xmin, ymin, display_txt, bbox={'alpha': 0.1})

    plt.imshow(image)
    plt.axis('off')

    plt.ion()
    plt.show(output_img_file_path)
    plt.close(output_img_file_path)
    plt.savefig(output_img_file_path, bbox_inches='tight')


if __name__ == "__main__":
    xml_files_input = os.listdir(load_xml_path)
    xml_files_output = os.listdir(save_xml_path)
    for one in xml_files_input:
        print(one)
        warpR = modify_xml(one)
        trans_plot_xml(one, warpR)
