from app import db
from werkzeug.security import generate_password_hash, check_password_hash

PROFILE_FILE = "profiles.json"


likeimage = db.Table('likeimage',
                     db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
                     db.Column('image_id', db.Integer, db.ForeignKey('upload_image.image_id')))


likevedio = db.Table('likevedio',
                     db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
                     db.Column('vedio_id', db.Integer, db.ForeignKey('upload_vedio.vedio_id')))


class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(300))
    relate_up = db.relationship("UploadImage", backref='relate_class', lazy='dynamic')
    likeimage = db.relationship('UploadImage', secondary=likeimage, backref=db.backref('user', lazy='dynamic'), lazy='dynamic')
    likevedio = db.relationship('UploadVedio', secondary=likevedio, backref=db.backref('user', lazy='dynamic'))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def pass_hash(self, password):
        self.password = generate_password_hash(password)

    def check_hash(self, in_password):
        result = check_password_hash(self.password, in_password)
        return result

    


class UploadImage(db.Model):
    __tablename__ = "upload_image"
    image_id = db.Column(db.Integer, primary_key=True)
    up = db.Column(db.String(200), nullable=False)
    up_name = db.Column(db.String(200), nullable=False)
    image_name = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(300), nullable=False)
    image_url = db.Column(db.String(300), nullable=False)
    up_avatar = db.Column(db.String(200), nullable=False)
    likenum = db.Column(db.Integer)
    uploader = db.Column(db.Integer, db.ForeignKey("user.user_id"))

    def __init__(self, up, up_name, image, image_url, up_avatar, image_name, uploader, likenum):
        self.up = up
        self.up_name = up_name
        self.image = image
        self.image_url = image_url
        self.up_avatar = up_avatar
        self.image_name = image_name
        self.uploader = uploader
        self.likenum = likenum


class UploadVedio(db.Model):
    __tablename__ = "upload_vedio"
    vedio_id = db.Column(db.Integer, primary_key=True)
    up = db.Column(db.String(200), nullable=False)
    up_name = db.Column(db.String(200), nullable=False)
    vedio_name = db.Column(db.String(200), nullable=False)
    vedio = db.Column(db.String(300), nullable=False)
    vedio_url = db.Column(db.String(300), nullable=False)
    up_avatar = db.Column(db.String(200), nullable=False)
    likenum = db.Column(db.Integer)
    uploader = db.Column(db.Integer, db.ForeignKey("user.user_id"))

    def __init__(self, up, up_name, vedio, vedio_url, up_avatar, vedio_name, uploader, likenum):
        self.up = up
        self.up_name = up_name
        self.vedio = vedio
        self.vedio_url = vedio_url
        self.up_avatar = up_avatar
        self.vedio_name = vedio_name
        self.uploader = uploader
        self.likenum = likenum
