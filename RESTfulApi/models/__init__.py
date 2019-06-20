#!/usr/bin/env python
# encoding: utf-8

from shop_db import *
from mongoengine import connect


def register_database(app):
    database = app.config['MONGODB_SETTINGS']['DB']
    connect(database)