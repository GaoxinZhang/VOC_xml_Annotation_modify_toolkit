# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# % Pick_out_pic_with_xml.py
# % To pick out those pic with xml
# % 4-8-2018 Created
# % Author:Zhang
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
from __future__ import division
import os
import shutil

root_path1 = "C:\Users\Hancy\Desktop\Zhang\AIRPLANE5_Zhang"
root_path2 = "C:\Users\Hancy\Desktop\Zhang\AIRPLANE5_Zhang"
save_path = "C:\Users\Hancy\Desktop\Zhang\AIRPLANE5_Zhang"
load_pic_path = os.path.join(root_path1, 'JPEGImages')
load_xml_path = os.path.join(root_path2, 'Annotations')



def pick_pic(pic_name):

    (shotname, extension) = os.path.splitext(pic_name)
    xml_full_name = shotname + '.xml'

    xml_files_input = os.listdir(load_xml_path)

    if xml_full_name in xml_files_input:
        mv_img_file_path = os.path.join(load_pic_path, pic_name)

        save_img_path = os.path.join(save_path, 'with_xml_pic')
        isExists = os.path.exists(save_img_path)

        if not isExists:
            os.makedirs(save_img_path)
            print(save_img_path + ' was built')

        save_img_file_path = os.path.join(save_img_path, pic_name)
        # shutil.move(mv_img_file_path, save_img_file_path)
        shutil.move(mv_img_file_path, save_img_file_path)
        # shutil.copy(mv_img_file_path, save_img_file_path)


if __name__ == "__main__":
    pic_files_input = os.listdir(load_pic_path)
    print 'Picking...'
    for one in pic_files_input:
        pick_pic(one)
