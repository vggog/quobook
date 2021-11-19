from app import app, db
from flask import render_template, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import app.forms as forms
from app.models import Users
from app import generate_token
from flask_login import logout_user, login_user, current_user


@app.route('/')
@app.route('/home')
def home():
    """Возвращает страницу home"""
    return render_template('home.html', title='Home')


@app.route('/documentation')
def docs():
    """Возвращает страницу с документацией"""
    return render_template('documentation.html', title='Documentation')


@app.route('/registration', methods=['GET', 'POST'])
def reg():
    """Возвращает страницу с регистрацией"""
    if current_user.is_authenticated:
        return render_template('after_login.html')
    login = forms.RegistrationForm()
    if login.validate_on_submit():
        if Users.query.filter_by(email=login.email.data).first():
            flash('Пользователь c таким email-адресом уже существует.')
            return redirect(url_for('reg'))

        user = Users(id=Users.query.count() + 1, email=login.email.data,
                     password_hash=generate_password_hash(login.password.data),
                     token=generate_token.generate_token())
        db.session.add(user)
        db.session.commit()
        flash('Вы успешно зарегистрировались.')
        login_user(user, remember=login.remember_me.data)
        return render_template('after_login.html')
    return render_template('registration.html', title='registration', form=login)


@app.route('/login', methods=['GET', 'POST'])
def get_token():
    """Страница аутентификации"""
    if current_user.is_authenticated:
        return render_template('after_login.html')
    login = forms.LoginForm()
    if login.validate_on_submit():
        user = Users.query.filter_by(email=login.email.data).first()
        if not user:
            flash('Вы не зарегистрированы.')
            return redirect(url_for('get_token'))

        if not check_password_hash(Users.query.filter_by(email=login.email.data).first().password_hash,
                                   login.password.data):
            flash('Пароль не верный.')
            return redirect(url_for('get_token'))

        # flash(f'Ваш токен: {Users.query.filter_by(email=login.email.data).first().token}')
        login_user(user, remember=login.remember_me.data)
        return render_template('after_login.html')
    return render_template('token.html', title='token', form=login)


@app.route('/quote')
def get_a_quote():
    """Возвращает страницу получения токена"""
    return render_template('get_quote.html', title='Home')


@app.route('/add_quote')
def add_quote():
    """Возвращает страницу добавления токена"""
    return render_template('add_quote.html', title='Documentation')


@app.route('/logout')
def logout():
    """Страница выхода"""
    logout_user()
    return redirect(url_for('get_token'))
