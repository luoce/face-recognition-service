#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import logging

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # 日志目录
    LOG_FILE_PATH = '/Users/huan/sources/python-sources/face-recognition-service/face-recognition-service.log'

    # 日志级别
    LOG_LEVEL = logging.DEBUG

    # 图片格式范围
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

    # 人脸库图片目录
    KNOW_FACE_DIR = '/Users/huan/sources/python-sources/face-recognition-service/face_data/know_face_dir'

    # 阀值，法治太低无法成功识别人脸，太高则会造成混淆，这里我也不懂，默认0.6  推荐0.39、0.49
    TOLERANCE = 0.49
