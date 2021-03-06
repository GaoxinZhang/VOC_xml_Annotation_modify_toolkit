# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# % Filter_the_pic_withno_xml.py
# % To Delete those pic with no xml
# % 4-8-2018 Created
# % Author:Zhang
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
from __future__ import division
import os
import shutil


src_path = "C:\Users\Hancy\Desktop\Boeing_data\AIRPLANE9"
save_path = "C:\Users\Hancy\Desktop\Boeing_data\AIRPLANE9"
load_pic_path = os.path.join(src_path, 'JPEGImages')
load_xml_path = os.path.join(save_path, 'Annotations_scratch')



def delete_pic(pic_name):

    (shotname, extension) = os.path.splitext(pic_name)
    xml_full_name = shotname + '.xml'

    xml_files_input = os.listdir(load_xml_path)

    if xml_full_name in xml_files_input:
        mv_img_file_path = os.path.join(load_pic_path, pic_name)

        save_img_path = os.path.join(save_path, 'JPEGImages_with_xml')
        isExists = os.path.exists(save_img_path)
        if not isExists:
            os.makedirs(save_img_path)
            print(save_img_path + ' was built')

        save_img_file_path = os.path.join(save_img_path, pic_name)
        shutil.copy(mv_img_file_path, save_img_file_path)


if __name__ == "__main__":
    pic_files_input = os.listdir(load_pic_path)
    print 'Creating new images set...'
    for one in pic_files_input:
        # print 'Counting...'
        delete_pic(one)
