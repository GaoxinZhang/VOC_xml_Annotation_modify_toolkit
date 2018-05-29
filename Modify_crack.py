# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# % Modify_crack.py
# % To modify ground truth box in xml.
# % 4-7-2018 Created
# % Author:Zhang
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
from __future__ import division
import xml.dom.minidom as minidom
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

plt.rcParams['figure.figsize'] = (10, 10)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'


root_path = "C:\Users\Hancy\Desktop\Dataset_AIRPLANE5"
result_path = "C:\Users\Hancy\Desktop\plot_AIRPLANE5"

load_xml_path = os.path.join(root_path, 'Annotations')
load_img_path = os.path.join(root_path, 'JPEGImages')

save_xml_path = os.path.join(result_path, 'Annotations_div')
save_img_path = os.path.join(result_path, 'JPEGImages_div')

isExists = os.path.exists(save_xml_path)
if not isExists:
    os.makedirs(save_xml_path)
    print save_xml_path + ' was built'

def modify_xml(xml_name):

    annotation = minidom.parse(os.path.join(load_xml_path, xml_name))

    size = annotation.getElementsByTagName("size")
    width = size[0].getElementsByTagName("width")[0].childNodes[0].nodeValue
    height = size[0].getElementsByTagName("height")[0].childNodes[0].nodeValue
    width = int(str(width))
    height = int(str(height))

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

        area_obj = (xmax - xmin) * (ymax - ymin)
        area_pic = height * width
        overlap = area_obj/area_pic

        bdn_width = xmax - xmin
        bdn_height = ymax - ymin

        x_center = xmin + bdn_width / 2
        y_center = ymin + bdn_height / 2

        s_ratio = 0.45
        overlap_threshold = 0.08

        if label_name == 'Crack' or label_name == 'Scratch':

            if overlap > overlap_threshold:

                # for corner

                newtext = annotation.createTextNode("\n  ")
                cloneNode1 = obj.cloneNode(obj)
                cloneNode2 = obj.cloneNode(obj)
                cloneNode3 = obj.cloneNode(obj)

                xmax_1 = int(xmin + s_ratio * bdn_width)
                ymax_1 = int(ymin + s_ratio * bdn_height)
                obj.getElementsByTagName("xmax")[0].childNodes[0].nodeValue = unicode(str(xmax_1), encoding='utf-8')
                obj.getElementsByTagName("ymax")[0].childNodes[0].nodeValue = unicode(str(ymax_1), encoding='utf-8')

                xmin_2 = int(xmax - s_ratio * bdn_width)
                ymin_2 = int(ymax - s_ratio * bdn_height)
                cloneNode1.getElementsByTagName("xmin")[0].childNodes[0].nodeValue = unicode(str(xmin_2), encoding='utf-8')
                cloneNode1.getElementsByTagName("ymin")[0].childNodes[0].nodeValue = unicode(str(ymin_2), encoding='utf-8')

                annotation.documentElement.appendChild(newtext)
                annotation.documentElement.appendChild(cloneNode1)


                ymin_3 = int(ymin + (1 - s_ratio) * bdn_height)
                xmax_3 = int(xmin + s_ratio * bdn_width)
                cloneNode2.getElementsByTagName("ymin")[0].childNodes[0].nodeValue = unicode(str(ymin_3), encoding='utf-8')
                cloneNode2.getElementsByTagName("xmax")[0].childNodes[0].nodeValue = unicode(str(xmax_3), encoding='utf-8')

                annotation.documentElement.appendChild(newtext)
                annotation.documentElement.appendChild(cloneNode2)

                xmin_4 = int(xmin + (1 - s_ratio) * bdn_width)
                ymax_4 = int(ymin + s_ratio * bdn_height)
                cloneNode3.getElementsByTagName("xmin")[0].childNodes[0].nodeValue = unicode(str(xmin_4), encoding='utf-8')
                cloneNode3.getElementsByTagName("ymax")[0].childNodes[0].nodeValue = unicode(str(ymax_4), encoding='utf-8')

                annotation.documentElement.appendChild(newtext)
                annotation.documentElement.appendChild(cloneNode3)

                # for center
                # xmax = int(x_center + s_ratio * bdn_width)
                # obj.getElementsByTagName("xmax")[0].childNodes[0].nodeValue = unicode(str(xmax), encoding='utf-8')
                # #obj.getElementsByTagName("xmax")[0].childNodes[0].nodeValue = str(xmax).encode('utf-8')
                # xmin = int(x_center - s_ratio * bdn_width)
                # obj.getElementsByTagName("xmin")[0].childNodes[0].nodeValue = unicode(str(xmin), encoding='utf-8')
                # ymax = int(y_center + s_ratio * bdn_height)
                # obj.getElementsByTagName("ymax")[0].childNodes[0].nodeValue = unicode(str(ymax), encoding='utf-8')
                # ymin = int(y_center - s_ratio * bdn_height)
                # obj.getElementsByTagName("ymin")[0].childNodes[0].nodeValue = unicode(str(ymin), encoding='utf-8')



    f = open(os.path.join(save_xml_path, xml_name), 'w')
    annotation.writexml(f, encoding='utf-8')
    f.close()

def plot_xml(xml_name):

    (shotname, extension) = os.path.splitext(xml_name)
    img_full_name = shotname + '.jpg'
    input_img_file_path = os.path.join(load_img_path, img_full_name)
    output_img_file_path = os.path.join(save_img_path, img_full_name)
    annotation = minidom.parse(os.path.join(save_xml_path, xml_name))

    image = mpimg.imread(input_img_file_path)
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
        currentAxis.add_patch(plt.Rectangle(*coords, fill=False, linewidth=2))
        # plt.Rectangle(*coords, fill=False, edgecolor=color, linewidth=2))
        # currentAxis.text(xmin, ymin, display_txt, bbox={'facecolor': color,'alpha': 0.5})
        currentAxis.text(xmin, ymin, display_txt, bbox={'alpha': 0.5})

    plt.imshow(image)
    plt.axis('off')
    isExists = os.path.exists(save_img_path)
    if not isExists:
        os.makedirs(save_img_path)
        print save_img_path + ' was built'

    plt.ion()
    plt.show(output_img_file_path)
    plt.close(output_img_file_path)
    plt.savefig(output_img_file_path, bbox_inches='tight')


if __name__ == "__main__":
    xml_files_input = os.listdir(load_xml_path)
    xml_files_output = os.listdir(save_xml_path)
    for one in xml_files_input:
        print(one)
        modify_xml(one)

    for one in xml_files_output:
        print(one)
        plot_xml(one)
