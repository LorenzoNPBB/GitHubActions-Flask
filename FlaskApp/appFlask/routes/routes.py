#from appFlask.src.database import database

from appFlask import database as db
from flask import Flask, render_template, request, redirect, url_for, Blueprint

from appFlask.data.alumnos_dao import AlumnDao
from appFlask.data.notas_dao import NotasDao  # PARA PODER ACCEDER A LOS DIRECTORIOS DE UNA MANERA FÁCIL 


app = Blueprint("routes", __name__)

@app.route('/')  # ESTO ES LA RUTA PRINCIPAL DE NUESTRA APP SE PONE CON LA BARRA
def home():
    alumnDao : AlumnDao = AlumnDao(db)
    return render_template('index.html', data=alumnDao.dameTodos())  # PARA QUE SALGA NUESTRO INDEX AL INICIO #DATA=INSERTOBJECT ES PARA QUE NOS SALGA EN NUESTRO HTML


@app.route('/user', methods=['POST'])
def addUser():
    nombre = request.form['Nombre'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL NOMBRE QUE INDIQUEMOS
    apellido = request.form['Apellido'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL password QUE INDIQUEMOS
    centroFormativo = request.form['CentroFormativo'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL NOMBRE QUE INDIQUEMOS
    alumnDao : AlumnDao = AlumnDao(db)
    alumnDao.añadirUsuario(nombre,apellido,centroFormativo)
    return redirect(url_for('routes.home')) # Y REDIRIGIMOS A HOME DE NUEVO. REDIRECT Y URL_FOR LO TENEMOS QUE IMPORTAR DE FLASK



@app.route('/edit/<string:CodigoAlumno>', methods=['POST'])
def edit (CodigoAlumno):
    Nombre = request.form['Nombre'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL NOMBRE DE USUARIO QUE INDIQUEMOs
    Apellido = request.form['Apellido'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL NOMBRE QUE INDIQUEMOS
    CentroFormativo = request.form['CentroFormativo'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL password QUE INDIQUEMOS
    alumnDao : AlumnDao = AlumnDao(db)
    alumnDao.editarUsuario(Nombre,Apellido,CentroFormativo,CodigoAlumno)
    return redirect(url_for('routes.home')) # Y REDIRIGIMOS A HOME DE NUEVO. REDIRECT Y URL_FOR LO TENEMOS QUE IMPORTAR DE FLASK
    


@app.route('/delete/<string:CodigoAlumno>')
def delete(CodigoAlumno):
    alumnDao : AlumnDao = AlumnDao(db)
    alumnDao.borrarUsuario(CodigoAlumno)
    return redirect(url_for('routes.home')) # Y REDIRIGIMOS A HOME DE NUEVO. REDIRECT Y URL_FOR LO TENEMOS QUE IMPORTAR DE FLASK


@app.route('/notas')  # ESTO ES LA RUTA PARA VER LAS NOTAS DE LOS ALUMNOS EN MI APP SE PONE CON LA BARRA
def notas():
    notasDao : NotasDao = NotasDao(db)
    return render_template('notas.html', data=notasDao.dameNotas())  # PARA QUE SALGA NUESTRO INDEX AL INICIO #DATA=INSERTOBJECT ES PARA QUE NOS SALGA EN NUESTRO HTML


@app.route('/userNotas', methods=['POST'])
def addNotas():
    CodigoAlumno = request.form['CodigoAlumno'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL CODIGO ALUMNO QUE INDIQUEMOS
    Seguridad = request.form['Seguridad'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON LA NOTA QUE INDIQUEMOS
    Implantacion = request.form['Implantacion'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON LA NOTA QUE INDIQUEMOS
    Redes = request.form['Redes']
    notasDao : NotasDao = NotasDao(db)
    notasDao.añadeNotas(CodigoAlumno,Seguridad,Implantacion,Redes)
    return redirect(url_for('routes.notas')) # Y REDIRIGIMOS A HOME DE NUEVO. REDIRECT Y URL_FOR LO TENEMOS QUE IMPORTAR DE FLASK


@app.route('/deleteNotas/<string:CodigoAlumno>')
def deleteNotas(CodigoAlumno):
    notasDao : NotasDao = NotasDao(db)
    notasDao.borrarNotas(CodigoAlumno)
    return redirect(url_for('routes.notas')) # Y REDIRIGIMOS A HOME DE NUEVO. REDIRECT Y URL_FOR LO TENEMOS QUE IMPORTAR DE FLASK


@app.route('/editNotas/<string:CodigoAlumno>', methods=['POST'])
def editNotas (CodigoAlumno):
    CodigoAlumno = request.form['CodigoAlumno'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL CodigoAlumno QUE INDIQUEMOS
    Seguridad = request.form['Seguridad'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON LA NOTA DE SEGURIDAD QUE INDIQUEMOS
    Implantacion = request.form['Implantacion'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON CON LA NOTA DE IMPLANTACION QUE INDIQUEMOS
    Redes = request.form['Redes'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON LA NOTA DE REDES QUE INDIQUEMOS
    notasDao: NotasDao = NotasDao(db)
    notasDao.editNotas(Seguridad,Implantacion,Redes,CodigoAlumno)
    return redirect(url_for('routes.notas')) # Y REDIRIGIMOS A HOME DE NUEVO. REDIRECT Y URL_FOR LO TENEMOS QUE IMPORTAR DE FLASK
