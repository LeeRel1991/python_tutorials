#!/usr/bin/env python
# encoding: utf-8


# -------------------------------------------------------
# version: v0.1
# author: lirui
# license: Apache Licence
# project: learning
# function:
# file: use_xml
# time: 7/27/17 11:21 AM
# -------------------------------------------------------
import os
import xml.etree.ElementTree as ET
import cv2


def extract_roi_image(ori_img, boxes, objs_dir):
    img = cv2.imread(ori_img)
    # print(os.path.splitext(ori_img)[-1])
    name, ext = os.path.splitext(os.path.split(ori_img)[-1])
    for ind, box in enumerate(boxes):
        label, x1, y1, x2, y2 = box
        roi = img[y1:y2, x1:x2, :]
        roi_name = os.path.join(objs_dir, "{name}_{label}_{ind}.jpg".format(**locals()))
        print("obj file", roi_name)
        cv2.imwrite(roi_name, roi)
        # print("local", locals().keys())


def extract_obj_image_from_pascal_voc(dataset_dir=""):
    xml_dir, img_dir, objs_dir = [os.path.join(dataset_dir, x) for x in ["xmls", "imgs", "objs"]]
    xml_files = os.listdir(xml_dir)

    for filename in xml_files:
        # print(filename)
        tree = ET.parse(os.path.join(xml_dir, filename))
        objs = tree.findall('object')
        img_file = os.path.join(img_dir, filename.replace(".xml", ".jpg"))
        boxes = []

        for ix, obj in enumerate(objs):
            bbox = obj.find('bndbox')
            # Make pixel indexes 0-based
            x1 = int(bbox.find('xmin').text)
            y1 = int(bbox.find('ymin').text)
            x2 = int(bbox.find('xmax').text)
            y2 = int(bbox.find('ymax').text)

            strlabel = obj.find('name').text.lower().strip()
            # 类别名错误的bounding_box不使用并输出警告
            if strlabel != "xiongqi":
                print("label", strlabel)
                boxes.append([strlabel, x1, y1, x2, y2])
                # if len(boxes) > 0:
                #     extract_roi_image(img_file, boxes, objs_dir)


if __name__ == '__main__':
    extract_obj_image_from_pascal_voc("/media/lirui/Program/Datas/imageqiangjie/trainset")
