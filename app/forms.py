#coding:utf-8
from flask_wtf import Form  ###从Flask-WTF扩展导入Form基类
from wtforms import IntegerField, StringField, PasswordField, BooleanField, TextField, TextAreaField, SubmitField  ###从WTForms包中导入字段类
from wtforms.validators import Required, Length, Email, DataRequired  ###从WTForms导入验证函数
from wtforms.fields.html5 import DateField



class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])


class Register(Form):
    email = StringField('Email', validators=[DataRequired()])
    username = StringField('User Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    repassword = PasswordField('RePassword', validators=[DataRequired(), Length(min=6)])


class Changepass(Form):
    opassword = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    repassword = PasswordField('Password', validators=[DataRequired(), Length(min=6)])


class UploadI(Form):
    up = StringField('Up', validators=[DataRequired()])
    up_name = StringField('Up_name', validators=[DataRequired()])
    image_name = StringField('Image_name', validators=[DataRequired()])
    image = StringField('Image', validators=[DataRequired()])
    image_url = StringField('Image_url', validators=[DataRequired()])
    up_avatar = StringField('Up_avatar', validators=[DataRequired()])


class UploadV(Form):
    up = StringField('Up', validators=[DataRequired()])
    up_name = StringField('Up_name', validators=[DataRequired()])
    vedio_name = StringField('Vedio_name', validators=[DataRequired()])
    vedio = StringField('Vedio', validators=[DataRequired()])
    vedio_url = StringField('Vedio_url', validators=[DataRequired()])
    up_avatar = StringField('Up_avatar', validators=[DataRequired()])

