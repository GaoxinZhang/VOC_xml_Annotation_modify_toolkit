from __future__ import division
import cv2
import numpy as np
import xml.dom.minidom as minidom
import os
import re
import math

# transform xml using M matrix
"""
pic_path = "pic"
pic_result = "pic_result"
root_path = "xml"
result_path = "xml_result"
"""
pic_path = "C:\Users\Hancy\Desktop\\testvacancy\\jpg"
root_path = "C:\Users\Hancy\Desktop\\testvacancy\\xml"
pic_result = "C:\Users\Hancy\Desktop\\testvacancy\\resultjpg"
result_path = "C:\Users\Hancy\Desktop\\testvacancy\\resultxml"
min_angle = 0
max_angle = 10
grp = 10
scale = 1


def LRotate(angle,xml_name):

    image = cv2.imread(pic_path + "\\" + re.findall(r'(.+?)\.', xml_name)[0] + '.jpg', 1)
    annotation = minidom.parse(os.path.join(root_path, xml_name))
    h = image.shape[0]
    w = image.shape[1]
    c = image.shape[2]
    anglePi = angle * math.pi / 180.0
    cosA = math.cos(anglePi)
    sinA = math.sin(anglePi)
    # X1 = math.ceil(abs(0.5 * h * cosA + 0.5 * w * sinA))
    # X2 = math.ceil(abs(0.5 * h * cosA - 0.5 * w * sinA))
    # Y1 = math.ceil(abs(-0.5 * h * sinA + 0.5 * w * cosA))
    # Y2 = math.ceil(abs(-0.5 * h * sinA - 0.5 * w * cosA))
    # H = int(2 * max(Y1, Y2))
    # W = int(2 * max(X1, X2))
    # # iLRotate = cv2.CreateImage(image.shape[0],image.shape[1],image.shape[2], np.uint8)
    # iLRotate = np.zeros((H+1,W+1,c),np.uint8)
    #
    # for i in range(h):
    #     for j in range(w):
    #         x = int(cosA * i - sinA * j - 0.5 * w * cosA + 0.5 * h * sinA + 0.5 * W)
    #         y = int(sinA * i + cosA * j - 0.5 * w * sinA - 0.5 * h * cosA + 0.5 * H)
    #         # if x>-1 and x<image.height and y>-1 and y<image.width:
    #         iLRotate[x, y] = image[i, j]

    M = cv2.getRotationMatrix2D((w / 2, h / 2), angle, scale)
    iLRotate = cv2.warpAffine(image, M, (w, h))

    img_sizes = annotation.getElementsByTagName("size")
    for img_size in img_sizes:
        img_size.getElementsByTagName("width")[0].childNodes[0].nodeValue = unicode(str(w),
                                                                                    encoding='utf-8')
        img_size.getElementsByTagName("height")[0].childNodes[0].nodeValue = unicode(str(h),
                                                                                     encoding='utf-8')
    bndbox = annotation.getElementsByTagName("bndbox")
    for one in bndbox:
        xmin = int(str(one.getElementsByTagName("xmin")[0].childNodes[0].nodeValue))
        ymin = int(str(one.getElementsByTagName("ymin")[0].childNodes[0].nodeValue))
        xmax = int(str(one.getElementsByTagName("xmax")[0].childNodes[0].nodeValue))
        ymax = int(str(one.getElementsByTagName("ymax")[0].childNodes[0].nodeValue))
        print xmin, ymin, xmax, ymax

        trans_xmin = int(cosA * xmin - sinA * ymin - 0.5 * w * cosA + 0.5 * h * sinA + 0.5 * w)
        trans_ymin = int(sinA * xmin + cosA * ymin - 0.5 * w * sinA - 0.5 * h * cosA + 0.5 * h)
        trans_xmax = int(cosA * xmax - sinA * ymax - 0.5 * w * cosA + 0.5 * h * sinA + 0.5 * w)
        trans_ymax = int(sinA * xmax + cosA * ymax - 0.5 * w * sinA - 0.5 * h * cosA + 0.5 * h)

        one.getElementsByTagName("xmin")[0].childNodes[0].nodeValue = unicode(str(int(trans_xmin)),
                                                                              encoding='utf-8')
        one.getElementsByTagName("ymin")[0].childNodes[0].nodeValue = unicode(str(int(trans_ymin)),
                                                                              encoding='utf-8')
        one.getElementsByTagName("xmax")[0].childNodes[0].nodeValue = unicode(str(int(trans_xmax)),
                                                                              encoding='utf-8')
        one.getElementsByTagName("ymax")[0].childNodes[0].nodeValue = unicode(str(int(trans_ymax)),
                                                                              encoding='utf-8')

    f = open(os.path.join(result_path, re.findall(r'(.+?)\.', xml_name)[0] + "_" + str(angle) + '.xml'),
             'w')  # write the xml into the directory
    annotation.writexml(f, encoding='utf-8')
    f.close()

    # return iLRotate
    cv2.imwrite(pic_result+"\\"+re.findall(r'(.+?)\.', xml_name)[0]+"_"+str(angle)+".jpg", iLRotate)


if __name__ == '__main__':
    xml_file = os.listdir(root_path)
    for xml_file_name in xml_file:
        print(xml_file_name)
        for i in range(0, grp):
            angle = float(min_angle + (max_angle - min_angle) / grp * i)
            print 'angle = ' + str(angle)
            LRotate(angle, xml_file_name)
