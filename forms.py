from wtforms import Form
from wtforms import StringField, TextAreaField,IntegerField, SelectField, RadioField
from wtforms import EmailField
from wtforms import validators


class UserForm(Form):
    nombre=StringField("nombre")
    email=EmailField("correo")
    apaterno=StringField("apaterno")
    materias=SelectField(choices=[('Español','Esp'),('Mat','Matematicas'),('Ingles','Ing')])
    radios= RadioField('Curso',choices=[('1','1'),('2','2'),('3','3')])
    
class DistanceForm(Form):
    n1=StringField("n1")
    n2=StringField("n2")
    n3=StringField("n3")
    n4=StringField("n4")
    
class CineForm(Form):
    cant_boletos=StringField("nombre")
    cant_personas=EmailField("correo")
    precio_boleto=StringField("apaterno")
    tarjeta=SelectField(choices=[('Español','Esp'),('Mat','Matematicas'),('Ingles','Ing')])
    radios= RadioField('Curso',choices=[('1','1'),('2','2'),('3','3')])
    
class ZodiacoForm(Form):
    nombre=StringField("nombre")
    apaterno=StringField("apaterno")
    amaterno=StringField("amaterno")
    dia=StringField("dia")
    mes=StringField("mes")
    anio=StringField("anio")
    sexo= RadioField(choices=[('m','Masculino'),('f','Femenino')])
    
class ResistenciaForm(Form):
    banda1=SelectField(choices=[
                                 ('0','Negro'),
                                 ('1','Cafe'),
                                 ('2','Rojo'),
                                 ('3','Naranja'),
                                 ('4','Amarillo'),
                                 ('5','Verde'),
                                 ('6','Azul'),
                                 ('7','Violeta'),
                                 ('8','Gris'),
                                 ('9','Blanco')
                                 ])
    banda2=SelectField(choices=[
                                 ('0','Negro'),
                                 ('1','Cafe'),
                                 ('2','Rojo'),
                                 ('3','Naranja'),
                                 ('4','Amarillo'),
                                 ('5','Verde'),
                                 ('6','Azul'),
                                 ('7','Violeta'),
                                 ('8','Gris'),
                                 ('9','Blanco')
                                 ])
    banda3=SelectField(choices=[
                                 ('0','Negro'),
                                 ('1','Cafe'),
                                 ('2','Rojo'),
                                 ('3','Naranja'),
                                 ('4','Amarillo'),
                                 ('5','Verde'),
                                 ('6','Azul'),
                                 ('7','Violeta'),
                                 ('8','Gris'),
                                 ('9','Blanco', {'style':'background-color:white; color: black'})
                                 ])
    tolerancia= RadioField(choices=[('0.05','Dorado'),('0.10','Plata')])

class TraductorForm1(Form):
    ingles=StringField("ingles",
                       [validators.DataRequired(message='el campo en ingles es requerido'),
        validators.length(min=2, max=50, message='Ingresa una palabra valida')])
    espanol=StringField("espanol",
                       [validators.DataRequired(message='el campo en español es requerido'),
        validators.length(min=2, max=50, message='Ingresa una palabra valida')])
class TraductorForm2(Form):
    palabra=StringField("palabra",
                       [validators.DataRequired(message='el campo palabra es requerido'),
        validators.length(min=2, max=50, message='Ingresa una palabra valida')])
    idioma= RadioField('idioma',choices=[('ingles','Inglés'),('espanol','Español')], validators=[validators.DataRequired(message='Selecciona un idioma')])
    