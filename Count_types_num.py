# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# % Count_types_num.py
# % include text file(Counted_type_names.txt)
# % To count number of every type and number of every pic included this type
# % 4-7-2018 Created
# % Author:Zhang
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
from __future__ import division
import xml.dom.minidom as minidom
import os
import numpy as np


src_path = "H:\Boeing_reannotated0604\Modified_all_0609_checked"
load_xml_path = os.path.join(src_path, 'Annotations')
a = open('Counted_type_names.txt')
# Counted_type_names = a.read().splitlines()
Counted_type_names = ["Scratch"]
num_counted_types = len(Counted_type_names)
num_of_types_xml = np.zeros(num_counted_types)
num_of_pic_included_any_types = np.zeros(num_counted_types)

def count_type_name(xml_name):

    annotation = minidom.parse(os.path.join(load_xml_path, xml_name))
    objects = annotation.getElementsByTagName("object")
    list_of_exist_type = list()
    for obj in objects:
        label_name = obj.getElementsByTagName("name")[0].childNodes[0].nodeValue
        label_name = str(label_name)

        # if label_name == 'Lightning_strikes':
        #     print 'Lightning_strikes is in ', xml_name
        #
        # if label_name == 'Lightning_strikes ':
        #     print 'Lightning_strikes is in ', xml_name

        # count number of every type:
        if label_name in Counted_type_names:
            index_1 = Counted_type_names.index(label_name)
            num_of_types_xml[index_1] = num_of_types_xml[index_1] + 1

        # count number of every pic included any type:
        if label_name not in list_of_exist_type and label_name in Counted_type_names:
            list_of_exist_type.append(label_name)
            index_2 = Counted_type_names.index(label_name)
            num_of_pic_included_any_types[index_2] = num_of_pic_included_any_types[index_2] + 1

if __name__ == "__main__":
    xml_files_input = os.listdir(load_xml_path)
    print 'Counting...'
    for one in xml_files_input:
        # print 'Counting...'
        count_type_name(one)
        print (one)

    for i in range(0, num_counted_types):
        print 'The num of type: [', Counted_type_names[i], '] is', num_of_types_xml[i]
        print 'The num of pic include any type: [', Counted_type_names[i], '] is', num_of_pic_included_any_types[i]
