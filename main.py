from flask import Flask, request,render_template
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def calculadora():
        if request.method=="POST":
            num1=(request.form.get("n1"))
            num2=(request.form.get("n2"))
            op=(request.form.get("operacion"))
            if "*" in op:
                res = str(int(num1) * int(num2))
                return render_template("form.html", resultado=res)
            if "/" in op:
                res = str(int(num1) / int(num2))
                return render_template("form.html", resultado=res)
            if "-" in op:
                res = str(int(num1) - int(num2))
                return render_template("form.html", resultado=res)
            if "+" in op:
                res = str(int(num1) + int(num2))
                return render_template("form.html", resultado=res)
        else:
            return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)