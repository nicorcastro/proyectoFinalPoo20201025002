from flask import Flask, render_template, request, redirect, url_for
from db import db
from puntoInteres import puntoInteres
from werkzeug.utils import secure_filename
import os

class Programa:
     #Clase que representa el programa principal de la aplicación.
    def __init__(self):
        #Constructor de la clase Programa.
        #Inicializa la aplicación Flask, configura la base de datos y el directorio de carga de archivos.
        #Agrega las rutas de la aplicación y crea la base de datos si no existe.
        #Inicia el servidor Flask en modo de depuración.
         self.app=Flask(__name__)
         self.app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///puntosinteres.sqlite3"
         self.app.config['UPLOAD_FOLDER'] = 'static'
         
         #Agregar la db a nuestra aplicación
         db.init_app(self.app)
         
         self.app.add_url_rule('/', view_func=self.visorGeografico)
         self.app.add_url_rule('/nuevoPuntoInteres', view_func=self.agregar, methods=["GET", "POST"])
         
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
            telefono=request.form["telefono"]    

            # Obtener el archivo y el nombre del archivo
            fotografia_fachada = request.files['fotografiaFachada']
            nombreArchivo = secure_filename(fotografia_fachada.filename)
            
            # Guardar el archivo en el sistema de archivos (puedes ajustar la ruta según tus necesidades)
            rutaArchivo = os.path.join(self.app.config['UPLOAD_FOLDER'], nombreArchivo)
            fotografia_fachada.save(rutaArchivo)
                
            #Crear un objeto de de la clase puntoInteres
            miPuntoInteres=puntoInteres(
                nombre=nombre, 
                latitud=latitud, 
                longitud=longitud, 
                nomenclatura=nomenclatura, 
                numeroObrasVenta=numeroObrasVenta, 
                horario=horario,
                telefono=telefono, 
                fotografiaFachada=nombreArchivo)
                
            #Guardar el objeto en la base de datos
            db.session.add(miPuntoInteres)
            db.session.commit()
            
            return redirect(url_for('visorGeografico'))

        return render_template('nuevoPuntoInteres.html')

miPrograma = Programa()