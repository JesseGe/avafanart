from flask import render_template, url_for, request, flash, redirect, session
from app import app, db
from .model import User, UploadImage, UploadVedio
from .forms import Register, LoginForm, UploadI, UploadV, Changepass


@app.route("/")
def homepage():
    images = UploadImage.query.all()
    vedios = UploadVedio.query.all()
    if session.get('username'):
        like = User.query.filter_by(user_id=session.get('userid')).first()
        checki = like.likeimage
        checkv = like.likevedio
        return render_template('main.html', username=session.get('username'), images=images, vedios=vedios, likeimage=checki, likevedio=checkv)
    return render_template('main.html', username=session.get('username'), images=images, vedios=vedios)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Register()
    if request.method == "GET":
        return render_template('register.html', form=form)
    elif request.method == "POST":
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user:
                flash(message='email number has been registered',
                      category='danger')
                return render_template('register.html', form=form)
            else:
                if form.password.data == form.repassword.data:
                    add_user = User(form.username.data, form.email.data,
                                    form.password.data)
                    add_user.pass_hash(form.password.data)
                    try:
                        db.session.add(add_user)
                        db.session.commit()
                        flash(message='Register successfully, please login',
                              category='success')
                        return redirect('/login')
                    except Exception:
                        db.session.rollback()
                        return 'There was an issue while updating that task'
                else:
                    flash(
                        message='The passwords entered twice are not the same',
                        category='danger')
                    return render_template('register.html', form=form)
        else:
            return 'None'


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None
    if request.method == "GET":
        return render_template('login.html', form=form)
    if request.method == 'POST':
        name = request.form['email']
        pawd = request.form['password']

        user = User.query.filter_by(email=name).first()
        if user:
            if user.check_hash(pawd):
                session['userid'] = user.user_id
                session['username'] = user.username
                session.permanent = True
                flash(message='登录成功，欢迎'+user.username+'!', category='success')
                return redirect('/')
            else:
                flash(message='登录失败', category='danger')
                return render_template('login.html', form=form)
        flash(message='登录失败', category='danger')
        return render_template('login.html', form=form)

    return render_template('login.html', error=error, form=form)


@app.route('/change', methods=['GET', 'POST'])
def change():
    form = Changepass()
    user = User.query.get(session.get('userid'))
    if request.method == "GET":
        return render_template('change.html', form=form, username=session.get('username'))
    if request.method == 'POST':
        if user.check_hash(form.opassword.data):
            if form.password.data == form.repassword.data:
                try:
                    user.pass_hash(form.password.data)
                    db.session.commit()
                    flash(message='更改密码成功!', category='success')
                    return redirect('/')
                except Exception:
                    db.session.rollback()
                    return 'There was an e`rror while deleting that task'
            else:
                flash(message='请输入相同的更改密码', category='danger')
                return render_template('change.html', form=form, username=session.get('username'))
        else:
            flash(message='请输入正确的初始密码', category='danger')
            return render_template('change.html', form=form, username=session.get('username'))
    flash(message='发生错误', category='danger')
    return render_template('change.html', form=form, username=session.get('username'))


@app.route('/logout')
def logout():
    session.clear()
    flash(message='成功注销', category='success')
    return redirect('/')


@app.route('/uploadimage', methods=['GET', 'POST'])
def uploadi():
    form = UploadI()
    if request.method == "GET":
        return render_template('upload_image.html', form=form, username=session.get('username'))
    elif request.method == "POST":
        if form.validate_on_submit():
            image_url = UploadImage.query.filter_by(image_url=form.image_url.data).first()
            if image_url:
                flash(message='Image has been uploaded',
                      category='danger')
                return render_template('upload_image.html', form=form, username=session.get('username'))
            else:
                add_image = UploadImage(form.up.data,
                                        form.up_name.data,  form.image.data,
                                        form.image_url.data,
                                        form.up_avatar.data,
                                        form.image_name.data, session.get('userid'), likenum=0)
                try:
                    db.session.add(add_image)
                    db.session.commit()
                    flash(message='Register successfully, please login',
                          category='success')
                    return redirect('/')
                except Exception:
                    db.session.rollback()
                    return 'There was an issue while updating that task'
        else:
            return 'None'


@app.route('/uploadvedio', methods=['GET', 'POST'])
def uploadv():
    form = UploadV()
    if request.method == "GET":
        return render_template('upload_vedio.html', form=form, username=session.get('username'))
    elif request.method == "POST":
        if form.validate_on_submit():
            vedio_url = UploadVedio.query.filter_by(vedio_url=form.vedio_url.data).first()
            if vedio_url:
                flash(message='vedio has been uploaded',
                      category='danger')
                return render_template('upload_vedio.html', form=form, username=session.get('username'))
            else:
                add_vedio = UploadVedio(form.up.data,
                                        form.up_name.data, form.vedio.data,
                                        form.vedio_url.data,
                                        form.up_avatar.data,
                                        form.vedio_name.data, session.get('userid'), likenum=0)
                try:
                    db.session.add(add_vedio)
                    db.session.commit()
                    flash(message='Register successfully, please login',
                          category='success')
                    return redirect('/')
                except Exception:
                    db.session.rollback()
                    return 'There was an issue while updating that task'
        else:
            return 'None'


