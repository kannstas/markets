from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class ReviewForm(FlaskForm):
    user_nickname = StringField('Nickname', validators=[DataRequired()])
    text = TextAreaField('Review Text')
    rating = IntegerField('Rating', validators=[DataRequired(), NumberRange(min=1, max=5)])
    submit = SubmitField('Submit')