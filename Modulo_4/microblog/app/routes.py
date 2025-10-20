from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app, alquimias

@app.route('/')
@login_required
def index():
    user = current_user if current_user.is_authenticated else None
    posts = alquimias.get_timeline() if user else None
    return render_template('index.html', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password']
        user = alquimias.validate_user_password(username, password)
        if user:
            login_user(user, remember=user.remember)
            return redirect(url_for('index'))
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password']
        photo = request.form['photo']
        bio = request.form['bio']
        remember = True if request.form.get('remember') == 'on' else False

        if alquimias.user_exists(username):
            return redirect(url_for('login'))
        user = alquimias.create_user(username, password, remember, photo, bio)
        login_user(user, remember=remember)
        return redirect(url_for('index'))
    return render_template('cadastro.html')

@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    if request.method == 'POST':
        body = request.form['body']
        alquimias.create_post(body, current_user)
        return redirect(url_for('index'))
    return render_template('post.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
