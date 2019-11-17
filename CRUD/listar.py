#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sqlite3

# listar o read data

try:
  db = 'estudiantes.db'
  conexion = sqlite3.connect(db)
  
  print("conexion realizada con exito a la bd " + db)
  
  cursor = conexion.cursor()
  
  listar = "SELECT * from estudiante"

  cursor.execute(listar)

  listarEstudiantes = cursor.fetchall()    

  print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("", "", "", "", ""))
  print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("ID", "Nombre", "Apellido", "Cédula", "Teléfono"))
  print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("", "", "", "", ""))

  for id, nombre, apellido, cedula, telefono in listarEstudiantes:
    print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(id, nombre, apellido, cedula, telefono))

  print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("", "", "", "", ""))
  
  conexion.close()
  

except sqlite3.OperationalError as error:
  print("Error al abrir:", error)