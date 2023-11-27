from flask import Flask, render_template
from db import db
from puntoInteres import puntoInteres

class Programa:
     
    def __init__(self):
         
         self.app=Flask(__name__)
         self.app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///puntosinteres.sqlite3"
         
         #Agregar la db a nuestra aplicación
         db.init_app(self.app)
         
         self.app.add_url_rule('/nuevo', view_func=self.agregar)
         
         #Iniciar el servidor
         with self.app.app_context():
             db.create_all()
         self.app.run(debug=True)
         
    
    def agregar(self):
        return render_template('nuevoPuntoInteres.html')
    

miPrograma=Programa()
    
    
    
    
    