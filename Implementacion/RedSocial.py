"""
Clase para gestionar la red social
"""

from TDAs.Grafo import Grafo, nodoVertice

class RedSocial:
  def __init__(self, dirigido = True) -> None:
    self.grafo = Grafo(dirigido)

  # Operaciones básicas
  def agregar_usuario(self, nombre_usuario:str):
    usuario = nodoVertice(nombre_usuario)
    self.grafo.insertarVertice(usuario.info)

    print(f'Usuario {usuario.info} registrado en la red social.')
    
  def agregar_relacion(self, usuario1: str, usuario2: str):
    nodo_usuario1 = self.grafo.buscarVertice(usuario1)
    nodo_usuario2 = self.grafo.buscarVertice(usuario2)

    result = self.existeUsuario(nodo_usuario1, nodo_usuario2)

    if result is False:
      return
    self.grafo.insertarArista(1, nodo_usuario1, nodo_usuario2)

  def eliminar_usuario(self, usuario:str):
    self.grafo.eliminarVertice(usuario)

    print(f'Usuario {usuario} eliminado de la red social.')

  def eliminar_relaciones(self, usuario1, usuario2):
    self.grafo.eliminarArista(usuario1, usuario2)

  def mostrar_conexiones(self):
    self.grafo.barridoVertices()

  def usuarios_estan_relacionados(self) -> bool:
    ...

  def recorrido_en_profundidad(self):
    ...

  def recorrido_en_anchura(self):
    ...

  def amigos_en_comun(self):
    ...

  def cantidad_amigos(self):
    ...

  # Operaciones clave
  def recomendar_amigos(self):
    ...

  def detectar_comunidades(self):
    ...

  def verificar_conectividad(self):
    ...

  def grado_de_conexion(self):
    ...

  def existe_usuario(self, usuario1: str, usuario2: str) -> bool:
    if usuario1 is None or usuario2 is None:
        if usuario1 is None:
          print(f'El usuario {usuario1} no está registrado en la red social')
        
        if usuario2 is None: 
          print(f'El usuario {usuario2} no está registrado en la red social')
        
        return False
    
    return True