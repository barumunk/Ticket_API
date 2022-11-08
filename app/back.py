import pymongo
import json
from flask import Flask,session,render_template,request,redirect,url_for,jsonify
import os

# conexion a la base de datos
class CONEXION:
    def Conexion(self):
        client = pymongo.MongoClient("mongodb://root:root123@mongo_DB:27017/")
        db     = client["ticket"]
        #coleccion = db['registro']
        print("Nombre de la DB: ",db.name)
        return db
        


app = Flask(__name__)
app.secret_key = os.urandom(24)


#Se hace un llamado a la funcion del render_template
def ren_temp(url,dato,usuario):
    #retorna una redireccion html.
    return render_template(url,diccionario=dato,usuario=usuario)


# inicio de sesión
@app.route('/', methods=['GET','POST'])
def index():

    if request.method == 'POST':# recibe una petición post
        # verificamos que las credenciales sean correctas
        if request.form['usuario'] == "admin":
            if request.form['contrasena'] == "admin123":
                session['admin'] = request.form['usuario']
                # retornamos una redireción a una url 
                return redirect(url_for('admin')) 
    elif "admin" in session:
        log = session['admin']
        if log != None:
            return redirect(url_for('admin'))

    # retornamos una redireción html 
    return render_template('index.html')



################# ADMINISTRADOR DE LA BASE DE DATOS #################
# muesta toda la colección
@app.route('/admin')
def admin():
    return ren_temp('admin.html',user(),session['admin'])

# muesta toda la colección
@app.route('/admin/cerrar')
def cerrar():
    session.pop('admin', None)
    return render_template('index.html')


################# BORRAR REGISTRO DE LA BASE DE DATOS #################
# muesta toda la colección
@app.route('/admin/borrar/<id>', methods=['GET','POST'])
def borrar_datos(id):
    conexion = CONEXION()
    db       = conexion.Conexion()
    turno    = db['turno']

    db.turno.delete_one({'id_turno':str(id)})

    return ren_temp('admin.html',user(),session['admin'])



################# REGISTROS DE LA BASE DE DATOS #################
@app.route('/user/ticket',methods=['GET','POST'])
def ticket():
    conexion       = CONEXION()
    db             = conexion.Conexion()
    municipios     = db['municipio']
    niveles        = db['nivel']
    asuntos        = db['asunto']
    listaMunicipio = []
    listaNivel     = []
    listaAsunto    = []

    for municipio in municipios.find():
        municipio['_id'] = str(municipio['_id'])
        listaMunicipio.append(municipio)
    
    for nivel in niveles.find():
        nivel['_id'] = str(nivel['_id'])
        listaNivel.append(nivel)
    
    for asunto in asuntos.find():
        asunto['_id'] = str(asunto['_id'])
        listaAsunto.append(asunto)

    return render_template('ticket.html',muni=listaMunicipio,nive=listaNivel,asun=listaAsunto)


@app.route('/user/ticket/registro',methods=['GET','POST'])
def registro():
    if request.method == 'POST':# recibe una petición post
        conexion       = CONEXION()
        db             = conexion.Conexion()
        turnos         = db['turno']
        aux            = 0
        registro_turno = {}

        if turnos != None:
            for turno in turnos.find():
                if request.form['f_muni'] == turno['municipio']:
                    aux += 1

            if aux != 0:
                registro_turno = {
                    "id_turno"  :str(aux+1),
                    "nombrecomp":request.form['f_namecom'],
                    "curp"      :request.form['f_curp'],
                    "nombre"    :request.form['f_name'],
                    "paterno"   :request.form['f_pate'],
                    "materno"   :request.form['f_mate'],
                    "telefono"  :request.form['f_tele'],
                    "celular"   :request.form['f_celu'],
                    "correo"    :request.form['f_corr'],
                    "nivel"     :request.form['f_nive'],
                    "municipio" :request.form['f_muni'],
                    "asunto"    :request.form['f_uni']
                }
            else:
                registro_turno = {
                    "id_turno"  :"1",
                    "nombrecomp":request.form['f_namecom'],
                    "curp"      :request.form['f_curp'],
                    "nombre"    :request.form['f_name'],
                    "paterno"   :request.form['f_pate'],
                    "materno"   :request.form['f_mate'],
                    "telefono"  :request.form['f_tele'],
                    "celular"   :request.form['f_celu'],
                    "correo"    :request.form['f_corr'],
                    "nivel"     :request.form['f_nive'],
                    "municipio" :request.form['f_muni'],
                    "asunto"    :request.form['f_uni']
                }
            db.turno.insert_many([registro_turno])

    return ren_temp('user.html',user(),"USUARIO")


