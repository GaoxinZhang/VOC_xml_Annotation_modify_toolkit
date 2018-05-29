# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# % FilterandRename_typename.py
# % include text file(Desired_types.txt & new_type_names.txt)
# % To filter the type we want and rename the name of that type.
# % 4-7-2018 Created
# % Author:Zhang
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
from __future__ import division
import xml.dom.minidom as minidom
import os


src_path = "G:\Boeing_reannotated0509"
result_path = "G:\Boeing_reannotated0509"
load_xml_path = os.path.join(src_path, 'Annotations_reannotated0509')
save_xml_path = os.path.join(result_path, 'Annotations_reannotated0509_filter0522_no_scratch')

isExists = os.path.exists(save_xml_path)
if not isExists:
    os.makedirs(save_xml_path)
    print save_xml_path + ' was built'

a = open('Desired_types.txt')
desired_types = a.read().splitlines()
# desired_types = ["Crack", "Scratch", "Dent"]
num_desired_types = len(desired_types)

b = open('new_type_names.txt')
new_type_names = b.read().splitlines()
# desired_types = ["Crack", "Scratch", "Dent"]
num_new_type_names = len(new_type_names)

if (num_desired_types != num_new_type_names):
    print ' num of names is not equal'
    exit()

def filterandrename_xml(xml_name):

    annotation = minidom.parse(os.path.join(load_xml_path, xml_name))
    objects = annotation.getElementsByTagName("object")

    for obj in objects:
        label_name = obj.getElementsByTagName("name")[0].childNodes[0].nodeValue
        label_name = str(label_name)

        if label_name in desired_types:
            index = desired_types.index(label_name)
            new_label_name = new_type_names[index]
            obj.getElementsByTagName("name")[0].childNodes[0].nodeValue = unicode(str(new_label_name), encoding='utf-8')

        elif label_name not in desired_types:
            annotation.documentElement.removeChild(obj)

    xml_tmp = 'tmp' + xml_name
    f_temp = open(os.path.join(save_xml_path, xml_tmp), 'w')
    f = open(os.path.join(save_xml_path, xml_name), 'w')
    blank_line_content = '  '
    head_of_xml = '<?xml version="1.0" encoding="utf-8"?><annotation>'
    annotation.writexml(f_temp, encoding='utf-8')

    f_temp = open(os.path.join(save_xml_path, xml_tmp), 'r')
    for line in f_temp.read().splitlines():
        if line == blank_line_content:
            continue
        else:
            if line == head_of_xml:
                f.write('<annotation>' + '\n')
            else:
                f.write(line + '\n')

    f_temp.close()
    os.remove(os.path.join(save_xml_path, xml_tmp))
    f.close()

    annotation = minidom.parse(os.path.join(save_xml_path, xml_name))
    objects_filter = annotation.getElementsByTagName("object")
    if len(objects_filter) == 0:
        os.remove(os.path.join(save_xml_path, xml_name))



if __name__ == "__main__":
    xml_files_input = os.listdir(load_xml_path)
    for one in xml_files_input:
        print(one)
        filterandrename_xml(one)
