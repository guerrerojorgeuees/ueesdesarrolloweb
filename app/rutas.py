from flask import Blueprint, jsonify, request, render_template, redirect, url_for, flash, session
from models import Cliente, db  # Asegúrate de importar la clase correcta
from models import Articulo
from models import User

rutas = Blueprint('rutas', __name__, template_folder='app/templates')

def get_logged():
    if not session.get('logged', False):
        logged = False
    else:
        logged = session['logged']
    return logged

@rutas.route('/')
def index():
    return render_template('inicio.html',logged=get_logged())

@rutas.route('/pantalla')
def pantalla():
    return render_template('articulo/lista_articulos.html',logged=get_logged())

@rutas.route('/login')
def login():
    session['logged'] = False
    return render_template('login.html',logged=get_logged())

@rutas.route('/ruta_para_procesar_datos', methods=['POST'])
def procesar_datos():
    # Obtener los datos del cuerpo de la solicitud JSON
    data = request.get_json()
    user = User.query.filter_by(username=data['username'],password=data['password']).all()
    if len(user) > 0:
        session['logged'] = True
        return jsonify({"mensaje": "Login Correcto", "data": user[0].role})
    session['logged'] = False
    return jsonify({"mensaje": "Usuario o Contraseña Incorrecto","data":"F"}) #F si no es correcto




# Cliente Crud


@rutas.route('/cliente')
def mostrar_cliente():
    clientes = Cliente.query.all()
    print(session)
    return render_template('cliente/cliente.html', clientes=clientes,logged=get_logged())

@rutas.route('/add_cliente', methods=['POST'])
def add_cliente():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cedula = request.form['cedula']
        address = request.form['address']
        estado = 'A'
        try:
            new_cliente = Cliente(fullname=fullname, phone=phone, email=email, cedula=cedula, address=address,estado=estado)
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
    return render_template('cliente/cliente_edicion.html', cliente=cliente,logged=get_logged())

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
    cliente.estado = 'I'  # Actualizar el estado a inactivo en lugar de eliminar físicamente
    db.session.commit()
    flash('Cliente marcado como inactivo exitosamente')
    return redirect(url_for('rutas.mostrar_cliente'))



# Articulo Crud

@rutas.route('/articulo')
def mostrar_articulo():
    articulos = Articulo.query.all()
    return render_template('articulo/articulo.html', articulos=articulos,logged=get_logged())
def stock():
    # articulos = Articulo.query.all()
    # return render_template('articulo/articulos.html', articulos=articulos)
    return render_template('articulo/stock.html',logged=get_logged())


@rutas.route('/add_articulo', methods=['POST'])
def add_articulo():
    try:
        if request.method == 'POST':
            # echa_empaque,fecha_vencimiento,lote,descripcion,precio,stock
            codigo = request.form['codigo']
            nombre = request.form['nombre']
            fecha_empaque = request.form['fecha_empaque']
            fecha_vencimiento = request.form['fecha_vencimiento']
            lote = request.form['lote']
            descripcion = request.form['descripcion']
            precio = request.form['precio']
            stock = request.form['stock']
            imagen = request.form['imagen']
            estado = 'A'
            try:
                new_articulo = Articulo(codigo=codigo, nombre=nombre, fecha_empaque=fecha_empaque,
                                        fecha_vencimiento=fecha_vencimiento, lote=lote, descripcion=descripcion,
                                        precio=precio, stock=stock, imagen=imagen,estado=estado)
                db.session.add(new_articulo)
                db.session.commit()
                flash('articulo agregado exitosamente')
                return redirect(url_for('rutas.mostrar_articulo'))
            except Exception as e:
                flash(str(e))
                return redirect(url_for('rutas.mostrar_articulo'))
    except Exception as eF:
        flash(str(eF))



@rutas.route('/editArticulo/<int:id>', methods=['POST', 'GET'])
def get_articulo(id):
    articulo = Articulo.query.get(id)
    return render_template('articulo/articulo_edicion.html', articulo=articulo,logged=get_logged())


@rutas.route('/updateArticulo/<int:id>', methods=['POST'])
def update_articulo(id):
    if request.method == 'POST':
        codigo = request.form['codigo']
        nombre = request.form['nombre']
        fecha_empaque = request.form['fecha_empaque']
        fecha_vencimiento = request.form['fecha_vencimiento']
        lote = request.form['lote']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        stock = request.form['stock']
        imagen = request.form['imagen']

        articulo = Articulo.query.get(id)
        articulo.codigo = codigo
        articulo.nombre = nombre
        articulo.fecha_empaque = fecha_empaque
        articulo.fecha_vencimiento = fecha_vencimiento
        articulo.lote = lote
        articulo.descripcion = descripcion
        articulo.precio = precio
        articulo.stock = stock
        articulo.imagen = imagen

        db.session.commit()
        flash('Articulo actualizado exitosamente')
        return redirect(url_for('rutas.mostrar_articulo'))


@rutas.route('/deleteArticulo/<int:id>', methods=['POST', 'GET'])
def delete_articulo(id):
    articulo = Articulo.query.get(id)
    articulo.estado = 'I'  # Actualizar el estado a inactivo en lugar de eliminar físicamente
    db.session.commit()
    flash('Articulo Eliminado exitosamente')
    return redirect(url_for('rutas.mostrar_articulo'))



# venta Crud


@rutas.route('/venta')
def mostrar_ventas():
    # Obtén la lista de clientes activos para el menú desplegable
    clientes_activos = Cliente.query.filter_by(estado='A').all()
    articulos_activos = Articulo.query.filter_by(estado='A').all()
    return render_template('venta/venta.html', clientes_activos=clientes_activos,articulos_activos=articulos_activos,logged=get_logged())

@rutas.route('/listado_ventas')
def listado_ventas():
    
    return render_template('venta/listado_ventas.html',logged=get_logged())

@rutas.route('/detalle_venta')
def detalle_venta():
    return render_template('venta/detalle_venta.html',logged=get_logged())


@rutas.route('/historial_venta')
def historial_venta():
    return render_template('venta/historial_venta.html',logged=get_logged())