#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import app
from flask import Flask, jsonify, request, redirect
from common.xa_result import XaResult
import face_recognition
from mock import face_mock_dict

# 判断文件格式是否在允许范围内
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/upload_faceimg_to_recognition', methods=['POST'])
def upload_faceimg_to_recognition():
    if 'file' not in request.files:
        return XaResult.error(0, u'请上传照片')
    if 'name' not in request.form:
        return XaResult.error(0, u'请提供姓名')

    faceimg = request.files['file']
    name = request.form['name']

    if faceimg.filename == '':
        return XaResult.error(0, u'无效的文件名')

    if not allowed_file(faceimg.filename):
        return XaResult.error(0, u'不支持的文件格式')

    locate_image = face_recognition.load_image_file(faceimg)
    face_locations = face_recognition.face_locations(locate_image)
    face_count = len(face_locations)

    if face_count == 0:
        return XaResult.error(0, u'照片中没能找到人脸')

    for face_location in face_locations:
        top, right, bottom, left = face_location
        print "A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right)

    if face_count > 1:
        return XaResult.error(0, u'照片中存在多张人脸')

    unknown_face_encodings = face_recognition.face_encodings(face_recognition.load_image_file(faceimg))

    if not len(unknown_face_encodings) > 0:
        return XaResult.error(0, u'照片中没能找到人脸')

    know_name = None
    know_face_encoding = None

    for face_info in face_mock_dict.mock_array:
        if face_info['name'] == name:
            know_name = face_info['name']
            know_face_encoding = face_info['face_encoding']

    if know_name is None:
        return XaResult.error(0, u'姓名不存在')

    if know_face_encoding is None:
        return XaResult.error(0, u'照片不存在')

    # 获取已知照片和上传照片，人脸特征点的距离
    face_distances = face_recognition.face_distance(know_face_encoding, unknown_face_encodings[0])
    print face_distances

    if not face_distances <= app.config['TOLERANCE']:
        return XaResult.success(u'人脸匹配失败')

    return XaResult.success(u'确认过眼神，是同一个人')



