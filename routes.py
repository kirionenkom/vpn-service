from flask import request, redirect, render_template, send_file, flash
from flask_login import login_user, login_required, current_user

from User import User
from app import app
from create_client import create_client
from database import get_user_by_username, create_user


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_id = create_user(username, password)
        user = User.get(user_id)
        create_client(user)
        login_user(user)
        return redirect('/')
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = get_user_by_username(username, password)
        if user:
            user = User.get(user[0])
            login_user(user)
            return redirect('/')
        else:
            flash('Invalid username or password')
    return render_template('login.html')


@app.route('/')
@login_required
def profile():
    user = current_user
    print(current_user)
    return render_template('profile.html', user = user)


@app.route('/config', methods=['POST'])
@login_required
def config():
    user = current_user
    return send_file(f'/etc/wireguard/clients/confs/{user.username}.conf')