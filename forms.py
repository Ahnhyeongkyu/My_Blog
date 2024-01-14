from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("제목", validators=[DataRequired()])
    subtitle = StringField("부제목", validators=[DataRequired()])
    body = CKEditorField("본문", validators=[DataRequired()])
    submit = SubmitField("확인")


class RegisterForm(FlaskForm):
    email = StringField("이메일", validators=[DataRequired()])
    password = PasswordField("비밀번호", validators=[DataRequired()])
    name = StringField("이름", validators=[DataRequired()])
    submit = SubmitField("회원가입")

class LoginForm(FlaskForm):
    email = StringField("이메일", validators=[DataRequired()])
    password = PasswordField("비밀번호", validators=[DataRequired()])
    submit = SubmitField("로그인")

class CommentForm(FlaskForm):
    comment = StringField("댓글", validators=[DataRequired()])
    submit = SubmitField("확인")