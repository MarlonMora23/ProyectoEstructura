"""
Clase para gestionar la red social
"""

from TDAs.Grafo import Grafo, nodo_vertice

class RedSocial:
  def __init__(self, dirigido = True) -> None:
    self.grafo = Grafo(dirigido)

  # Operaciones básicas
  def agregar_usuario(self, nombre_usuario:str):
    usuario = nodo_vertice(nombre_usuario)
    self.grafo.insertar_vertice(usuario.info)

    print(f'Usuario {usuario.info} registrado en la red social.')
    
  def agregar_relacion(self, nombre_usuario1: str, nombre_usuario2: str): 
    # Buscar el Vertice del usuario
    nodo_usuario1 = self.buscar_usuario(nombre_usuario1)
    nodo_usuario2 = self.buscar_usuario(nombre_usuario2)

    # Verificar si los usuarios existen
    if not self.verificar_usuarios(nodo_usuario1, nodo_usuario2, nombre_usuario1, nombre_usuario2):
      return

    self.grafo.insertar_arista(1, nodo_usuario1, nodo_usuario2)

  def eliminar_usuario(self, usuario:str):
    self.grafo.eliminar_vertice(usuario)

    print(f'Usuario {usuario} eliminado de la red social.')

  def eliminar_relaciones(self, usuario1, usuario2):
    self.grafo.eliminar_arista(usuario1, usuario2)

  def mostrar_conexiones(self):
    self.grafo.ver_conexiones()

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

  # Operaciones complementarias
  def buscar_usuario(self, nombre_usuario) -> nodo_vertice | None:
    return self.grafo.buscar_vertice(nombre_usuario)

  def verificar_usuarios(self, nodo_usuario1: nodo_vertice, nodo_usuario2: nodo_vertice, nombre_usuario1: str, nombre_usuario2: str) -> bool:
    if nodo_usuario1 is None or nodo_usuario2 is None:
        if nodo_usuario1 is None and nodo_usuario2 is None:
            print(f'Los usuarios {nombre_usuario1} y {nombre_usuario2} no existen')
        elif nodo_usuario1 is None:
            print(f'El usuario {nombre_usuario1} no existe')
        elif nodo_usuario2 is None:
            print(f'El usuario {nombre_usuario2} no existe')
        return False
    
    return True