from flask import Blueprint, request, render_template, redirect, url_for, flash
from models import Cliente, db  # Asegúrate de importar la clase correcta

rutas = Blueprint('rutas', __name__, template_folder='app/templates')

@rutas.route('/')
def index():
    return render_template('inicio.html')

@rutas.route('/login')
def login():
    return render_template('login.html')

@rutas.route('/ruta_para_procesar_datos', methods=['POST'])
def procesar_datos():
    # Obtener los datos del cuerpo de la solicitud JSON
    data = request.get_json()
    return jsonify({"mensaje": "Datos recibidos correctamente", "datos": data})



# Cliente Crud


@rutas.route('/cliente')
def mostrar_cliente():
    clientes = Cliente.query.all()
    return render_template('cliente/cliente.html', clientes=clientes)

@rutas.route('/add_cliente', methods=['POST'])
def add_cliente():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cedula = request.form['cedula']
        address = request.form['address']
        try:
            new_cliente = Cliente(fullname=fullname, phone=phone, email=email, cedula=cedula, address=address)
            db.session.add(new_cliente)
            db.session.commit()
            flash('Cliente agregado exitosamente')
            return redirect(url_for('rutas.mostrar_cliente'))
        except Exception as e:
            flash(str(e))
            return redirect(url_for('rutas.mostrar_cliente'))


@rutas.route('/edit/<int:id>', methods=['POST', 'GET'])
def get_cliente(id):
    cliente = Cliente.query.get(id)
    return render_template('cliente/cliente_edicion.html', cliente=cliente)

@rutas.route('/update/<int:id>', methods=['POST'])
def update_cliente(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cedula = request.form['cedula']
        address = request.form['address']

        cliente = Cliente.query.get(id)
        cliente.fullname = fullname
        cliente.phone = phone
        cliente.email = email
        cliente.cedula = cedula
        cliente.address = address

        db.session.commit()
        flash('Cliente actualizado exitosamente')
        return redirect(url_for('rutas.mostrar_cliente'))

@rutas.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete_cliente(id):
    cliente = Cliente.query.get(id)
    db.session.delete(cliente)
    db.session.commit()
    flash('Cliente Eliminado exitosamente')
    return redirect(url_for('rutas.mostrar_cliente'))



# Articulo Crud


@rutas.route('/articulo')
def mostrar_articulos():
    # articulos = Articulo.query.all()
    # return render_template('articulo/articulos.html', articulos=articulos)
    return render_template('articulo/articulos.html')