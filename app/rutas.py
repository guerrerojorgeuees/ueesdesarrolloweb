from flask import Blueprint, request, render_template, redirect, url_for, flash
from models import Cliente, db  # Asegúrate de importar la clase correcta
from models import Articulo

rutas = Blueprint('rutas', __name__, template_folder='app/templates')

@rutas.route('/')
def index():
    return render_template('inicio.html')

@rutas.route('/pantalla')
def pantalla():
    return render_template('articulo/lista_articulos.html')


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
    cliente.estado = 'I'  # Actualizar el estado a inactivo en lugar de eliminar físicamente
    db.session.commit()
    flash('Cliente marcado como inactivo exitosamente')
    return redirect(url_for('rutas.mostrar_cliente'))



# Articulo Crud

@rutas.route('/articulo')
def mostrar_articulo():
    articulos = Articulo.query.all()
    return render_template('articulo/articulo.html', articulos=articulos)
def stock():
    # articulos = Articulo.query.all()
    # return render_template('articulo/articulos.html', articulos=articulos)
    return render_template('articulo/stock.html')


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
            try:
                new_articulo = Articulo(codigo=codigo, nombre=nombre, fecha_empaque=fecha_empaque,
                                        fecha_vencimiento=fecha_vencimiento, lote=lote, descripcion=descripcion,
                                        precio=precio, stock=stock, imagen=imagen)
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
    return render_template('articulo/articulo_edicion.html', articulo=articulo)


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
    db.session.delete(articulo)
    db.session.commit()
    flash('Articulo Eliminado exitosamente')
    return redirect(url_for('rutas.mostrar_articulo'))






# Articulo Crud


@rutas.route('/venta')
def mostrar_ventas():
    # Obtén la lista de clientes activos para el menú desplegable
    clientes_activos = Cliente.query.filter_by(estado='A').all()
    
    return render_template('venta/venta.html', clientes_activos=clientes_activos)

@rutas.route('/listado_ventas')
def listado_ventas():
    
    return render_template('venta/listado_ventas.html')

@rutas.route('/detalle_venta')
def detalle_venta():
    return render_template('venta/detalle_venta.html')


@rutas.route('/historial_venta')
def historial_venta():
    return render_template('venta/historial_venta.html')