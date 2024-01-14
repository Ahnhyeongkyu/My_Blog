from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
from functools import wraps
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')
ckeditor = CKEditor(app)
Bootstrap(app)

#DB에 연결

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI", "sqlite:///blog.db")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager(app)

#각 테이블 config

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship("User", back_populates="posts")
    comments = db.relationship("Comment", back_populates="parent_post")

class User(UserMixin,db.Model):
    __tablename__="user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    posts = db.relationship("BlogPost", back_populates="author")
    comments = db.relationship("Comment", back_populates="comment_author")

class Comment(db.Model):
    __tablename__="comments"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comment_author = db.relationship("User", back_populates="comments")
    parent_post_id = db.Column(db.Integer, db.ForeignKey('blog_posts.id'), nullable=False)
    parent_post = db.relationship("BlogPost", back_populates="comments")

#DB 생성
with app.app_context():
    db.create_all()

#관리자 권한 데코레이터 생성
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # 현재 사용자가 로그인되어 있고 ID가 1인 경우에만 액세스 허용
        if current_user.is_authenticated and current_user.id == 1:
            return f(*args, **kwargs)
        else:
            abort(403)

    return decorated_function


#user_loader를 사용해서 current_user관리
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#홈페이지에 모든 게시물 렌더링
@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    
    return render_template("index.html", all_posts=posts)


#회원가입 페이지
@app.route('/register', methods=["GET","POST"])
def register():
    form = RegisterForm()
    
    if request.method == "POST":
        password = form.password.data
        email = form.email.data
        hash_and_salted_password = generate_password_hash(
            password,
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email = email,
            password = hash_and_salted_password,
            name = form.name.data
        )
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("이미 존재하는 이메일입니다. 해당 이메일로 로그인하세요.")
            return redirect(url_for("login"))

        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("get_all_posts"))
        
    return render_template("register.html", form=form)


#로그인 페이지
@app.route('/login', methods=["GET","POST"])
def login():
    form = LoginForm()

    if request.method == "POST":
        user = User.query.filter_by(email = form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("get_all_posts"))
        elif not user or check_password_hash(user.password, form.password.data) == False:
            flash("이메일 또는 비밀번호가 올바르지 않습니다. 다시 시도해 주세요.", 'error')
            return redirect(url_for("login"))

    return render_template("login.html", form=form)

# 사용자 정보 전역 변수로 템플릿에 전달
@app.context_processor
def inject_user():
    return dict(current_user=current_user)


#로그아웃 후 홈페이지로 이동
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


#각 게시물 렌더링 및 댓글 기능
@app.route("/post/<int:post_id>", methods=["GET","POST"])
def show_post(post_id):
    form = CommentForm()
    requested_post = BlogPost.query.get(post_id)
    comments = Comment.query.filter_by(parent_post_id=post_id).all()
    if request.method == "POST":
        if not current_user.is_authenticated:
            flash("로그인이 필요합니다")
            return redirect(url_for("login"))
        
        new_comment = Comment(
            text = form.comment.data,
            comment_author = current_user,
            parent_post = requested_post
        )

        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for("show_post", post_id=post_id))
        
    

    return render_template("post.html", post=requested_post, form=form, current_user=current_user, comments=comments)


#자기소개 페이지
@app.route("/about")
def about():
    return render_template("about.html")


#문의사항 페이지
@app.route("/contact")
def contact():
    return render_template("contact.html")


#새로운 게시물 추가 페이지(관리자만 가능)
@app.route("/new-post", methods=["GET","POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if request.method == "POST":
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


#게시물 수정 페이지(관리자만 가능)
@app.route("/edit-post/<int:post_id>", methods=["GET","POST"])
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        body=post.body
    )
    if request.method == "POST":
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form)


#게시물 삭제(관리자만 가능)
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

#댓글 삭제(관리자만 가능)
@app.route("/delete-comment/<int:comment_id>")
@admin_only
def delete_comment(comment_id):
    comment_to_delete = Comment.query.get(comment_id)
    post_id = comment_to_delete.parent_post_id
    db.session.delete(comment_to_delete)
    db.session.commit()
    return redirect(url_for("show_post", post_id=post_id))



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
