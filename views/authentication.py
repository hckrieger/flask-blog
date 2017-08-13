from flask import render_template, request, redirect, url_for
from config import app
from models.authentication import db, User
from forms.authentication import LoginForm, RegisterForm
from flask_login import login_user, login_required, logout_user, current_user, login_required, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))
	
@app.route('/login', methods=['POST', 'GET'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user:
			if check_password_hash(user.password, form.password.data):
				login_user(user, remember=form.remember.data)
				return redirect(url_for('dashboard'))
	return render_template('login.html', form=form, admin=True)
	
'''@app.route('/signup', methods=['POST', 'GET'])
def signup():
	form = RegisterForm()
	if form.validate_on_submit():
		hashed_password = generate_password_hash(form.password.data, method='sha256')
		new_user = User(name=form.name.data, email=form.email.data, password=hashed_password)
		db.session.add(new_user)
		db.session.commit()
		return 'user has been created'
	return render_template('signup.html', form=form, admin=True)
	'''
	
@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))