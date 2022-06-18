# 0. ejecutamos pip install flask flask-sqlalchemy flask-migrate flask-cors
# 1. Crear modelos
# 2. importamos las librerias de flask

from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Cliente, Venta, Vendedor, Comuna, Region, Despacho, Detalle, Donacion, Suscripcion, Producto, Descuento, Descuento_Producto
from flask_cors import CORS, cross_origin

# 3. instanciamos la app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Conten-Type'
app.url_map.strict_slashes = False
app.config['DEBUG'] = False
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

Migrate(app, db)

# 5. Creamos la ruta por defecto para saber si mi app esta funcionado
# 6. ejecutamos el comando en la consola: python app.py o python3 app.py y revisamos nuestro navegador
@app.route('/')
def index():
    return 'Hola desde gitpod'



#1RUTAS CLIENTE****************************************************************************************************************************

#A-Ruta para consultar todos los Clientes
@app.route('/clientes', methods=['GET'])
def getClientes():
    user = Cliente.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200

#B-Ruta para agregar Cliente
@app.route('/clientes', methods=['POST'])
def addClientes():
    user = Cliente()

    # asignar a variables lo que recibo mediante post  
    user.rut = request.json.get('rut')
    user.dv = request.json.get('dv')
    user.primer_nombre = request.json.get('primer_nombre')
    user.segundo_nombre = request.json.get('segundo_nombre')
    user.apellido_paterno = request.json.get('apellido_paterno')
    user.apellido_materno = request.json.get('apellido_materno')
    user.direccion = request.json.get('direccion')
    user.fono = request.json.get('fono')
    user.correo = request.json.get('correo')
    user.estado = request.json.get('estado')
    user.comuna_id  = request.json.get('comuna_id ')
    
    Cliente.save(user)

    return jsonify(user.serialize()),200

#C-Creamos metodo para consultar una Cliente en especifico
@app.route('/clientes/<id_cliente>', methods=['GET'])
def getCliente(id_cliente):
    user = Cliente.query.get(id_cliente)
    return jsonify(user.serialize()),200

#D.Borrar Cliente
@app.route('/clientes/<id_cliente>', methods=['DELETE'])
def deleteCliente(id_cliente):
    user = Cliente.query.get(id_cliente)
    Cliente.delete(user)
    return jsonify(user.serialize()),200

#E.Modificar Cliente
@app.route('/clientes/<id_cliente>', methods=['PUT'])
def updateCliente(id_cliente):
    user = Cliente.query.get(id_cliente)

    user.rut = request.json.get('rut')
    user.dv = request.json.get('dv')
    user.primer_nombre = request.json.get('primer_nombre')
    user.segundo_nombre = request.json.get('segundo_nombre')
    user.apellido_paterno = request.json.get('apellido_paterno')
    user.apellido_materno = request.json.get('apellido_materno')
    user.direccion = request.json.get('direccion')
    user.fono = request.json.get('fono')
    user.correo = request.json.get('correo')
    user.estado = request.json.get('estado')
    user.comuna_id  = request.json.get('comuna_id ')
    
   
    Cliente.save(user)

    return jsonify(user.serialize()),200

#2-VENTA***************************************************************************************************************************************
#A-Ruta para consultar todas las VENTAS
@app.route('/ventas', methods=['GET'])
def getVentas():
    user = Venta.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200

#B-Ruta para agregar VENTAS
@app.route('/ventas', methods=['POST'])
def addVentas():
    user = Venta()
    # asignar a variables lo que recibo mediante post

    user.fecha = request.json.get('fecha')
    user.descuento = request.json.get('descuento')
    user.sub_total = request.json.get('sub_total')
    user.iva = request.json.get('iva')
    user.total = request.json.get('total')
    user.estado = request.json.get('estado')
    user.cliente_id = request.json.get('cliente_id')
    user.vendedor_id = request.json.get('vendedor_id')
    user.despacho_id = request.json.get('despacho_id')

    Venta.save(user)

    return jsonify(user.serialize()),200

#C-Creamos metodo para consultar una VENTAS en especifico
@app.route('/ventas/<id_venta>', methods=['GET'])
def getVenta(id_venta):
    user = Venta.query.get(id_venta)
    return jsonify(user.serialize()),200
#D.Borrar VENTAS
@app.route('/ventas/<id_venta>', methods=['DELETE'])
def deleteVenta(id_venta):
    user = Venta.query.get(id_venta)
    Venta.delete(user)
    return jsonify(user.serialize()),200