@app.route('/admin/ticket',methods=['GET','POST'])
def ticket_admin():
    conexion       = CONEXION()
    db             = conexion.Conexion()
    municipios     = db['municipio']
    niveles        = db['nivel']
    asuntos        = db['asunto']
    listaMunicipio = []
    listaNivel     = []
    listaAsunto    = []

    for municipio in municipios.find():
        municipio['_id'] = str(municipio['_id'])
        listaMunicipio.append(municipio)
    
    for nivel in niveles.find():
        nivel['_id'] = str(nivel['_id'])
        listaNivel.append(nivel)
    
    for asunto in asuntos.find():
        asunto['_id'] = str(asunto['_id'])
        listaAsunto.append(asunto)

    return render_template('ticket_admin.html',muni=listaMunicipio,nive=listaNivel,asun=listaAsunto)


@app.route('/admin/ticket/registro',methods=['GET','POST'])
def registro_admin():
    if request.method == 'POST':# recibe una petición post
        conexion       = CONEXION()
        db             = conexion.Conexion()
        turnos         = db['turno']
        aux            = 0
        registro_turno = {}

        if turnos != None:
            for turno in turnos.find():
                if request.form['f_muni'] == turno['municipio']:
                    aux += 1

            if aux != 0:
                registro_turno = {
                    "id_turno"  :str(aux+1),
                    "nombrecomp":request.form['f_namecom'],
                    "curp"      :request.form['f_curp'],
                    "nombre"    :request.form['f_name'],
                    "paterno"   :request.form['f_pate'],
                    "materno"   :request.form['f_mate'],
                    "telefono"  :request.form['f_tele'],
                    "celular"   :request.form['f_celu'],
                    "correo"    :request.form['f_corr'],
                    "nivel"     :request.form['f_nive'],
                    "municipio" :request.form['f_muni'],
                    "asunto"    :request.form['f_uni']
                }
            else:
                registro_turno = {
                    "id_turno"  :"1",
                    "nombrecomp":request.form['f_namecom'],
                    "curp"      :request.form['f_curp'],
                    "nombre"    :request.form['f_name'],
                    "paterno"   :request.form['f_pate'],
                    "materno"   :request.form['f_mate'],
                    "telefono"  :request.form['f_tele'],
                    "celular"   :request.form['f_celu'],
                    "correo"    :request.form['f_corr'],
                    "nivel"     :request.form['f_nive'],
                    "municipio" :request.form['f_muni'],
                    "asunto"    :request.form['f_uni']
                }
            db.turno.insert_many([registro_turno])

    return ren_temp('admin.html',user(),"USUARIO")


################# LECTURA DE LA BASE DE DATOS #################
# muesta toda la colección
@app.route('/user')
def user():
    return ren_temp('user.html',user(),"USUARIOS")

#Funcion que ejecuta el trabajo mostrar ticket
def user():
    conexion  = CONEXION()
    db        = conexion.Conexion()
    coleccion = db['turno']
    lista     = []
    # nos agrega a la lista de todo los registros 
    for col in coleccion.find():
        col['_id'] = str(col['_id'])
        lista.append(col)
    # retornamos una redireción html  le pasamos parametros de la lista y nombre de usuario
    return lista
    


################# ACTUALIZAR LA BASE DE DATOS #################
# muesta toda la colección
@app.route('/user/validar/<municipio>', methods=['GET','POST'])
def validar(municipio):
        
    # retornamos una redireción html  le pasamos parametros de la lista y nombre de usuario
    return render_template('validar.html',municipio=municipio,actualizar="VALIDAR")


# muesta toda la colección
@app.route('/user/actualizar',methods=['GET','POST'])
def actualizar():
    if request.method == 'POST':# recibe una petición post
        conexion       = CONEXION()
        db             = conexion.Conexion()
        coleccion      = db['turno']
        municipios     = db['municipio']
        niveles        = db['nivel']
        asuntos        = db['asunto']
        listaMunicipio = []
        listaNivel     = []
        listaAsunto    = []
        lista          = []

        # nos agrega a la lista de todo los registros 
        for col in coleccion.find():
            if col['id_turno'] == str(request.form['turno']) and col['municipio'] == request.form['municipio']:
                col['_id'] = str(col['_id'])
                lista.append(col)

        for municipio in municipios.find():
            municipio['_id'] = str(municipio['_id'])
            listaMunicipio.append(municipio)

        for nivel in niveles.find():
            nivel['_id'] = str(nivel['_id'])
            listaNivel.append(nivel)

        for asunto in asuntos.find():
            asunto['_id'] = str(asunto['_id'])
            listaAsunto.append(asunto)

        if str(request.form['turno']) == lista[0]['id_turno'] and request.form['curp'] == lista[0]['curp']:
            return render_template('actualizar.html', listas=lista, muni=listaMunicipio, nive=listaNivel, asun=listaAsunto,actualizar="ACTUALIZAR")

    # retornamos una redireción html  le pasamos parametros de la lista y nombre de usuario
    #return render_template('validar.html', listas=lista, muni=listaMunicipio, nive=listaNivel, asun=listaAsunto, curp=curp, id=id,actualizar="ACTUALIZAR")
    return render_template('validar.html',municipio=request.form['municipio'],actualizar="ACTUALIZAR")


