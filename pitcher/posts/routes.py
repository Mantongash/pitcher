from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from pitcher import db
from pitcher.models import Pitch, Comment
from pitcher.posts.forms import PostForm,CommentForm

posts = Blueprint("posts",__name__)

@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Pitch(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template("post.html", title = "New post", form=form)
    
    
@posts.route("/post/<int:post_id>", methods=['GET', 'POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(content=form.content.data)
        db.session.add(comment)
        #db.session.commit()
        flash('Your comment has been posted!', 'success')
        return redirect(url_for('main.home'))
    return render_template('posted.html', title=post.title, post=post,form=form)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Pitch.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=pitch.id))
    elif request.method == 'GET':
        form.title.data = pitch.title
        form.content.data = pitch.content
    return render_template("postupdate.html", title = "Update Post", form=form, legend= "Update Post")


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Pitch.query.get_or_404(post_id)
    if pitch.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Your pitch has been succesfully deleted", "success")
    return redirect(url_for("main.home"))
