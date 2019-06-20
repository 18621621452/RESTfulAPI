#!/usr/bin/env python
# encoding: utf-8

from datetime import datetime
from mongoengine import *


class Token(Document):
    user_id = StringField(required=True, unique=True)
    token = StringField(default='', unique=True)
    created = DateTimeField(default=datetime.today)