#!/usr/bin/python
import os
import time
import psycopg2
from io import open
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__),'.env')
load_dotenv(dotenv_path)

if __name__ == "__main__":
	Hst = os.getenv('HOST')
	Pto = os.getenv('PUERTO')
	Usr = os.getenv('USUARIO')
	Psw = os.getenv('PASS')
	Db = os.getenv('DB')
	
	#print ("Parametros para la conexion:\nHost:{}\nPuerto:{}\n{}\nUsuario:{}\nDatabase:{}".format(Hst,Pto,Usr,Psw,Db))


aceptar="s"
cancelar="n"
i=0
while i<1:
	print "Gestor de base de datos desde PYTHON \n Ejercicion de evaluacion para ISEP \n Autor: Edgar Allen\n"
	#time.sleep(2)
	print "Por favor Seleccione la Opcion a Realizar luego precione Enter\n"
	print "0.-Consultar desde una base de datos\n1.-Consultar una base de datos\n2.-Cargar Datos \n3.-Eliminar un Registro\n4.-Actualizar un Registro\n5.-Salir\n"
	confirmacion= raw_input("Opcion:")
	conf=int(confirmacion)
#----------------------------------------------------------------------------
	if conf == 0:

		listardb="psql --host " + Hst + " --port 5432 --username 'postgres' -l"
		os.system(listardb)
		print "....prueba"
#----------------------------------------------------------------------------
	elif conf ==1:
		print "CARGANDO INFORMACION A LA BASE DE DATOS\nConsultar Usuarios"
		conexion=psycopg2.connect(host=Hst,database=Db,user=Usr,password=Psw)
		cur= conexion.cursor()
		cur.execute("SELECT nombre, apellido FROM prueba")
		for nombre,apellido in cur.fetchall():
			print nombre, apellido 
		conexion.close()



#----------------------------------------------------------------------------		
	elif conf ==2:
		print "CARGANDO INFORMACION A LA BASE DE DATOS\nAGREGAR USUARIO"
		nusr=raw_input("Nombre de Usuario:\n")
		ausr=raw_input("Apellido de Usuario\n")
		conexion=psycopg2.connect(host=Hst,database=Db,user=Usr,password=Psw)
		
		cur= conexion.cursor()
		query="INSERT into prueba(nombre, apellido) values (%s,%s)"
		datos=(nusr,ausr)
		cur.execute(query,datos)
		conexion.commit()
		cur.execute("SELECT nombre, apellido FROM prueba")
		for nombre,apellido in cur.fetchall():
			print nombre, apellido 
		conexion.close()
#-------------------------------------------------------------------------

	elif conf ==3:
		print "CARGANDO INFORMACION A LA BASE DE DATOS\nEliminar Registro"
		conexion=psycopg2.connect(host=Hst,database=Db,user=Usr,password=Psw)
		cur= conexion.cursor()
		cur.execute("SELECT id,nombre, apellido FROM prueba")
		for id, nombre,apellido in cur.fetchall():
			print id,nombre, apellido 

		
		dusr=raw_input("Usuario a Eliminar:\n")
		
		
		#conexion=psycopg2.connect(host=Hst,database=Db,user=Usr,password=Psw)
		
		#cur= conexion.cursor()
		#cur.execute("SELECT nombre, apellido FROM prueba")
		query="DELETE from prueba WHERE id="+dusr
		

		cur.execute(query)
		conexion.commit()

		cur.execute("SELECT nombre, apellido FROM prueba")
		for nombre,apellido in cur.fetchall():
			print nombre, apellido 
		conexion.close()	

#-------------------------------------------------------------------------

	elif conf == 4:
		#ndb=raw_input("Nombre para la Base de Datos a Crear\n")

		print "CARGANDO INFORMACION A LA BASE DE DATOS\nActualizar Registro"
		conexion=psycopg2.connect(host=Hst,database=Db,user=Usr,password=Psw)
		cur= conexion.cursor()
		cur.execute("SELECT id,nombre, apellido FROM prueba")
		for id, nombre,apellido in cur.fetchall():
			print id,nombre, apellido 

		
		dusr=raw_input("Usuario a Actualizar:\n")
		nwd=raw_input("Actualizar Nombre\n:")

		query="UPDATE prueba SET nombre=%s WHERE id= %s"
		cur.execute(query,(nwd,dusr))
		conexion.commit()

		cur.execute("SELECT nombre, apellido FROM prueba")
		for nombre,apellido in cur.fetchall():
			print nombre, apellido 
		conexion.close()	
		

	elif conf == 5:
		print "Gracias por usar el gestor de base de datos desde Python"
		time.sleep(1)
		break
	#mensaje en terminal 
		#print "..generando"
		#nombredb=raw_input("Nombre de la base de datos\n")
		#hostdb=raw_input("ip del servidor de la base de datos\n")
		#usuariodb=raw_input("Usuario de la base de datos\n")
		#passdb=raw_input("password para la base de datos\n")
		#conexion=psycopg2.connect(host=Hst,database=Db,user=Usr,password=Psw)
		#cur= conexion.cursor()
		#cur.execute("SELECT nombre, apellido FROM prueba")

		#for nombre, apellido in cur.fetchall():
		#	print nombre, apellido 
		#conexion.close()

	#cf1=raw_input("los datos son correctos")
	#if cf1 == aceptar:
	#	print "Los datos han sido cargados"
	#else:
	#	os.system(confirmacion)# buscar como regresar al principio del bucle
	##################ME ESTA BORRANDO EL .ENV################
	#env=open("env.txt","w")
	#env.write(nombred)
	#env.close()
	###################REVISAR#################################
