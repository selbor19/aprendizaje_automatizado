
# Cargamos el archivo (solo en collaborative) en caso contrario colocar el archivo en la raiz

import sqlite3

# Create a SQL connection to our SQLite database
con = sqlite3.connect("guia_fasecolda.sqlite")

cur = con.cursor()

# the result of a "cursor.execute" can be iterated over by row

#for row in cur.execute('SELECT Marca,Referencia1,Cilindraje,Peso,"2015","2016","2017" FROM carros where Cilindraje<1500 AND Cilindraje>1200 AND "2015">0;'):
#   print(row)
    
#AQUI Realize sus consultas sql de los datos

        #Consulta numero 1

cur.execute("select * from carros where Clase = 'MOTOCICLETA' AND Nacionalidad = 'COL'")
consulta = cur.fetchall()
print(consulta)

        #Consulta numero 2

cur.execute("select Marca,cilindraje,peso,CapacidadPasajeros,Clase, Servicio, Potencia, TipoCaja, Nacionalidad, Transmision from carros where CapacidadPasajeros > 60")
consulta2 = cur.fetchall()

for resultado_con2 in consulta2:
        print ("Marca:",resultado_con2[0], 
               "Cilindraje:",resultado_con2[1],
               "peso:", resultado_con2[2],
               "Capacidad Pasajeros:", resultado_con2[3],
               "Clase:", resultado_con2[4], 
               "Servicio:", resultado_con2[5], 
               "Potencia:", resultado_con2[6], 
               "TipoCaja:", resultado_con2[7], 
               "Nacionalidad:",  resultado_con2[8],
               "Transmision:",  resultado_con2[9])

        #Consulta numero 3

cur.execute('''
   CREATE TABLE Clientes (
   Id_Cliente INT(11) PRIMARY KEY,
   Nombre_Cliente VARCHAR(20),
   Apellido_CLiente VARCHAR (20),
   Nacionalidad_CLiente VARCHAR (20),
   Fecha_Nacimiento DATE,
   Ciudad_Nacimiento VARCHAR (20),
   Ciudad_Actual VARCHAR(20),
   Direccion_Cliente VARCHAR (50),
   Telefono_1 VARCHAR (20),
   Telefono_2 VARCHAR (20)  
   )         
''')

#Be sure to close the connection.
con.close()