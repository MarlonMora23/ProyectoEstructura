"""
Clase para gestionar la red social
"""

from TDAs.Grafo import Grafo

class RedSocial:
  def __init__(self) -> None:
    self.grafo = Grafo()

  # Operaciones básicas
  def agregarUsuario(self, usuario):
    self.grafo.insertarVertice(usuario)
    print(f'Usuario {usuario} registrado en la red social.')

  def agregarRelacion(self, usuario1, usuario2):
    self.grafo.insertarArista(0, usuario1, usuario2)

  def eliminarUsuario(self):
    ...

  def eliminarRelaciones(self):
    ...

  def mostrarConexiones(self):
    ...

  def usuariosEstanRelacionados(self) -> bool:
    ...

  def recorridoEnProfundidad(self):
    ...

  def recorridoEnAnchura(self):
    ...

  def amigosEnComun(self):
    ...

  def cantidadAmigos(self):
    ...

  # Operaciones clave
  def recomendarAmigos(self):
    ...

  def detectarComunidades(self):
    ...

  def verificarConectividad(self):
    ...

  def gradoDeConexion(self):
    ...