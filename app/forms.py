from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length


class UserForm(FlaskForm):
    name = StringField(label="Ваше Iмя та Прiзвище", validators=[Length(min=4, max=20)])
    button = SubmitField("Привітатись")
