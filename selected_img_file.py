#!/usr/bin/evn python
#coding:utf-8
# by Xin He
import os
import shutil

img_src = 'G:\Boeing_10k_Dataset\Third\Third_perforation\\'
remove_txt = 'G:\Boeing_10k_Dataset\Third\WangFan\wangfan.txt'
output_path = 'G:\Boeing_10k_Dataset\Third\Third_perforation_selected\\'


def file_list(file_dir):
    jpg_list = []
    for root, dirs,files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.xml':
                jpg_list.append(os.path.join(file))

    return jpg_list


def gen_log_list(dir):
    log_file = open(dir, "r")
    lines = log_file.readlines()

    lines_num = len(lines)
    # columns_num = len(lines[1].split())

    log_list = []

    for line_count in range(0, lines_num):
        if len(lines[line_count].split()) == 1:
            log_list.append(int(lines[line_count]))
        else:
            for l_count in range(int(lines[line_count].split()[0]),
                                 int(lines[line_count].split()[1])):
                log_list.append(l_count)
    print log_list
    return log_list


def select_imgs(img_src_dir, remove_txt_dir, output_dir):
    img_list = file_list(img_src_dir)
    num_imgs = len(img_list)
    remove_list = gen_log_list(remove_txt_dir)

    for img_count in range(0, num_imgs):
        if int(img_list[img_count][:-4]) in remove_list:
            pass
        else:
            shutil.copy(img_src_dir + img_list[img_count], output_dir + img_list[img_count])

select_imgs(img_src, remove_txt, output_path)
# file_list(img_src)
# gen_log_list(select_txt)



