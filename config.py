"""
    configurations for the server and DB
"""

from io import BytesIO
from flask import Flask , request, jsonify, redirect, render_template, url_for, session, send_file
from flask_sqlalchemy import SQLAlchemy
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.sql import func
from creds import db_cred

app = Flask(__name__, template_folder="templates")
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True   # makes json output more readable

# set the database to work with flask
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_cred["username"]}:{db_cred["password"]}@localhost/file_sys' #mysql://username:password@server/db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Set to True if you want Flask-SQLAlchemy to track modifications of objects and emit signals
db = SQLAlchemy(app)