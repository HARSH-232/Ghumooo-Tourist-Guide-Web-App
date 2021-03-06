
   
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from flask import request, render_template, Flask


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("Login copy.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)

@auth.route('/content')
def content():
    return render_template('Content2.html')

@auth.route('/contributors')
def contributors():
    return render_template('contributors.html')

@auth.route('/main')
def main():
    return render_template('Mahabaleshwar.html')

@auth.route('/Food')
def food():
    return render_template('Food.html')

@auth.route('/info')
def info():
    return render_template('Mahabaleshwar_sub.html')

@auth.route('/Nagpur')
def Nagpur():
    return render_template('Nagpur.html')

@auth.route('/NagpurInfo')
def NagpurInfo():
    return render_template('Nagpur_sub.html')

@auth.route('/Ratnagiri')
def Ratnagiri():
    return render_template('Ratnagiri.html')

@auth.route('/RatnagiriInfo')
def RatnagiriInfo():
    return render_template('Ratnagiri_sub.html')

@auth.route('/Goa')
def Goa():
    return render_template('Goa.html')

@auth.route('/GoaInfo')
def GoaInfo():
    return render_template ('Goa_sub.html')

@auth.route('/Mumbai')
def Mumbai():
    return render_template('Mumbai.html')

@auth.route('/MumbaiInfo')
def MumbaiInfo():
    return render_template('Mumbai_sub.html')

@auth.route('/Varanasi')
def Varanasi():
    return render_template('Varanasi.html')

@auth.route('/VaranasiInfo')
def VaranasiInfo():
    return render_template ('Varanasi_sub.html')

@auth.route('/Jaipur')
def Jaipur():
    return render_template('Jaipur.html')

@auth.route('/JaipurInfo')
def JaipurInfo():
    return render_template ('Jaipur_sub.html')

@auth.route('/Agra')
def Agra():
    return render_template('Agra.html')

@auth.route('/AgraInfo')
def AgraInfo():
    return render_template('Agra_sub.html')
    
@auth.route('/Jaisalmer')
def Jaisalmer():
    return render_template('Jaisalmer.html')

@auth.route('/JaisalmerInfo')
def JaisalmerInfo():
    return render_template('Jaisalmer_sub.html')

@auth.route('/Guides')
def Guides():
    return render_template('Guides.html')

@auth.route('/Food_mahabaleshwar')
def Food_mahabaleshwar():
    return render_template('food_mahabaleshwar.html')

@auth.route('/Food_goa')
def Food_goa():
    return render_template('food_goa.html')

@auth.route('/Food_nagpur')
def Food_nagpur():
    return render_template('food_nagpur.html')

@auth.route('/Food_varanasi')
def Food_varanasi():
    return render_template('food_varanasi.html')

@auth.route('/Food_jaipur')
def Food_jaipur():
    return render_template('food_jaipur.html')

@auth.route('/Food_mumbai')
def Food_mumbai():
    return render_template('food_mumbai.html')

@auth.route('/Food_ratnagiri')
def Food_ratnagiri():
    return render_template('food_ratnagiri.html')

@auth.route('/Food_agra')
def Food_agra():
    return render_template('food_agra.html')