"""
This code is adapted from the Github repository shared by user Nicholasli1995 (Shichao Li) at https://github.com/Nicholasli1995/VisualizingNDF
Age estimation below uses the pretrained model shared in the Github repo mentioned above. All copyrights belong to them. 
Copyright (c) 2019 Shichao Li
Please check out their awesome repository as well as their papers. Links are in the Github repository.
Lastly, big thanks to them for open sourcing their code under the MIT License!
"""

import torch
import argparse
import vis_utils
from data_prepare import prepare_db
from pathlib import Path
import torch.utils.data
import torchvision.transforms.functional as transform_f
import imageio as io
import numpy as np
import logging
import PIL
import cv2
import urllib

def pred_age_from_image_url(url):

    # load model
    model_path = "../pre-trained/CACD_MAE_4.59.pth"
    model = torch.load(model_path)
    model.cuda()


    mean = [0.432, 0.359, 0.320]
    std = [0.30,  0.264,  0.252]

    req = urllib.request.urlopen(url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    image = cv2.imdecode(arr, -1)  # 'Load it as it is'

    # image_path = '../test/t4.jpg'
    # image = cv2.imread(image_path)
    face_cascade = cv2.CascadeClassifier("../haarcascade_frontalface_default.xml")
    face_cascade.load('../haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # return error if no faces are detected
    if len(faces) == 0:
        return "Error"

    for (x, y, w, h) in faces:
        crop = image[y:y + h, x:x + w]
        break

    resized_crop = cv2.resize(crop, (256, 256))
    # cv2.imshow('crop', resized_crop)

    image = cv2.cvtColor(resized_crop, cv2.COLOR_BGR2RGB)
    image = PIL.Image.fromarray(image)

    # image = PIL.Image.open(image_path)
    image = transform_f.to_tensor(image)
    image = transform_f.normalize(image, mean=mean, std=std)

    sample = image.unsqueeze(0)

    # predict
    pred, _,  cache = model(sample.cuda(), save_flag = True)

    return (pred.data.item()*90)