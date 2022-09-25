"""
    configurations for the server and DB
"""

# import os
from io import BytesIO
from flask import Flask , request, jsonify, redirect, render_template, url_for, session, send_file
from flask_sqlalchemy import SQLAlchemy
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from creds import db_cred


user = db_cred['MYSQL_USER']
password = db_cred['MYSQL_PASSWORD']
host = db_cred['MYSQL_HOST']
port = db_cred['MYSQL_PORT']
database = db_cred ['MYSQL_DB']
DATABASE_URI = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'



app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)