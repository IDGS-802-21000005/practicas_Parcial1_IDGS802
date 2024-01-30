from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField, RadioField
from wtforms import EmailField
class UserForm(Form):
    nombre=StringField("nombre")
    n1=StringField("n1")
    n2=StringField("n2")
    n3=StringField("n3")
    n4=StringField("n4")
    email=EmailField("correo")
    apaterno=StringField("apaterno")
    materias=SelectField(choices=[('Español','Esp'),('Mat','Matematicas'),('Ingles','Ing')])
    radios= RadioField('Curso',choices=[('1','1'),('2','2'),('3','3')])
