# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# % DivideDataset.py
# %
# %
# % 17-7-2018 Created
# % Author:Zhang
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
from __future__ import division
import os
import shutil


src_path = "H:\Reannotation0717"
result_path = "H:\Reannotation0717"
load_xml_path = os.path.join(src_path, 'Annotations_resize')
load_img_path = os.path.join(src_path, 'JPEGImages_resize')

save_files_path = os.path.join(result_path, 'Result2')

isExists = os.path.exists(save_files_path)
if not isExists:
    os.makedirs(save_files_path)
    print save_files_path + ' was built'

xml_files_input = os.listdir(load_xml_path)

ratio = ["0", "3", "3", "3", "2", "2"]
num_r = len(ratio)
r_total = 0
for r in ratio:
    r_total = r_total + int(r)

num_xml = len(xml_files_input)

for one in xml_files_input:
    (shotname, extension) = os.path.splitext(one)
    jpg_full_name = shotname + '.jpg'


def sum_list(list,i):
    sum_list = 0
    for j in range(0,i+1):
        sum_list = sum_list + int(list[j])
    return sum_list


def DivideDataset(i, xml_files_input, save_files_path_xml, save_files_path_img ):

    low = int(sum_list(ratio,i-1)/r_total*num_xml)
    high = int(sum_list(ratio,i)/r_total*num_xml)


    for j in range(low, high):

        src_xml_file_path = os.path.join(load_xml_path, xml_files_input[j])
        save_xml_file_path = os.path.join(save_files_path_xml, xml_files_input[j])
        shutil.copy(src_xml_file_path, save_xml_file_path)

        (shotname, extension) = os.path.splitext(xml_files_input[j])
        jpg_full_name = shotname + '.jpg'
        src_img_file_path = os.path.join(load_img_path, jpg_full_name)
        save_img_file_path = os.path.join(save_files_path_img, jpg_full_name)
        shutil.copy(src_img_file_path, save_img_file_path)



if __name__ == "__main__":
    xml_files_input = os.listdir(load_xml_path)
    for i in range(1, num_r):

        save_files_path_xml = os.path.join(save_files_path, str(i), 'Annotations')
        save_files_path_img = os.path.join(save_files_path, str(i), 'JPEGImages')

        isExists = os.path.exists(save_files_path_xml)
        if not isExists:
            os.makedirs(save_files_path_xml)
            print save_files_path_xml + ' was built'

        isExists = os.path.exists(save_files_path_img)
        if not isExists:
            os.makedirs(save_files_path_img)
            print save_files_path_img + ' was built'

        DivideDataset(i, xml_files_input, save_files_path_xml, save_files_path_img)

