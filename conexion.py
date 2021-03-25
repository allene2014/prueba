#!/usr/bin/python
import os
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

	print ("Parametros para la conexion:\nHost:{}\nPuerto:{}\n{}\nUsuario:{}\nDatabase:{}".format(Hst,Pto,Usr,Psw,Db))