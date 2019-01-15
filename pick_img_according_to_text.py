# coding: utf-8
import os
import shutil

if __name__ == '__main__':

    Dataset_folder = "C:\Users\Hancy\Desktop\Boeing_data\\airplane_9_classes_VR"
    load_img_path = os.path.join(Dataset_folder,'JPEGImages')
    load_xml_path = os.path.join(Dataset_folder,'Annotations')
    load_text_path = os.path.join(Dataset_folder,'ImageSets/Main_PHASE2_old+new')
    load_text_file = os.path.join(load_text_path,'test.txt')
    text = open(load_text_file)
    im_names = text.read().splitlines()
    save_img_path = os.path.join(Dataset_folder,'img_test_new+old')
    save_xml_path = os.path.join(Dataset_folder,'anno_test_new+old')
    if not os.path.exists(save_img_path):
        os.makedirs(save_img_path)
        print (save_img_path + ' was built')
    if not os.path.exists(save_xml_path):
        os.makedirs(save_xml_path)
        print (save_xml_path + ' was built')

    # im_names = os.listdir(load_img_path)
    # im_names = ['002.jpg']
    for im_name in im_names:
        img_name = im_name +'.jpg'
        xml_name = im_name +'.xml'
        img_file = os.path.join(load_img_path, img_name)
        xml_file = os.path.join(load_xml_path, xml_name)
        save_img_file = os.path.join(save_img_path, img_name)
        save_xml_file = os.path.join(save_xml_path, xml_name)
        shutil.copy(img_file, save_img_file)
        shutil.copy(xml_file, save_xml_file)