@app.route('/showlike')
def showlike():
    like = User.query.filter_by(user_id=session.get('userid')).first()
    checki = like.likeimage
    checkv = like.likevedio
    getvedio = None
    getimage = None
    if checki:
        if checkv:
            getimage_id = []
            getvedio_id = []
            for i in checki:
                getimage_id.append(i.image_id)
            getimage = UploadImage.query.filter(UploadImage.image_id.in_(getimage_id)).all()
            for v in checkv:
                getvedio_id.append(v.vedio_id)
            getvedio = UploadVedio.query.filter(UploadVedio.vedio_id.in_(getvedio_id)).all()
            return render_template('like.html', username=session.get('username'), images=getimage, vedios=getvedio)
        getimage_id = []
        for i in checki:
            getimage_id.append(i.image_id)
        getimage = UploadImage.query.filter(UploadImage.image_id.in_(getimage_id)).all()
        return render_template('like.html', username=session.get('username'), images=getimage)
    elif checkv:
        getvedio_id = []
        for v in checkv:
            getvedio_id.append(v.vedio_id)
        getvedio = UploadVedio.query.filter(UploadVedio.vedio_id.in_(getvedio_id)).all()
        return render_template('like.html', username=session.get('username'), vedios=getvedio)
    return render_template('like.html', username=session.get('username'))


@app.route('/likeimage/<int:id>', methods=['GET'])
def like(id):
    like = User.query.filter_by(user_id=session.get('userid')).first()
    images = UploadImage.query.all()
    vedios = UploadVedio.query.all()
    image = like.likeimage
    vedio = like.likevedio
    goti = UploadImage.query.get(id)
    if image:
        for i in image:
            if id == i.image_id:
                try:
                    like.likeimage.remove(goti)
                    db.session.commit()
                    return render_template('likeimage.html', username=session.get('username'), images=images, vedios=vedios, likeimage=image, likevedio=vedio)
                except Exception:
                    db.session.rollback()
                    return 'There was an issue while updating that task'
    like.likeimage.append(goti)
    try:
        db.session.commit()
        return render_template('likeimage.html', username=session.get('username'), images=images, vedios=vedios, likeimage=image, likevedio=vedio)
    except Exception:
        db.session.rollback()
        return 'There was an issue while updating that task'


@app.route('/likevedio/<int:id>', methods=['GET'])
def likev(id):
    like = User.query.filter_by(user_id=session.get('userid')).first()
    images = UploadImage.query.all()
    vedios = UploadVedio.query.all()
    image = like.likeimage
    vedio = like.likevedio
    goti = UploadVedio.query.get(id)
    if vedio:
        for i in vedio:
            if id == i.vedio_id:
                try:
                    like.likevedio.remove(goti)
                    db.session.commit()
                    return render_template('likevedio.html', username=session.get('username'), images=images, vedios=vedios, likeimage=image, likevedio=vedio)
                except Exception:
                    db.session.rollback()
                    return 'There was an issue while updating that task'
    like.likevedio.append(goti)
    try:
        db.session.commit()
        return render_template('likevedio.html', username=session.get('username'), images=images, vedios=vedios, likeimage=image, likevedio=vedio)
    except Exception:
        db.session.rollback()
        return 'There was an issue while updating that task'


@app.route('/di/<int:id>', methods=['GET'])
def di(id):
    like = User.query.filter_by(user_id=session.get('userid')).first()
    image = UploadImage.query.get(id)
    like.likeimage.remove(image)
    try:
        db.session.commit()
        likeimage = like.likeimage
        vedio = like.likevedio
        return render_template('deletei.html', username=session.get('username'), images=likeimage, vedios=vedio)
    except Exception:
        db.session.rollback()
        return 'There was an issue while updating that task'


@app.route('/dv/<int:id>', methods=['GET'])
def dv(id):
    like = User.query.filter_by(user_id=session.get('userid')).first()
    vedio = UploadVedio.query.get(id)
    like.likevedio.remove(vedio)
    try:
        db.session.commit()
        likeimage = like.likeimage
        vedio = like.likevedio
        return render_template('deletev.html', username=session.get('username'), images=likeimage, vedios=vedio)
    except Exception:
        db.session.rollback()
        return 'There was an issue while updating that task'


@app.route('/alert', methods=['GET'])
def alert():
    return render_template('alert.html')
