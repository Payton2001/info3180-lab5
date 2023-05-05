from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed, FileRequired

class MovieForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    poster = FileField("Poster", validators=[InputRequired(), FileRequired(), FileAllowed(['jpg','jpeg', 'jfif', 'png', 'gif'], 'Images only')])
    