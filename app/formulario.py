from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

class Contactenos(FlaskForm):
    nombre= StringField('nombre',validators=[DataRequired(message='No dejar vacío, completar')])
    correo= EmailField('correo',validators=[DataRequired(message='No dejar vacío, completar')])
    mensaje= StringField('mensaje',validators=[DataRequired(message='No dejar vacío, completar')])
    enviar=SubmitField('Enviar Mensaje',  render_kw={'class':'form_boton'})

