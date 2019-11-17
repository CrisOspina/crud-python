#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sqlite3

# Inserta data
try:
  db = 'estudiantes.db'
  conexion = sqlite3.connect(db)
  
  print("conexion realizada con exito a la bd " + db)
  
  cursor = conexion.cursor()
  
  insertar = "INSERT INTO estudiante (nombre, apellido, cedula, telefono) VALUES (?,?,?,?)"
  
  data = ("thor", "midgar", "2020", "4124565656")
  
  cursor.execute(insertar, data)
    
  # Guardamos cambios
  conexion.commit()
  
  print("Guardado exitosamente")
  
  conexion.close()
  
except sqlite3.OperationalError as error:
  print(error + "error al insertar estudiante")