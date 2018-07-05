from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators


class LoginForm(FlaskForm):
    email = EmailField(label="邮箱", validators=[validators.Email()])
    password = PasswordField(label="密码", validators=[validators.Length(min=8)])
    default = BooleanField(label="  记住我", default=True)
    submit = SubmitField('登录')
