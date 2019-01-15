# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# % DivideDataset.py
# % 17-7-2018 Created
# % Author:Zhang
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
from __future__ import division
import os
import shutil


def split_filename(anno_file):
    (shotname, extension) = os.path.splitext(anno_file)
    number = shotname[-5:]
    prefix = shotname[:-5]
    return prefix, int(number), extension


if __name__ == "__main__":

    src_path = "C:\Users\Hancy\Desktop\Boeing_data\TO_BUPT_TianRui"
    load_anno_path = os.path.join(src_path, 'zgx_anno_190114')
    start_anno = 'jj-pm1217-17_1_01050.xml'
    end_anno = 'jj-pm1217-17_1_01051.xml'
    prefix, start_num, extension= split_filename(start_anno)
    end_num = split_filename(end_anno)[1]
    src_anno_path = os.path.join(load_anno_path, start_anno)

    # count_duplicate = 223
    # (shotname, extension) = os.path.splitext(start_xml)
    # print(shotname)
    # number = shotname[-5:]
    # print(number)
    # prefix = shotname[:-5]

    for i in range(1, end_num - start_num + 1):
        save_anno_name = prefix + str("%05d" %(start_num + i)) + extension
        save_anno_file_path = os.path.join(load_anno_path, save_anno_name)
        shutil.copy(src_anno_path, save_anno_file_path)