#E.Modificar VENTAS
@app.route('/ventas/<id_venta>', methods=['PUT'])
def updateVenta(id_venta):
    user = Venta.query.get(id_venta)

    user.fecha = request.json.get('fecha')
    user.descuento = request.json.get('descuento')
    user.sub_total = request.json.get('sub_total')
    user.iva = request.json.get('iva')
    user.total = request.json.get('total')
    user.estado = request.json.get('estado')
    user.cliente_id = request.json.get('cliente_id')
    user.vendedor_id = request.json.get('vendedor_id')
    user.despacho_id = request.json.get('despacho_id')

    Venta.save(user)

    return jsonify(user.serialize()),200


#3-VENDEDOR***************************************************************************************************************************************
#A-Ruta para consultar todos los VENDEDOR
@app.route('/vendedores', methods=['GET'])
def getVendedores():
    user = Vendedor.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200
#B-Ruta para agregar VENDEDOR
@app.route('/vendedores', methods=['POST'])
def addVendedores():
    user = Vendedor()
    # asignar a variables lo que recibo mediante post

    user.rut = request.json.get('rut')
    user.dv = request.json.get('dv')
    user.primer_nombre = request.json.get('primer_nombre')
    user.segundo_nombre = request.json.get('segundo_nombre')
    user.apellido_paterno = request.json.get('apellido_paterno')
    user.apellido_materno = request.json.get('apellido_materno')
    user.direccion = request.json.get('direccion')
    user.fono = request.json.get('fono')
    user.correo = request.json.get('correo')
    user.estado = request.json.get('estado')
    user.comuna_id  = request.json.get('comuna_id ')
    
    Vendedor.save(user)

    return jsonify(user.serialize()),200
#C-Creamos metodo para consultar una VENDEDOR en especifico
@app.route('/vendedores/<id_vendedor>', methods=['GET'])
def getVendedor(id_vendedor):
    user = Vendedor.query.get(id_vendedor)
    return jsonify(user.serialize()),200
#D.Borrar VENDEDOR
@app.route('/vendedores/<id_vendedor>', methods=['DELETE'])
def deleteVendedor(id_vendedor):
    user = Vendedor.query.get(id_vendedor)
    Vendedor.delete(user)
    return jsonify(user.serialize()),200
#E.Modificar VENDEDOR
@app.route('/vendedores/<id_vendedor>', methods=['PUT'])
def updateVendedor(id_vendedor):
    user = Vendedor.query.get(id_vendedor)

    user.rut = request.json.get('rut')
    user.dv = request.json.get('dv')
    user.primer_nombre = request.json.get('primer_nombre')
    user.segundo_nombre = request.json.get('segundo_nombre')
    user.apellido_paterno = request.json.get('apellido_paterno')
    user.apellido_materno = request.json.get('apellido_materno')
    user.direccion = request.json.get('direccion')
    user.fono = request.json.get('fono')
    user.correo = request.json.get('correo')
    user.estado = request.json.get('estado')
    user.comuna_id  = request.json.get('comuna_id ')
    
   
    Vendedor.save(user)

    return jsonify(user.serialize()),200

#4-COMUNA***************************************************************************************************************************************
#A-Ruta para consultar todas las Comunas 
@app.route('/comunas', methods=['GET'])
def getComunas():
    user = Comuna.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200
#B-Ruta para agregar Comuna
@app.route('/comunas', methods=['POST'])
def addComuna():
    user = Comuna()
    # asignar a variables lo que recibo mediante post
    user.nombre = request.json.get('nombre')
    
    Comuna.save(user)

    return jsonify(user.serialize()),200
#C-Creamos metodo para consultar una Cliente en especifico
@app.route('/comunas/<id_comuna>', methods=['GET'])
def getComuna(id_comuna):
    user = Comuna.query.get(id_comuna)
    return jsonify(user.serialize()),200
#D.Borrar Cliente
@app.route('/comunas/<id_comuna>', methods=['DELETE'])
def deleteComuna(id_comuna):
    user = Comuna.query.get(id_comuna)
    Comuna.delete(user)
    return jsonify(user.serialize()),200
#E.Modificar Cliente
@app.route('/comunas/<id_comuna>', methods=['PUT'])
def updateComuna(id_comuna):
    user = Comuna.query.get(id_comuna)

    user.nombre = request.json.get('nombre')
    
    Comuna.save(user)

    return jsonify(user.serialize()),200

#5-REGION***************************************************************************************************************************************
#A-Ruta para consultar todas las Regiones
@app.route('/regiones', methods=['GET'])
def getUsuarios():
    user = Region.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200
