from db import db

#Crear un modelo de datos que tenga los siguientes campos nombre(string), latitud(Grados sexagesimales, GRADOS MINUTOS Y SEGUNDOS, que se conviertan a decimal), longitud(Grados sexagesimales, GRADOS MINUTOS Y SEGUNDOS, que se conviertan a decimal), nomenclatura(string), numeroObrasVenta(int positivo), horario(string), fotografíaFachada(archivo de tipo imagen)
class puntoInteres(db.Model):
    __tablename__='puntoInteres'
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(80))
    latitud=db.Column(db.Float(precision=10))
    longitud=db.Column(db.Float(precision=10))
    nomenclatura=db.Column(db.String(80))
    numeroObrasVenta=db.Column(db.Integer)
    horario=db.Column(db.String(80))
    telefono=db.Column(db.String(80))
    fotografiaFachada=db.Column(db.String(80))

    def __init__(self, nombre, latitud, longitud, nomenclatura, numeroObrasVenta, horario, telefono, fotografiaFachada):
        self.nombre=nombre
        self.latitud=latitud
        self.longitud=longitud
        self.nomenclatura=nomenclatura
        self.numeroObrasVenta=numeroObrasVenta
        self.horario=horario
        self.telefono=telefono
        self.fotografiaFachada=fotografiaFachada