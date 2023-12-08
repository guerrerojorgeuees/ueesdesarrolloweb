# models.py
from db import db

class Cliente(db.Model):
    __tablename__ = 'cliente'
    __table_args__ = {'schema': 'uees'}  # Agrega esta línea para especificar el esquema
    # Resto de la definición del modelo...
    
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(255), nullable=False)
    cedula = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.String(1), nullable=False)

    def __repr__(self):
        return f'<Uees {self.fullname}>'



# Modelo de Articulo
class Articulo(db.Model):
    __tablename__ = 'articulo'
    __table_args__ = {'schema': 'uees'}  # Agrega esta línea para especificar el esquema

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(10), nullable=False)
    nombre = db.Column(db.String(255), nullable=False)
    fecha_empaque = db.Column(db.Date(), nullable=False)
    fecha_vencimiento = db.Column(db.Date(), nullable=False)
    lote = db.Column(db.String(20), nullable=True)
    descripcion = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Numeric(10, 2), nullable=True)
    stock = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Uees {self.nombre}>'
