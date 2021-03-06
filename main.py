#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib import quote_plus

from flask import Flask
from flask_pymongo import PyMongo

from flask_restful import Api
from router import home, dashboard
import config
# Khởi tạo db

from api.googlecloudstore import *

# DbMongo().init_db()

# Khởi tạo app
app = Flask(__name__)

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

# Configure this environment variable via app.yaml
CLOUD_STORAGE_BUCKET = os.environ['CLOUD_STORAGE_BUCKET']
# [end config]

# connect to another MongoDB server altogether
# app.config['MC_MONGO_URI'] = "mongodb://username:password@host:port/database"

uri = "mongodb://%s:%s@%s/%s?%s" % (
    quote_plus("thangld_1202_user"),
    quote_plus("QAZwsx*098#pl,"),
    "35.184.69.50:27017",
    quote_plus("test"),
    "authMechanism=SCRAM-SHA-1")

app.config['MC_MONGO_URI'] = uri
# app.config['MC_MONGO_HOST'] = config.DB_IP["ip"]
# app.config['MC_MONGO_PORT'] = config.DB_IP["port"]
# app.config['MC_MONGO_DBNAME'] = quote_plus(config.DB_NAME)
# app.config['MC_MONGO_USERNAME'] = quote_plus(config.DB_ACCOUNT["user"])
# app.config['MC_MONGO_PASSWORD'] = quote_plus(config.DB_ACCOUNT["password"])
mongo = None
# PyMongo(app, config_prefix='MC_MONGO')

app.debug = True

# Đăng ký các url
home.register_urls(app)
dashboard.register_urls(app)

from api import restful_api_mobile

restful_api_mobile.register_extra(app)
# Đăng ký api
# api_mobile.register_urls(app)

from routermobile import routermanager

api = Api(app)
routermanager.add_resources(api)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
