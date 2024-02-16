from flask import Flask, request,render_template
import forms
app = Flask(__name__)

@app.route("/agregar",methods=["POST","GET"])
def agregar():
    traductor1_form=forms.TraductorForm1(request.form)
    traductor2_form=forms.TraductorForm2(request.form)
    palabras=[]
    traduccion=""
    if request.method == "POST" and traductor1_form.validate():
        
        nueva_palabra = traductor1_form.ingles.data+':'+traductor1_form.espanol.data
        
        archivo = open("palabras.txt", "a")
        archivo.write(nueva_palabra+"\n")
        archivo.close()
        
    archivo = open("palabras.txt", "r")
    for lineas in archivo.readlines():
        par = lineas.split(":")
        palabras.append({"ingles":par[0],"espanol":par[1]})
    archivo.close()
        
    return render_template("traductor.html", form1=traductor1_form, form2=traductor2_form, palabras=palabras, trad = traduccion)

@app.route("/traducir",methods=["POST","GET"])
def traducir():
    traductor1_form=forms.TraductorForm1(request.form)
    traductor2_form=forms.TraductorForm2(request.form)
    palabras=[]
    traduccion=""
    if request.method == "POST" and traductor2_form.validate():
        
        palabra = traductor2_form.palabra.data
        idioma = traductor2_form.idioma.data
        
        archivo = open("palabras.txt", "r")
        for lineas in archivo.readlines():
            par = lineas.rstrip().split(":")
            print(palabra +""+ par[1])
            if idioma == "ingles" and palabra == par[0]:
                    traduccion = par[1]
            elif idioma == "espanol" and palabra == par[1]:
                traduccion = par[0]
        archivo.close()
        
    archivo = open("palabras.txt", "r")
    for lineas in archivo.readlines():
        par = lineas.split(":")
        palabras.append({"ingles":par[0],"espanol":par[1]})
    archivo.close()
        
    return render_template("traductor.html", form1=traductor1_form, form2=traductor2_form, palabras=palabras, trad = traduccion)


if __name__ == "__main__":
    app.run(debug=True)