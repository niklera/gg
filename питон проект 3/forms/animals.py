from flask_wtf import FlaskForm   #это все библиотеки и методы
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class AnimalsForm(FlaskForm):
    title = StringField('Имя, название животного', validators=[DataRequired()])
    content = TextAreaField("Краткое описание")
    longcontent = TextAreaField("Полная характеристика")
    is_private = BooleanField("Показывать только мне")
    submit = SubmitField('Применить')