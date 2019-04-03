#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

from app import db


class FaceDict(db.Document):
    name = db.StringField(max_length=255, required=True)
    faceEncoding = db.ListField()