#B-Ruta para agregar REGION
@app.route('/regiones', methods=['POST'])
def addRegion():
    user = Region()
    # asignar a variables lo que recibo mediante post
    user.nombre = request.json.get('nombre')
   

    Region.save(user)

    return jsonify(user.serialize()),200
#C-Creamos metodo para consultar una REGION en especifico
@app.route('/regiones/<id_region>', methods=['GET'])
def getRegion(id_region):
    user = Region.query.get(id_region)
    return jsonify(user.serialize()),200

#D.Borrar REGION
@app.route('/regiones/<id_region>', methods=['DELETE'])
def deleteRegion(id_region):
    user = Region.query.get(id_region)
    Region.delete(user)
    return jsonify(user.serialize()),200
#E.Modificar REGION
@app.route('/regiones/<id_region>', methods=['PUT'])
def updateRegion(id_region):
    user = Region.query.get(id_region)

    user.nombre = request.json.get('nombre')
    
    Region.save(user)

    return jsonify(user.serialize()),200

#6-DESPACHO***************************************************************************************************************************************
#A-Ruta para consultar todos los DESPACHOS
@app.route('/despachos', methods=['GET'])
def getDespachos():
    user = Despacho.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200
#B-Ruta para agregar DESPACHO
@app.route('/despachos', methods=['POST'])
def addDespachos():
    user = Despacho()
    # asignar a variables lo que recibo mediante post

    user.direccion = request.json.get('direccion')
    user.fecha_entrega = request.json.get('fecha_entrega')
    user.hora_entrega = request.json.get('hora_entrega')
    user.rut_recibe = request.json.get('rut_recibe')
    user.nombre_recibe = request.json.get('nombre_recibe')
    user.esto_despacho = request.json.get('esto_despacho')
    user.venta_id = request.json.get('venta_id')
    user.comuna_id = request.json.get('comuna_id')
    
    Despacho.save(user)

    return jsonify(user.serialize()),200
#C-Creamos metodo para consultar un DESPACHO en especifico
@app.route('/despachos/<id_despacho>', methods=['GET'])
def getDespacho(id_despacho):
    user = Despacho.query.get(id_despacho)
    return jsonify(user.serialize()),200

#D.Borrar DESPACHO
@app.route('/despachos/<id_despacho>', methods=['DELETE'])
def deleteDespacho(id_despacho):
    user = Despacho.query.get(id_despacho)
    Despacho.delete(user)
    return jsonify(user.serialize()),200
#E.Modificar DESPACHO
@app.route('/despachos/<id_despacho>', methods=['PUT'])
def updateDespacho(id_despacho):
    user = Despacho.query.get(id_despacho)

    user.direccion = request.json.get('direccion')
    user.fecha_entrega = request.json.get('fecha_entrega')
    user.hora_entrega = request.json.get('hora_entrega')
    user.rut_recibe = request.json.get('rut_recibe')
    user.nombre_recibe = request.json.get('nombre_recibe')
    user.esto_despacho = request.json.get('esto_despacho')
    user.venta_id = request.json.get('venta_id')
    user.comuna_id = request.json.get('comuna_id')
       
    Despacho.save(user)

    return jsonify(user.serialize()),200
#7-DETALLE***************************************************************************************************************************************
#A-Ruta para consultar todos los Detalles
@app.route('/detalles', methods=['GET'])
def getDetalles():
    user = Detalle.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200

#B-Ruta para agregar DETALLES
@app.route('/detalles', methods=['POST'])
def addDetalles():
    user = Detalle()
    # asignar a variables lo que recibo mediante post

    user.cantidad = request.json.get('cantidad')
    user.valor = request.json.get('valor')
    user.descuento = request.json.get('descuento')
    user.estado = request.json.get('estado')
    user.venta_id = request.json.get('venta_id')
    user.producto_id = request.json.get('producto_id')
        
    Detalle.save(user)

    return jsonify(user.serialize()),200
#C-Creamos metodo para consultar una DETALLES en especifico
@app.route('/detalles/<id_detalle>', methods=['GET'])
def getDetalle(id_detalle):
    user = Detalle.query.get(id_detalle)
    return jsonify(user.serialize()),200
#D.Borrar DETALLES
@app.route('/detalles/<id_detalle>', methods=['DELETE'])
def deleteDetalle(id_detalle):
    user = Detalle.query.get(id_detalle)
    Detalle.delete(user)
    return jsonify(user.serialize()),200
