from flask import request
#from appFlask import database as db
#from appFlask.src.database import database



class AlumnDao:

    def __init__(self, db):
        self.db = db

    def dameTodos(self):
        cursor = self.db.cursor() # PARA ACCEDER A LA BD
        cursor.execute("SELECT * FROM InformacionAlumno") # PARA OBTENER TODOS LOS DATOS DE LA BD QUE VAMOS A VER EN NUESTRO INDEX
        myresult = cursor.fetchall()  #PARA ACCEDER A TODOS LOS DATOS
        #CONVERTIR TODOS LOS DATOS A DICCIONARIO.
        insertObject = [] # AQUI VAN GUARDADAS LAS CLAVES DE LAS COLUMNAS
        columnNames = [column[0] for column in cursor.description] # PARA OBTENER LOS NOMBRES DE LAS COLUMNAS
        for record in myresult: # CON UN BUCLE DENTRO DE MYRESULT EXTRAIGO TODA LA INFORMACION 
            insertObject.append(dict(zip(columnNames,record))) # PARA IR METIENDO TODOS LOS DATOS EN FORMATO DICCIONARIO CON EL DICT. LA FUNCION ZIP ES PORQUE VAMOS A USAR COLUMN Y RECORD
        cursor.close() # PARA CERRAR EL CURSOR
        return insertObject


    def añadirUsuario(self,nombre,apellido,centroFormativo):
        if nombre and apellido and centroFormativo: # ESTA CONDICION SIRVE PARA QUE SI TENEMOS TODOS LOS CAMPOS VAMOS A HACER LA CONSULTA INSERT A LA BASE DE DATOS
            cursor = self.db.cursor() # ESTABLECEMOS UN CURSOR PARA LA CONEXION 
            sql = "INSERT INTO InformacionAlumno (Nombre,Apellido,CentroFormativo) VALUES (%s, %s, %s)" # DEFINIMOS LA CONSULTA INSERT DE TIPO STRING %S
            data = (nombre,apellido,centroFormativo) # HACEMOS UNA TUPLA CON LOS DATOS 
            cursor.execute(sql,data) # Y SE LO PASAMOS CON LA FUNCION EXECUTE
            self.db.commit() # ESTO ES PARA MATERIALIZAR LA CONSULTA QUE HEMOS DEFINIDO


    def editarUsuario(self,Nombre,Apellido,CentroFormativo,CodigoAlumno):
        if Nombre and Apellido and CentroFormativo: # ESTA CONDICION SIRVE PARA QUE SI TENEMOS TODOS LOS CAMPOS VAMOS A HACER LA CONSULTA INSERT A LA BASE DE DATOS
            cursor = self.db.cursor() # ESTABLECEMOS UN CURSOR PARA LA CONEXION 
            sql = "UPDATE InformacionAlumno SET Nombre = %s, Apellido = %s, CentroFormativo = %s WHERE CodigoAlumno = %s"# DEFINIMOS LA CONSULTA UPDATE EN LOS SIGUIENTES CAMPOS
            data = (Nombre,Apellido,CentroFormativo,CodigoAlumno) # HACEMOS UNA TUPLA CON LOS DATOS 
            cursor.execute(sql,data) # Y SE LO PASAMOS CON LA FUNCION EXECUTE
            self.db.commit() # ESTO ES PARA MATERIALIZAR LA CONSULTA QUE HEMOS DEFINIDO


    def borrarUsuario(self,CodigoAlumno):
        cursor = self.db.cursor() # ESTABLECEMOS UN CURSOR PARA LA CONEXION 
        sql = "DELETE FROM InformacionAlumno WHERE CodigoAlumno=%s"
        data = [CodigoAlumno] 
        cursor.execute(sql,data) # Y SE LO PASAMOS CON LA FUNCION EXECUTE
        self.db.commit() # ESTO ES PARA MATERIALIZAR LA CONSULTA QUE HEMOS DEFINIDO


    