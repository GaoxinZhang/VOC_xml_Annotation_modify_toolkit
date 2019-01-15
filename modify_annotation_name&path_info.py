# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# % Delete_chinese_path.py
# % To delete path and folder include chinese.
# % 4-7-2018 Created
# % Author:Zhang
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
from __future__ import division
import xml.dom.minidom as minidom
import os


src_path = "C:\Users\Hancy\Desktop\Dataset\dataset_6_classes\VOCdevkit\VOC2007"
result_path = "C:\Users\Hancy\Desktop\Dataset\dataset_6_classes\VOCdevkit\VOC2007"

load_xml_path = os.path.join(src_path, 'Annotations')
save_xml_path = os.path.join(result_path, 'Annotations_rightpath')


def filterandrename_xml(xml_name):

    (shotname, extension) = os.path.splitext(one)
    jpg_full_name = shotname + '.jpg'
    annotation = minidom.parse(os.path.join(load_xml_path, xml_name))
    new_path = jpg_full_name


    annotation.getElementsByTagName("filename")[0].childNodes[0].nodeValue = unicode(str(new_path), encoding='utf-8')

    isExists = os.path.exists(save_xml_path)
    if not isExists:
        os.makedirs(save_xml_path)
        print save_xml_path + ' was built'

    f = open(os.path.join(save_xml_path, xml_name), 'w')
    annotation.writexml(f, encoding='utf-8')
    f.close()

if __name__ == "__main__":
    xml_files_input = os.listdir(load_xml_path)
    for one in xml_files_input:
        print(one)
        filterandrename_xml(one)
