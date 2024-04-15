from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class NewsForm(FlaskForm):
    title = StringField('Имя, название животного', validators=[DataRequired()])
    content = TextAreaField("Описание")
    is_private = BooleanField("Показывать только мне")
    submit = SubmitField('Применить')