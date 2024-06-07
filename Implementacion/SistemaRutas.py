"""
Clase para gestionar el sistema de rutas
"""

from TDAs.Grafo import Grafo, nodo_vertice

def dijkstra(grafo: Grafo, origen: nodo_vertice, destino: nodo_vertice):
  distancias = {origen.info: 0}
  anteriores = {origen.info: None}
  visitados = set()
  no_visitados = set()
  
  # Obtener todos los vertices
  aux = grafo.inicio
  while aux is not None:
      no_visitados.add(aux.info)
      if aux.info != origen.info:
          distancias[aux.info] = float('inf')
          anteriores[aux.info] = None
      aux = aux.sig

  while no_visitados:
      vertice_actual = min(no_visitados, key=lambda vertice: distancias[vertice])
      if distancias[vertice_actual] == float('inf'):
          break

      no_visitados.remove(vertice_actual)
      visitados.add(vertice_actual)

      vertice_nodo = grafo.buscar_vertice(vertice_actual)
      adyacentes = vertice_nodo.adyacentes.inicio

      while adyacentes is not None:
          vecino = adyacentes.destino
          if vecino in visitados:
              adyacentes = adyacentes.sig
              continue
          
          nueva_distancia = distancias[vertice_actual] + adyacentes.info
          if nueva_distancia < distancias[vecino]:
              distancias[vecino] = nueva_distancia
              anteriores[vecino] = vertice_actual

          adyacentes = adyacentes.sig

  camino = []
  distancia_total = distancias[destino.info]
  vertice_actual = destino.info

  # Si la distancia total es infinita, no hay camino
  if distancia_total == float('inf'):
      return None, []

  # Obtener el camino mas corto
  while vertice_actual is not None:
      camino.append(vertice_actual)
      vertice_actual = anteriores[vertice_actual]

  return distancia_total, camino[::-1]

class SistemaRutas():
  def __init__(self) -> None:  
    self.grafo = Grafo(dirigido=False)

  def agregar_ubicacion(self, nombre_ubicacion: str) -> None:
    ubicacion = nodo_vertice(nombre_ubicacion)
    self.grafo.insertar_vertice(ubicacion.info.lower())

    print(f'Ubicacion {ubicacion.info.title()} registrado en el sistema de rutas')

  def agregar_conexion(self, nombre_ubicacion1: str, nombre_ubicacion2: str, distancia: str) -> None:
    nodo_ubicacion1, nodo_ubicacion2 = self.validar_ubicacion(nombre_ubicacion1, nombre_ubicacion2)
    try:
      distancia = float(distancia)
    except ValueError:
       print('Distancia debe de ser un numero')
       return

    if nodo_ubicacion1 and nodo_ubicacion2:
      self.grafo.insertar_arista(distancia, nodo_ubicacion1, nodo_ubicacion2)

      print(f'Agregada la conexion entre {nombre_ubicacion1.title()} y {nombre_ubicacion2.title()} con distancia de {distancia}')

  def eliminar_ubicacion(self, nombre_ubicacion: str) -> None:
    self.grafo.eliminar_vertice(nombre_ubicacion)

  def eliminar_conexion(self, nombre_ubicacion1: str, nombre_ubicacion2: str) -> None:
    nodo_ubicacion1, nodo_ubicacion2 = self.validar_ubicacion(nombre_ubicacion1, nombre_ubicacion2)

    if nodo_ubicacion1 and nodo_ubicacion2:
       self.grafo.eliminar_arista(nodo_ubicacion1, nodo_ubicacion2)
       

  def camino_mas_corto(self, nombre_ubicacion1: str, nombre_ubicacion2: str) -> None:
    origen: nodo_vertice = self.grafo.buscar_vertice(nombre_ubicacion1.lower())
    destino: nodo_vertice = self.grafo.buscar_vertice(nombre_ubicacion2.lower())
    
    if origen is None or destino is None:
        print('Una o ambas ubicaciones no existen.')
        return

    distancia, camino = dijkstra(self.grafo, origen, destino)
    if distancia is not None:
        print(f'La distancia más corta entre {nombre_ubicacion1.title()} y {nombre_ubicacion2.title()} es {round(distancia, 2)}')
        print('El camino es:', ' -> '.join([ubicacion.title() for ubicacion in camino]))
        self.grafo.visualizar_grafo(camino)
    else:
        print(f'No existe un camino entre {nombre_ubicacion1.title()} y {nombre_ubicacion2.title()}')
    

  def ruta_mas_corta(self) -> None:
    self.grafo.barrido_profundidad(self.grafo.inicio)


  def ver_mapa(self) -> None:
    self.grafo.visualizar_grafo()


  # Guardar estructura del grafo
  def guardar_rutas(self, direccion_archivo):
        self.grafo.guardar_grafo(direccion_archivo)
    
  def cargar_rutas(self, direccion_archivo):
      self.grafo = Grafo.cargar_grafo(direccion_archivo)


  # Operaciones complementarias
  def validar_ubicacion(self, *args) -> list:
    nombre_ubicacion = []
    nodo_ubicacion = []

    for i in range(len(args)):
      # Obtener usuarios de los parámetros
      nombre_ubicacion.append(args[i])

      # Buscar el vertice del usuario
      nodo_ubicacion.append(self.buscar_ubicacion(nombre_ubicacion[i]))

      # Verificar si el vertice existe
      if not self.verificar_ubicacion(nodo_ubicacion[i], nombre_ubicacion[i]):
        return [None, None]
    
    return nodo_ubicacion
  
  def buscar_ubicacion(self, nombre_ubicacion) -> nodo_vertice | None:
    return self.grafo.buscar_vertice(nombre_ubicacion)


  def verificar_ubicacion(self, *args) -> bool:
    # Obtener los nodos de ubicacion de args
    ubicaciones = args[0::2]  

    # Obtener los nombres de ubicacion de args
    nombres = args[1::2]   
    
    for ubicacion, nombre in zip(ubicaciones, nombres):
        if ubicacion is None:
            print(f'La ubicacion {nombre.title()} no existe')
            return False
    
    return True