#E.Modificar DETALLES
@app.route('/detalles/<id_detalle>', methods=['PUT'])
def updateDetalle(id_detalle):
    user = Detalle.query.get(id_detalle)

    user.cantidad = request.json.get('cantidad')
    user.valor = request.json.get('valor')
    user.descuento = request.json.get('descuento')
    user.estado = request.json.get('estado')
    user.venta_id = request.json.get('venta_id')
    user.producto_id = request.json.get('producto_id')
           
    Detalle.save(user)

    return jsonify(user.serialize()),200

#8-DONACION***************************************************************************************************************************************
#A-Ruta para consultar todas los DONACIONES
@app.route('/donaciones', methods=['GET'])
def getDonaciones():
    user = Donacion.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200
#B-Ruta para agregar DONACION
@app.route('/donaciones', methods=['POST'])
def addDonaciones():
    user = Donacion()
    # asignar a variables lo que recibo mediante post

    user.valor = request.json.get('valor')
    user.fecha = request.json.get('fecha')
    user.cliente_id = request.json.get('cliente_id')

    Donacion.save(user)

    return jsonify(user.serialize()),200

#C-Creamos metodo para consultar una DONACION en especifico
@app.route('/donaciones/<id_donacion>', methods=['GET'])
def getDonacion(id_donacion):
    user = Donacion.query.get(id_donacion)
    return jsonify(user.serialize()),200
#D.Borrar DONACION
@app.route('/donaciones/<id_donacion>', methods=['DELETE'])
def deleteDonacion(id_donacion):
    user = Donacion.query.get(id_donacion)
    Donacion.delete(user)
    return jsonify(user.serialize()),200
#E.Modificar DONACION
@app.route('/donaciones/<id_donacion>', methods=['PUT'])
def updateDonacion(id_donacion):
    user = Donacion.query.get(id_donacion)

    user.valor = request.json.get('valor')
    user.fecha = request.json.get('fecha')
    user.cliente_id = request.json.get('cliente_id')
   
    Donacion.save(user)

    return jsonify(user.serialize()),200


#9-SUSCRIPCION***************************************************************************************************************************************
#A-Ruta para consultar todas las SUSCRIPCIONES
@app.route('/suscripciones', methods=['GET'])
def getSuscripciones():
    user = Suscripcion.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200
#B-Ruta para agregar SUSCRIPCIONES
@app.route('/suscripciones', methods=['POST'])
def addSuscripciones():
    user = Suscripcion()
    # asignar a variables lo que recibo mediante post

    user.valor = request.json.get('valor')
    user.fecha = request.json.get('fecha')
    user.cliente_id = request.json.get('cliente_id')

    Suscripcion.save(user)

    return jsonify(user.serialize()),200
#C-Creamos metodo para consultar una SUSCRIPCIONES en especifico
@app.route('/suscripciones/<id>', methods=['GET'])
def getSuscripcion(id_suscripcion):
    user = Suscripcion.query.get(id_suscripcion)
    return jsonify(user.serialize()),200
#D.Borrar SUSCRIPCIONES
@app.route('/suscripciones/<id>', methods=['DELETE'])
def deleteSuscripcion(id_suscripcion):
    user = Suscripcion.query.get(id_suscripcion)
    Suscripcion.delete(user)
    return jsonify(user.serialize()),200
#E.Modificar SUSCRIPCIONES
@app.route('/suscripciones/<id>', methods=['PUT'])
def updateSuscripcion(id_suscripcion):
    user = Suscripcion.query.get(id_suscripcion)

    user.valor = request.json.get('valor')
    user.fecha = request.json.get('fecha')
    user.cliente_id = request.json.get('cliente_id')
   
    Suscripcion.save(user)

    return jsonify(user.serialize()),200
#10-PRODUCTO***************************************************************************************************************************************
#A-Ruta para consultar todos los PRODUCTOS
@app.route('/productos', methods=['GET'])
def getProductos():
    user = Producto.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200
#B-Ruta para agregar PRODUCTO
@app.route('/productos', methods=['POST'])
def addProducto():
    user = Producto()
    # asignar a variables lo que recibo mediante post

    user.codigo = request.json.get('codigo')
    user.nombre = request.json.get('nombre')
    user.valor_venta = request.json.get('valor_venta')
    user.stock = request.json.get('stock')
    user.descripcion = request.json.get('descripcion')
    user.imagen = request.json.get('imagen')
    user.estado = request.json.get('estado')

    Producto.save(user)
    return jsonify(user.serialize()),200

