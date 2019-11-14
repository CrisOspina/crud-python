import sqlite3

conexion = sqlite3.connect('estudiantes.db')

# Creamos el cursor
cursor = conexion.cursor()

# Ahora crearemos una tabla de usuarios para almacenar nombres, edades y emails
#cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")

# Crear usuarios
#cursor.execute("INSERT INTO usuarios VALUES ('cris', 22, 'cris@gmail.com')")

# Consutar usuarios
# cursor.execute("SELECT * FROM usuarios")
# usuario = cursor.fetchone()
# print('Nombre: ' + usuario[0])
# print(usuario[1])
# print('Email: ' + usuario[2])

# usuarios = cursor.fetchall()

# for usuario in usuarios:
#   print("Nombre:", usuario[0], "Email: ", usuario[2])

cursor.execute('''
  CREATE TABLE estudiante (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    cedula VARCHAR(100) NOT NULL,
    telefono VARCHAR(50) NOT NULL,
  )
  ''')

# estudiante = [
#   ('Cris', 'Ospina', '101010', '2934545'),
#   ('Hel', 'Midgard', '1212', '434')
# ]

# cursor.executemany("INSERT INTO estudiante VALUES (null, ?, ?, ?, ?)", estudiante)

# Guardamos los cambios haciendo un commit
conexion.commit()

conexion.close()