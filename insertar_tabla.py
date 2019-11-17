#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sqlite3

try:
  db = 'estudiantes.db'
  conexion = sqlite3.connect(db)
  
  print("conexion realizada con exito a la bd " + db)
  
  cursor = conexion.cursor()
  
except sqlite3.OperationalError as error:
  print("Error al abrir:", error)
  
Crear tablas en bd si no existe
try:
  tablas = [
    """
      CREATE TABLE IF NOT EXISTS estudiante(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(100) NOT NULL,
        apellido VARCHAR(100) NOT NULL,
        cedula VARCHAR(100) NOT NULL,
        telefono VARCHAR(50) NOT NULL
      )
    """
  ]
  
  for tabla in tablas:
    cursor.execute(tabla)
    
  conexion.close()
  
  print("Tabla creada correctamente ")
except sqlite3.OperationalError as error:
  print(error + "Error al crear tabla en la db " + db)