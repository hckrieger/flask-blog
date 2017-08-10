from flask import render_template, request, redirect, url_for
from models.posts import db, Post, Draft
from config import app, bootstrap
from forms.posts import PostForm
from forms.contact import ContactForm
from flask_login import login_required, current_user

	
@app.route('/dashboard')
@login_required
def dashboard():
	post = Post.query.order_by(Post.created_at.desc()).all()
	draft = Draft.query.order_by(Draft.created_at.desc()).all()
	return render_template('dashboard.html', admin=True, post=post, draft=draft)

@app.route('/')
def index():
	post = Post.query.order_by(Post.created_at.desc()).all()
	return render_template('index.html', post=post)



@app.route('/<slug>', methods=['POST', 'GET'])
def select(slug):
	post = Post.query.order_by(Post.created_at.desc()).all()
	single = Post.query.filter_by(slug=slug).first_or_404()
	return render_template('posts/select.html', single=single, post=post)
	
@app.route('/dashboard/<slug>/delete-{deletethispostnowplease}', methods=['POST', 'GET'])
@login_required
def delete(slug):
	single = Post.query.filter_by(slug=slug).first_or_404()
	db.session.delete(single)
	db.session.commit()
	return redirect(url_for('index'), admin=True)
	
@app.route('/about')
def about():
	post = Post.query.order_by(Post.created_at.desc()).all()
	return render_template('about.html', post=post)

@app.route('/contact')
def contact():
	post = Post.query.order_by(Post.created_at.desc()).all()
	return render_template('contact.html', post=post)
	
@app.route('/dashboard/create_draft', methods=['POST', 'GET'])
@login_required
def create_draft():
	form = PostForm()
	the_id = current_user.get_id()
	the_name = current_user.name
	if form.validate_on_submit():
		if form.create_draft.data:
			draft = Draft(request.form['title'], request.form['slug'], request.form['body'], the_name, request.form['category'], the_id)
			db.session.add(draft)
			db.session.commit()
			return redirect(url_for('dashboard'))
	return render_template('posts/create_draft.html', form=form, admin=True)
	
@app.route('/dashboard/<slug>/update_draft', methods=['POST', 'GET'])
@login_required
def update_draft(slug):
	form = PostForm()
	
	#grap post data 
	draft = Draft.query.filter_by(slug=slug).first_or_404()
	
	#populate form with data
	form.title.data = draft.title
	form.slug.data = draft.slug
	form.category.data = draft.category
	form.body.data = draft.body
	
	the_id = current_user.get_id()
	the_name = current_user.name
	
	#if 
	if form.validate_on_submit():
		if form.update_draft.data:
			draft.title = request.form['title']
			draft.slug = request.form['slug']
			draft.category = request.form['category']
			draft.body = request.form['body']
			db.session.commit()
			return redirect(url_for('dashboard'))
		elif form.create_post.data:
			post = Post(request.form['title'], request.form['slug'], request.form['body'], request.form['category'], the_name, the_id)
			db.session.delete(draft)
			db.session.add(post)
			db.session.commit()
			return redirect(url_for('index'))
	return render_template('posts/update_draft.html', form=form, admin=True)
	
@app.route('/dashboard/<slug>/update_post', methods=['POST', 'GET'])
@login_required
def update_post(slug):
	#Grab Form function
	form = PostForm()
	
	#grap post data 
	post = Post.query.filter_by(slug=slug).first_or_404()
	
	#populate form with data
	form.title.data = post.title
	form.slug.data = post.slug
	form.category.data = post.category
	form.body.data = post.body
	
	#declare variables for authors name and id
	the_id = current_user.get_id()
	the_name = current_user.name
	
	#update post on submit
	if form.validate_on_submit():
		if form.update_post.data:
			post.title = request.form['title']
			post.slug = request.form['slug']
			post.category = request.form['category']
			post.body = request.form['body']
			db.session.commit()
			return redirect(url_for('index'))
	return render_template('posts/update_post.html', form=form, admin=True)