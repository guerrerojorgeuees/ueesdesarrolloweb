from flask import Flask
from db import db
from rutas import rutas
app = Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/bd_uees'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'uees'  # Cambia esto por una cadena única y segura
# Inicialización de SQLAlchemy
db.init_app(app)

# Resto de tu código (rutas, configuraciones adicionales, etc.)


app.register_blueprint(rutas)

# starting the app
if __name__ == "__main__":
    app.run(port=4000, debug=True)
