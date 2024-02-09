from flask import Flask, render_template, request
import forms
app=Flask(__name__)


@app.route("/",methods=["GET","POST"])
def zodiaco():
        zodiaco_form=forms.ZodiacoForm(request.form)
        
        imagenes = {
            "rata":"https://ccl.uanl.mx/wp-content/uploads/2023/10/06_horoscopo_chino_Rata-768x657-1.jpg",
            "tigre":"https://ccl.uanl.mx/wp-content/uploads/2023/10/06_horoscopo_chino_Tigre-768x657-1.jpg",
            "buey":"https://ccl.uanl.mx/wp-content/uploads/2023/10/06_horoscopo_chino_Buey-768x657-1.jpg",
            "conejo":"https://ccl.uanl.mx/wp-content/uploads/2023/10/06_horoscopo_chino_Conejo-768x657-1.jpg",
            "dragon":"https://ccl.uanl.mx/wp-content/uploads/2023/10/06_horoscopo_chino_Dragon-768x657-1.jpg",
            "serpiente":"https://ccl.uanl.mx/wp-content/uploads/2023/10/06_horoscopo_chino_Serpiente-768x657-1.jpg",
            "caballo":"https://ccl.uanl.mx/wp-content/uploads/2023/10/06_horoscopo_chino_Caballo-768x657-1.jpg",
            "cabra":"https://ccl.uanl.mx/wp-content/uploads/2023/10/06_horoscopo_chino_Cabra-768x657-1.jpg",
            "mono":"https://ccl.uanl.mx/wp-content/uploads/2023/10/06_horoscopo_chino_Mono-768x657-1.jpg",
            "gallo":"https://ccl.uanl.mx/wp-content/uploads/2023/10/06_horoscopo_chino_Gallo-768x657-1.jpg",
            "perro":"https://ccl.uanl.mx/wp-content/uploads/2023/10/06_horoscopo_chino_Perro-768x657-1.jpg",
            "cerdo":"https://ccl.uanl.mx/wp-content/uploads/2023/10/06_horoscopo_chino_Cerdo-768x657-1.jpg",
        }
        
        if request.method=="POST":
              
            nombre=request.form.get("nombre")
            apaterno=request.form.get("apaterno")
            amaterno=request.form.get("amaterno")
            dia=request.form.get("dia")
            mes=request.form.get("mes")
            anio=request.form.get("anio")
            
            edad = 2024-int(anio)
            
            if int(mes) < 2 or (int(mes) == 2 and int(dia) < 8):
                edad=edad-1
                
            signo = ""
            
            
            if int(anio) in (1936, 1948, 1960, 1972, 1984, 1996, 2008):
                signo ="rata"
            elif int(anio) in (1937, 1949, 1961, 1973, 1985, 1997, 2009):
                signo ="tigre"
            elif int(anio) in (1938, 1950, 1962, 1974, 1986, 1998, 2010):
                signo ="buey"
            elif int(anio) in (1939, 1951, 1963, 1975, 1987, 1999, 2011):
                signo ="conejo"
            elif int(anio) in (1940, 1952, 1964, 1976, 1988, 2000, 2012):
                signo ="dragon"
            elif int(anio) in (1941, 1953, 1965, 1977, 1989, 2001, 2013):
                signo ="serpiente"
            elif int(anio) in (1942, 1954, 1966, 1978, 1990, 2002, 2014):
                signo ="caballo"
            elif int(anio) in (1943, 1955, 1967, 1979, 1991, 2003, 2015):
                signo ="cabra"
            elif int(anio) in (1944, 1956, 1968, 1980, 1992, 2004, 2016):
                signo ="mono"
            elif int(anio) in (1945, 1957, 1969, 1981, 1993, 2005, 2017):
                signo ="gallo"
            elif int(anio) in (1946, 1958, 1970, 1982, 1994, 2006, 2018):
                signo ="perro"
            elif int(anio) in (1947, 1959, 1971, 1983, 1995, 2007, 2019):
                signo ="cerdo"
            
            
            
            return render_template("result_zodiaco.html", 
                                   nombre = nombre+" "+apaterno+" "+amaterno,
                                   edad= edad,
                                   signo = signo,
                                   imagen = imagenes[signo])
        else:
            return render_template("form_zodiaco.html",
                                   form = zodiaco_form)
            

if __name__=="__main__":
    app.run(debug=True,port=4000)

