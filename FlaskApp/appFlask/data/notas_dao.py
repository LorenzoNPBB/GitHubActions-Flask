from flask import request

#from appFlask.src.database import database

class NotasDao:

    def __init__(self, db):
        self.db = db


    def dameNotas(self):
        cursor = self.db.cursor() # PARA ACCEDER A LA BD
        cursor.execute("SELECT * FROM Notas") # PARA OBTENER TODOS LOS DATOS DE LA BD QUE VAMOS A VER EN NUESTRO INDEX
        myresult = cursor.fetchall()  #PARA ACCEDER A TODOS LOS DATOS
        #CONVERTIR TODOS LOS DATOS A DICCIONARIO.
        insertObject = [] # AQUI VAN GUARDADAS LAS CLAVES DE LAS COLUMNAS
        columnNames = [column[0] for column in cursor.description] # PARA OBTENER LOS NOMBRES DE LAS COLUMNAS
        for record in myresult: # CON UN BUCLE DENTRO DE MYRESULT EXTRAIGO TODA LA INFORMACION 
            insertObject.append(dict(zip(columnNames,record))) # PARA IR METIENDO TODOS LOS DATOS EN FORMATO DICCIONARIO CON EL DICT. LA FUNCION ZIP ES PORQUE VAMOS A USAR COLUMN Y RECORD
        cursor.close() # PARA CERRAR EL CURSOR
        return insertObject


    def añadeNotas(self,CodigoAlumno,Seguridad,Implantacion,Redes):
        CodigoAlumno = request.form['CodigoAlumno'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL CODIGO ALUMNO QUE INDIQUEMOS
        Seguridad = request.form['Seguridad'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON LA NOTA QUE INDIQUEMOS
        Implantacion = request.form['Implantacion'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON LA NOTA QUE INDIQUEMOS
        Redes = request.form['Redes'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON LA NOTA QUE INDIQUEMOS

        if CodigoAlumno and Seguridad and Implantacion and Redes: # ESTA CONDICION SIRVE PARA QUE SI TENEMOS TODOS LOS CAMPOS VAMOS A HACER LA CONSULTA INSERT A LA BASE DE DATOS
            cursor = self.db.cursor() # ESTABLECEMOS UN CURSOR PARA LA CONEXION 
            sql = "INSERT INTO Notas (CodigoAlumno,Seguridad,Implantacion,Redes) VALUES (%s, %s, %s, %s)" # DEFINIMOS LA CONSULTA INSERT DE TIPO STRING %S
            data = (CodigoAlumno,Seguridad,Implantacion,Redes) # HACEMOS UNA TUPLA CON LOS DATOS 
            cursor.execute(sql,data) # Y SE LO PASAMOS CON LA FUNCION EXECUTE
            self.db.commit() # ESTO ES PARA MATERIALIZAR LA CONSULTA QUE HEMOS DEFINIDO


    def borrarNotas(self,CodigoAlumno):
        cursor = self.db.cursor() # ESTABLECEMOS UN CURSOR PARA LA CONEXION 
        sql = "DELETE FROM Notas WHERE CodigoAlumno=%s"
        data = [CodigoAlumno] # HACEMOS UNA TUPLA CON LOS DATOS 
        cursor.execute(sql,data) # Y SE LO PASAMOS CON LA FUNCION EXECUTE
        self.db.commit() # ESTO ES PARA MATERIALIZAR LA CONSULTA QUE HEMOS DEFINIDO

    def editNotas(self,Seguridad,Implantacion,Redes,CodigoAlumno):
        if CodigoAlumno and Seguridad and Implantacion and Redes: # ESTA CONDICION SIRVE PARA QUE SI TENEMOS TODOS LOS CAMPOS VAMOS A HACER LA CONSULTA INSERT A LA BASE DE DATOS
            cursor = self.db.cursor() # ESTABLECEMOS UN CURSOR PARA LA CONEXION 
            sql = "UPDATE Notas SET Seguridad = %s, Implantacion = %s, Redes = %s WHERE CodigoAlumno = %s"# DEFINIMOS LA CONSULTA UPDATE EN LOS SIGUIENTES CAMPOS
            data = (Seguridad,Implantacion,Redes,CodigoAlumno) # HACEMOS UNA TUPLA CON LOS DATOS 
            cursor.execute(sql,data) # Y SE LO PASAMOS CON LA FUNCION EXECUTE
            self.db.commit() # ESTO ES PARA MATERIALIZAR LA CONSULTA QUE HEMOS DEFINIDO
            #return redirect(url_for('notas')) # Y REDIRIGIMOS A HOME DE NUEVO. REDIRECT Y URL_FOR LO TENEMOS QUE IMPORTAR DE FLASK
