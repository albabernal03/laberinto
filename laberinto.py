
#variables para el laberinto
#Estas variables las pongo en forma de tupla (ya que sirve para agrupara varios valores convirtiéndolos en uno)

muros = ((0,1),(0,2),(0,3),(0,4),(1,1),(2,1),(2,3),(3,3),(4,0),(4,1),(4,2),(4,3),(0,5),(1,5),(2,5),(3,5),(4,5))
entrada = ((0,0),(0,0)) 
salida = ((4,4),(4,4))

#En primer lugar definimos las dimensiones del laberinto y el recorrido

def laberinto(dimension,muros):
  laberinto = []

  for i in range(dimension): 
      fila = []

      for j in range(dimension):

          if tuple ([i,j]) in muros:
              fila.append('X')

          elif tuple ([i,j]) in entrada:
              fila.append('E')

          elif tuple ([i,j]) in salida:
              fila.append('S')

          else:
              fila.append(' ')
      laberinto.append(fila)
      return laberinto 

          
imagenlaberinto = laberinto(6,muros)

for i in imagenlaberinto:
    print(' '.join(i))

#Una vez creado el laberinto nos ponemos en marcha en programar la tarea 

def salir_del_laberinto (laberinto):
    n = 6   #La dimensión que se ha establecido para este laberinto
    fila = 0
    columna = 0 
