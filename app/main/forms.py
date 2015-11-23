from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from flask.ext.pagedown.fields import PageDownField

class NoteForm(Form):
    title = StringField('Title:', validators=[Required()])
    body = PageDownField('Dump Your Brain:', validators=[Required()])
    submit = SubmitField('Submit')