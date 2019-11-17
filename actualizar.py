#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sqlite3

# actualizar data
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
  
  idEstudiante = input("\n Escribe el id del usuario que quieres editar: ")
  
  if not idEstudiante:
    print("Digita el ID...")
    exit()
      
  # pedir data para actualizar
  nombre = input("\nNuevo nombre -- (debe estar entre ' '): ")
  apellido = input("\nNuevo apellido -- (debe estar entre ' '): ")
  cedula = input("\nNueva cedula -- (debe estar entre ' '): ")
  telefono = input("\nNuevo telefono -- (debe estar entre ' '): ")
  
  actualizar = "UPDATE estudiante SET nombre = ?, apellido = ?, cedula = ?, telefono = ? WHERE id = ?"
  
  cursor.execute(actualizar, [nombre, apellido, cedula, telefono, idEstudiante])
  
  conexion.commit()
  
  print("Datos actualizados")
  
  conexion.close()
  
except sqlite3.OperationalError as error:
  print(error + "error al actualizar data")