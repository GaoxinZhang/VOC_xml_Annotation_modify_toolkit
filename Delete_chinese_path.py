# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# % Delete_chinese_path.py
# % To delete path and folder include chinese.
# % 4-7-2018 Created
# % Author:Zhang
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
from __future__ import division
import xml.dom.minidom as minidom
import os

# root_path is a folder where original xml files stored
root_path = "G:\Boeing_10k_Dataset\Forth"
# result_path is a folder where converted xml files stored
result_path = "G:\Boeing_10k_Dataset\Forth"

load_xml_path = os.path.join(root_path, 'Annotations')
save_xml_path = os.path.join(result_path, 'Annotations_withoutchinese')


def filterandrename_xml(xml_name):

    annotation = minidom.parse(os.path.join(load_xml_path, xml_name))
    new_folder = 'JPEGImages'
    new_path = 'boeingdata'

    annotation.getElementsByTagName("folder")[0].childNodes[0].nodeValue = unicode(str(new_folder), encoding='utf-8')
    annotation.getElementsByTagName("path")[0].childNodes[0].nodeValue = unicode(str(new_path), encoding='utf-8')

    isExists = os.path.exists(save_xml_path)
    if not isExists:
        os.makedirs(save_xml_path)
        print save_xml_path + ' was built'

    xml_tmp = 'tmp' + xml_name
    f_temp = open(os.path.join(save_xml_path, xml_tmp), 'w')
    f = open(os.path.join(save_xml_path, xml_name), 'w')
    blank_line_content = '  '
    annotation.writexml(f_temp, encoding='utf-8')

    f_temp = open(os.path.join(save_xml_path, xml_tmp), 'r')
    for line in f_temp.read().splitlines():
        if line == blank_line_content:
            continue
        else:
            f.write(line + '\n')

    f_temp.close()
    os.remove(os.path.join(save_xml_path, xml_tmp))
    f.close()

if __name__ == "__main__":
    xml_files_input = os.listdir(load_xml_path)
    for one in xml_files_input:
        print(one)
        filterandrename_xml(one)
