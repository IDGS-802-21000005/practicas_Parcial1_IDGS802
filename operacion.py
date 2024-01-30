from flask import Flask, request,render_template
import forms
app = Flask(__name__)


@app.route("/",methods=["GET","POST"])
def distancia():
    alumnos_form=forms.UserForm(request.form)
    res=""
    if request.method == "POST":
        n1=int(alumnos_form.n1.data)
        n2=int(alumnos_form.n2.data)
        n3=int(alumnos_form.n3.data)
        n4=int(alumnos_form.n4.data)
        res= ((n1-n2)**2+(n3-n4)**2)**(1/2)
    return render_template("operacion.html", form=alumnos_form, res=str(res))
    



if __name__ == "__main__":
    app.run(debug=True)