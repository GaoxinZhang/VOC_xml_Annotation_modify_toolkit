# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# % plot_ground_truth.py
# % To plot ground truth box in pic.
# % 4-7-2018 Created
# % Author:Zhang
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
from __future__ import division
import xml.dom.minidom as minidom
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os


src_path = "G:\Boeing_reannotated0509"
result_path = "G:\Boeing_reannotated0509"
load_xml_path = os.path.join(src_path, 'Annotations_reannotated0509_resized')
load_img_path = os.path.join(src_path, 'JPEGImages')
save_img_path = os.path.join(result_path, 'JPEGImages_plot_gt')


def print_xml_on_pic(xml_name):

    (shotname, extension) = os.path.splitext(xml_name)
    img_full_name = shotname + '.jpg'
    input_img_file_path = os.path.join(load_img_path, img_full_name)
    output_img_file_path = os.path.join(save_img_path, img_full_name)
    annotation = minidom.parse(os.path.join(load_xml_path, xml_name))

    size = annotation.getElementsByTagName("size")
    width = size[0].getElementsByTagName("width")[0].childNodes[0].nodeValue
    height = size[0].getElementsByTagName("height")[0].childNodes[0].nodeValue
    width = int(str(width))
    height = int(str(height))

    #plt.rcParams['figure.figsize'] = (1, 1)
    plt.rcParams['image.interpolation'] = 'nearest'
    plt.rcParams['image.cmap'] = 'gray'

    object = annotation.getElementsByTagName("object")
    image = mpimg.imread(input_img_file_path)
    plt.switch_backend('agg')
    currentAxis = plt.gca()
    for obj in object:
        label_name = obj.getElementsByTagName("name")[0].childNodes[0].nodeValue
        label_name = str(label_name)

        xmin = obj.getElementsByTagName("xmin")[0].childNodes[0].nodeValue
        xmin = int(str(xmin))
        xmax = obj.getElementsByTagName("xmax")[0].childNodes[0].nodeValue
        xmax = int(str(xmax))
        ymin = obj.getElementsByTagName("ymin")[0].childNodes[0].nodeValue
        ymin = int(str(ymin))
        ymax = obj.getElementsByTagName("ymax")[0].childNodes[0].nodeValue
        ymax = int(str(ymax))

        # colors = plt.cm.hsv(np.linspace(0, 1, 21)).tolist()
        display_txt = '%s' % (label_name)
        # display_bbox_value = '%d %d %d %d' % (xmin, ymin, xmax, ymax)
        coords = (xmin, ymin), xmax - xmin + 1, ymax - ymin + 1
        currentAxis.add_patch(plt.Rectangle(*coords, fill=False, linewidth=0.5))
        # plt.Rectangle(*coords, fill=False, edgecolor=color, linewidth=2))
        # currentAxis.text(xmin, ymin, display_txt, bbox={'facecolor': color,'alpha': 0.5})
        currentAxis.text(xmin, ymin, display_txt, bbox={'alpha': 0.2})

    plt.imshow(image)
    plt.axis('off')
    isExists = os.path.exists(save_img_path)
    if not isExists:
        os.makedirs(save_img_path)
        print save_img_path + ' was built'
    # plt.ion()
    plt.show()
    # plt.close(output_img_file_path)
    plt.savefig(output_img_file_path, bbox_inches='tight')


if __name__ == "__main__":
    xml_files = os.listdir(load_xml_path)
    for one in xml_files:
        print(one)
        print_xml_on_pic(one)
