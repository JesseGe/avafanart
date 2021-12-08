from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, render_template, url_for, flash
from flask_wtf import Form
from wtforms import StringField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired

app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config["SECRET_KEY"] = "123456"

db = SQLAlchemy(app)