#C-Creamos metodo para consultar un PRODUCTO en especifico
@app.route('/productos/<id>', methods=['GET'])
def getProducto(id_producto):
    user = Producto.query.get(id_producto)
    return jsonify(user.serialize()),200

#D.Borrar PRODUCTO
@app.route('/productos/<id>', methods=['DELETE'])
def deleteProducto(id_producto):
    user = Producto.query.get(id_producto)
    Producto.delete(user)
    return jsonify(user.serialize()),200
#E.Modificar PRODUCTO
@app.route('/productos/<id>', methods=['PUT'])
def updateProducto(id_producto):
    user = Producto.query.get(id_producto)

    user.codigo = request.json.get('codigo')
    user.nombre = request.json.get('nombre')
    user.valor_venta = request.json.get('valor_venta')
    user.stock = request.json.get('stock')
    user.descripcion = request.json.get('descripcion')
    user.imagen = request.json.get('imagen')
    user.estado = request.json.get('estado')

    Producto.save(user)

    return jsonify(user.serialize()),200


#11-DESCUENTO***************************************************************************************************************************************
#A-Ruta para consultar todos los DESCUENTOS
@app.route('/descuentos', methods=['GET'])
def getDescuentos():
    user = Descuento.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200
#B-Ruta para agregar DESCUENTOS
@app.route('/descuentos', methods=['POST'])
def addDescuento():
    user = Descuento()
    # asignar a variables lo que recibo mediante post
    user.nombre = request.json.get('nombre')
    user.fecha = request.json.get('fecha')
    user.porcentaje = request.json.get('porcentaje')
    user.estado = request.json.get('estado')
    
    Descuento.save(user)

    return jsonify(user.serialize()),200
#C-Creamos metodo para consultar un DESCUENTO en especifico
@app.route('/descuentos/<id>', methods=['GET'])
def getDescuento(id_descuento):
    user = Descuento.query.get(id_descuento)
    return jsonify(user.serialize()),200

#D.Borrar DESCUENTOS
@app.route('/descuentos/<id>', methods=['DELETE'])
def deleteDescuento(id_descuento):
    user = Descuento.query.get(id_descuento)
    Descuento.delete(user)
    return jsonify(user.serialize()),200

#E.Modificar DESCUENTOS
@app.route('/descuentos/<id>', methods=['PUT'])
def updateDescuento(id_descuento):
    user = Descuento.query.get(id_descuento)

    user.nombre = request.json.get('nombre')
    user.fecha = request.json.get('fecha')
    user.porcentaje = request.json.get('porcentaje')
    user.estado = request.json.get('estado')

    Descuento.save(user)

    return jsonify(user.serialize()),200


#12-DESCUENTO PRODUCTO***************************************************************************************************************************************
#A-Ruta para consultar todos los DESCUENTOS PRODUCTOS
@app.route('/descuento_productos', methods=['GET'])
def getDescuento_Productos():
    user = Descuento_Producto.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user),200
#B-Ruta para agregar DESCUENTO PRODUCTO
@app.route('/descuento_productos', methods=['POST'])
def addDescuento_Productos():
    user = Descuento_Producto()
    # asignar a variables lo que recibo mediante post

    user.fecha_inicio = request.json.get('fecha_inicio')
    user.fecha_termino = request.json.get('fecha_termino')
    
    Descuento_Producto.save(user)

    return jsonify(user.serialize()),200
#C-Creamos metodo para consultar un DESCUENTO PRODUCTO en especifico
@app.route('/descuento_productos/<id>', methods=['GET'])
def getDescuento_Producto(id):
    user = Descuento_Producto.query.get(id)
    return jsonify(user.serialize()),200
#D.Borrar DESCUENTO PRODUCTO
@app.route('/descuento_productos/<id>', methods=['DELETE'])
def deleteDescuento_Producto(id):
    user = Descuento_Producto.query.get(id)
    Descuento_Producto.delete(user)
    return jsonify(user.serialize()),200

#E.Modificar DESCUENTO PRODUCTO
@app.route('/descuento_productos/<id>', methods=['PUT'])
def updateDescuento_Producto(id):
    user = Descuento_Producto.query.get(id)

    user.fecha_inicio = request.json.get('fecha_inicio')
    user.fecha_termino = request.json.get('fecha_termino')
    
    Descuento_Producto.save(user)

    return jsonify(user.serialize()),200

#PUERTO
if __name__ == '__main__':
    app.run(port=5000, debug=True)