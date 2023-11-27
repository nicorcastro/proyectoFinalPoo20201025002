from flask import Flask, render_template, request, redirect, url_for, flash
from db import db
from puntoInteres import puntoInteres

class Programa:
     
    def __init__(self):
         
         self.app=Flask(__name__)
         self.app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///puntosinteres.sqlite3"
         
         #Agregar la db a nuestra aplicación
         db.init_app(self.app)
         
         self.app.add_url_rule('/', view_func=self.visorGeografico)
         self.app.add_url_rule('/nuevo', view_func=self.agregar, methods=["GET", "POST"])
         
         #Iniciar el servidor
         with self.app.app_context():
             db.create_all()
         self.app.run(debug=True)
         
         
    def visorGeografico(self):
        return render_template('visorGeografico.html', puntosInteres=puntoInteres.query.all())
    
    
    def agregar(self):
        #Verificar si debe enviar el formulario o procesar los datos
        if request.method=="POST":
            #Obtener los datos del formulario
            nombre=request.form["nombre"]
            latitud=request.form["latitud"]
            longitud=request.form["longitud"]
            nomenclatura=request.form["nomenclatura"]
            numeroObrasVenta=request.form["numeroObrasVenta"]
            horario=request.form["horario"] 
            #Procesar la imagen
            fotografiaFachada = None
            if 'fotografiaFachada' in request.files:
                imagen = request.files['fotografiaFachada']
                fotografiaFachada = imagen.read()
               
            #Crear un objeto de de la clase puntoInteres
            miPuntoInteres=puntoInteres(nombre, latitud, longitud, nomenclatura, numeroObrasVenta, horario, fotografiaFachada)
            
            #Guardar el objeto en la base de datos
            db.session.add(miPuntoInteres)
            db.session.commit()
          
            return redirect(url_for('visorGeografico'))
            
            
            
            
        return render_template('nuevoPuntoInteres.html')



miPrograma=Programa()