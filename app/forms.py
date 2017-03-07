from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators, SelectField


class JobAdForm(FlaskForm):
    texttotest = TextAreaField(u'', [validators.Length(min=1)])
    language = SelectField('Language', choices = [ ("sv", "swedish"), ("en", "english") ])
