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

    def __repr__(self):
        return f'<Uees {self.fullname}>'

