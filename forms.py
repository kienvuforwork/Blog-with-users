from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email, Length
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class Register(FlaskForm):
    email = StringField("Your email", validators=[DataRequired(), Email()])
    password = PasswordField(validators=[Length(min=4, max=25)])
    name = StringField("Your name", validators=[DataRequired()])
    submit = SubmitField("Submit")

class Login(FlaskForm):
    email = StringField("Your email", validators=[DataRequired(), Email()])
    password = PasswordField(validators=[Length(min=4, max=25)])
    submit = SubmitField("Log in")

class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")