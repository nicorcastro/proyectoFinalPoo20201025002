from db import db
class puntoInteres(db.Model):
# Clase que representa un punto de interés.
# Atributos:
# - id: Identificador del punto de interés (entero).
# - nombre: Nombre del punto de interés (cadena de caracteres).
# - latitud: Latitud del punto de interés (flotante).
# - longitud: Longitud del punto de interés (flotante).
# - nomenclatura: Nomenclatura del punto de interés (cadena de caracteres).
# - numeroObrasVenta: Número de obras en venta del punto de interés (entero).
# - horario: Horario del punto de interés (cadena de caracteres).
# - telefono: Teléfono del punto de interés (cadena de caracteres).
# - fotografiaFachada: Fotografía de la fachada del punto de interés (cadena de caracteres).
    __tablename__ = 'puntoInteres'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80))
    latitud = db.Column(db.Float(precision=16))
    longitud = db.Column(db.Float(precision=16))
    nomenclatura = db.Column(db.String(80))
    numeroObrasVenta = db.Column(db.Integer)
    horario = db.Column(db.String(80))
    telefono = db.Column(db.String(80))
    fotografiaFachada = db.Column(db.String(80))

#Constructor de la clase puntoInteres.
def __init__(self, nombre, latitud, longitud, nomenclatura, numeroObrasVenta, horario, telefono, fotografiaFachada):
    self.nombre = nombre
    self.latitud = latitud
    self.longitud = longitud
    self.nomenclatura = nomenclatura
    self.numeroObrasVenta = numeroObrasVenta
    self.horario = horario
    self.telefono = telefono
    self.fotografiaFachada = fotografiaFachada
