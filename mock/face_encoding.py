#!/usr/bin/env python
# -*- coding: utf-8 -*-

import face_recognition

# print face_recognition.face_encodings(face_recognition.load_image_file(u'/Users/huan/sources/python-sources/face-recognition-service/face_data/know_face_dir/王思聪.jpeg'))
# print face_recognition.face_encodings(face_recognition.load_image_file(u'/Users/huan/sources/python-sources/face-recognition-service/face_data/know_face_dir/林狗.jpeg'))

print face_recognition.face_encodings(face_recognition.load_image_file(u'/Users/huan/sources/python-sources/face-recognition-service/face_data/know_face_dir/张曼.jpg'))
print face_recognition.face_encodings(face_recognition.load_image_file(u'/Users/huan/sources/python-sources/face-recognition-service/face_data/know_face_dir/宋克军.JPG'))