# muesta toda la colección
@app.route('/user/actualizar/datos',methods=['GET','POST'])
def actualizar_datos():
    if request.method == 'POST':# recibe una petición post
        conexion  = CONEXION()
        db        = conexion.Conexion()
        turno     = db['turno']
        myquery   = { "id_turno":str(request.form['id_turno'])}
        newvalues = { "$set": { 
            "nombrecomp":request.form['f_namecom'],
            "curp"      :request.form['f_curp'],
            "nombre"    :request.form['f_name'],
            "paterno"   :request.form['f_pate'],
            "materno"   :request.form['f_mate'],
            "telefono"  :request.form['f_tele'],
            "celular"   :request.form['f_celu'],
            "correo"    :request.form['f_corr'],
            "nivel"     :request.form['f_nive'],
            "municipio" :request.form['f_muni'],
            "asunto"    :request.form['f_uni']
            } 
        }

        db.turno.update_one(myquery, newvalues)
    return ren_temp('user.html',user(),"USUARIOS")


# muesta toda la colección
@app.route('/admin/validar/<municipio>', methods=['GET','POST'])
def validar_admin(municipio):
        
    # retornamos una redireción html  le pasamos parametros de la lista y nombre de usuario
    return render_template('validar_admin.html',municipio=municipio,actualizar="VALIDAR")


# muesta toda la colección
@app.route('/admin/actualizar',methods=['GET','POST'])
def actualizar_admin():
    if request.method == 'POST':# recibe una petición post
        conexion       = CONEXION()
        db             = conexion.Conexion()
        coleccion      = db['turno']
        municipios     = db['municipio']
        niveles        = db['nivel']
        asuntos        = db['asunto']
        listaMunicipio = []
        listaNivel     = []
        listaAsunto    = []
        lista          = []

        # nos agrega a la lista de todo los registros 
        for col in coleccion.find():
            if col['id_turno'] == str(request.form['turno']) and col['municipio'] == request.form['municipio']:
                col['_id'] = str(col['_id'])
                lista.append(col)

        for municipio in municipios.find():
            municipio['_id'] = str(municipio['_id'])
            listaMunicipio.append(municipio)

        for nivel in niveles.find():
            nivel['_id'] = str(nivel['_id'])
            listaNivel.append(nivel)

        for asunto in asuntos.find():
            asunto['_id'] = str(asunto['_id'])
            listaAsunto.append(asunto)

        if str(request.form['turno']) == lista[0]['id_turno'] and request.form['curp'] == lista[0]['curp']:
            return render_template('actualizar_admin.html', listas=lista, muni=listaMunicipio, nive=listaNivel, asun=listaAsunto,actualizar="ACTUALIZAR")

    # retornamos una redireción html  le pasamos parametros de la lista y nombre de usuario
    #return render_template('validar.html', listas=lista, muni=listaMunicipio, nive=listaNivel, asun=listaAsunto, curp=curp, id=id,actualizar="ACTUALIZAR")
    return render_template('validar_admin.html',municipio=request.form['municipio'],actualizar="ACTUALIZAR")


# muesta toda la colección
@app.route('/admin/actualizar/datos',methods=['GET','POST'])
def actualizar_datos_admin():
    if request.method == 'POST':# recibe una petición post
        conexion  = CONEXION()
        db        = conexion.Conexion()
        turno     = db['turno']
        myquery   = { "id_turno":str(request.form['id_turno'])}
        newvalues = { "$set": { 
            "nombrecomp":request.form['f_namecom'],
            "curp"      :request.form['f_curp'],
            "nombre"    :request.form['f_name'],
            "paterno"   :request.form['f_pate'],
            "materno"   :request.form['f_mate'],
            "telefono"  :request.form['f_tele'],
            "celular"   :request.form['f_celu'],
            "correo"    :request.form['f_corr'],
            "nivel"     :request.form['f_nive'],
            "municipio" :request.form['f_muni'],
            "asunto"    :request.form['f_uni']
            } 
        }

        db.turno.update_one(myquery, newvalues)
    return ren_temp('admin.html',user(),"USUARIOS")


#charmeleon  charizard
def main():
    app.run(debug=True,host="0.0.0.0")

if __name__=="__main__":
    main()
