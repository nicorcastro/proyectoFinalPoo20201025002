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
    fotografíaFachada=db.Column(db.String(80))
    #relacion con la tabla usuario
    usuario_id=db.Column(db.Integer, db.ForeignKey('usuario.id'))
    usuario=db.relationship('usuarioModel')

    def __init__(self, nombre, latitud, longitud, nomenclatura, numeroObrasVenta, horario, fotografíaFachada, usuario_id):
        self.nombre=nombre
        self.latitud=latitud
        self.longitud=longitud
        self.nomenclatura=nomenclatura
        self.numeroObrasVenta=numeroObrasVenta
        self.horario=horario
        self.fotografíaFachada=fotografíaFachada
        self.usuario_id=usuario_id

    def json(self):
        return {
            'id':self.id,
            'nombre':self.nombre,
            'latitud':self.latitud,
            'longitud':self.longitud,
            'nomenclatura':self.nomenclatura,
            'numeroObrasVenta':self.numeroObrasVenta,
            'horario':self.horario,
            'fotografíaFachada':self.fotografíaFachada,
            'usuario_id':self.usuario_id
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first() #SELECT * FROM puntoInteres WHERE id=id LIMIT 1

    @classmethod
    def find_by_nombre(cls, nombre):
        return cls.query.filter_by(nombre=nombre).first() #SELECT * FROM puntoInteres WHERE nombre=nombre LIMIT 1

    @classmethod
    def find_by_nomenclatura(cls, nomenclatura):
        return cls.query.filter_by(nomenclatura=nomenclatura).first() #SELECT * FROM puntoInteres WHERE nomenclatura=nomenclatura LIMIT 1

    @classmethod
    def find_by_usuario_id(cls, usuario_id):
        return cls.query.filter_by(usuario_id=usuario_id).all()
