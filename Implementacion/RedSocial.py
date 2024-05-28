"""
Clase para gestionar la red social
"""

from TDAs.Grafo import Grafo, nodo_vertice

class RedSocial:
  def __init__(self, dirigido = True) -> None:
    self.grafo = Grafo(dirigido)


  # Operaciones básicas
  def agregar_usuario(self, nombre_usuario:str) -> None:
    usuario = nodo_vertice(nombre_usuario)
    self.grafo.insertar_vertice(usuario.info)

    print(f'Usuario {usuario.info} registrado en la red social.')
    

  def agregar_relacion(self, nombre_usuario1: str, nombre_usuario2: str) -> None: 
    # Buscar el Vertice del usuario
    nodo_usuario1 = self.buscar_usuario(nombre_usuario1)
    nodo_usuario2 = self.buscar_usuario(nombre_usuario2)

    # Verificar si los usuarios existen
    if not self.verificar_usuarios(nodo_usuario1, nodo_usuario2, nombre_usuario1, nombre_usuario2):
      return

    self.grafo.insertar_arista(1, nodo_usuario1, nodo_usuario2)

    print(f'Agregada la conexion entre {nombre_usuario1} y {nombre_usuario2}')


  def eliminar_usuario(self, nombre_usuario:str) -> None:
    self.grafo.eliminar_vertice(nombre_usuario)

    print(f'Usuario {nombre_usuario} eliminado de la red social.')


  def eliminar_relaciones(self, nombre_usuario1: str, nombre_usuario2: str) -> None:
    self.grafo.eliminar_arista(nombre_usuario1, nombre_usuario2)

    print(f'Eliminada la conexion entre {nombre_usuario1} y {nombre_usuario2}')


  def mostrar_conexiones(self) -> None:
    usuarios_conectados = self.grafo.ver_conexiones()
    for usuario, conexiones in usuarios_conectados:
      if len(conexiones) == 0:
        print(f'{usuario} no tiene conexiones')
        continue
      
      # Recorrer diccionario de conexiones
      print(f'{usuario} está conectado con: ')
      for key, _ in conexiones.items():
        print(key)


  def usuarios_estan_relacionados(self, nombre_usuario1: str, nombre_usuario2: str) -> None:
    # Buscar el Vertice del usuario
    nodo_usuario1 = self.buscar_usuario(nombre_usuario1)
    nodo_usuario2 = self.buscar_usuario(nombre_usuario2)

    # Verificar si los usuarios existen
    if not self.verificar_usuarios(nodo_usuario1, nodo_usuario2, nombre_usuario1, nombre_usuario2):
      return
    
    si_relacionados = self.grafo.existe_paso(nodo_usuario1, nodo_usuario2)

    if not si_relacionados:
      print(f'Los usuarios {nombre_usuario1} y {nombre_usuario2} NO están relacionados directa o indirectamente')
      return
    
    print(f'Los usuarios {nombre_usuario1} y {nombre_usuario2} SI están relacionados directa o indirectamente')


  def recorrido_en_profundidad(self, nombre_usuario: str) -> None:
    nodo_usuario = self.buscar_usuario(nombre_usuario)

    # Verificar si el usuario existe
    if not self.verificar_usuarios(nodo_usuario, nombre_usuario):
      return

    print('Barrido en profundidad')
    self.grafo.marcar_no_visitado()
    self.grafo.barrido_profundidad(nodo_usuario)
    self.grafo.marcar_no_visitado()

  def recorrido_en_anchura(self, nombre_usuario: str) -> None:
    nodo_usuario = self.buscar_usuario(nombre_usuario)

    # Verificar si el usuario existe
    if not self.verificar_usuarios(nodo_usuario, nombre_usuario):
      return

    print('Barrido en anchura')
    self.grafo.marcar_no_visitado()
    self.grafo.barrido_amplitud(nodo_usuario)
    self.grafo.marcar_no_visitado()


  def amigos_en_comun(self, nombre_usuario1: str, nombre_usuario2: str) -> None:
    # Buscar el Vertice del usuario
    nodo_usuario1 = self.buscar_usuario(nombre_usuario1)
    nodo_usuario2 = self.buscar_usuario(nombre_usuario2)

    # Verificar si los usuarios existen
    if not self.verificar_usuarios(nodo_usuario1, nodo_usuario2, nombre_usuario1, nombre_usuario2):
      return
    
    amigos_comunes = self.grafo.vertices_comunes(nodo_usuario1, nodo_usuario2)

    if len(amigos_comunes) == 0:
      print(f'No hay conexiones en común entre {nombre_usuario1} y {nombre_usuario2}')
      return
    
    print(f'Las conexiones comunes entre {nombre_usuario1} y {nombre_usuario2} son: ')
    for i in amigos_comunes:
      print(i)

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


  def verificar_usuarios(self, *args) -> bool:
    usuarios = args[0::2]  # Obtiene los nodos de usuario de args
    nombres = args[1::2]   # Obtiene los nombres de usuario de args
    
    for usuario, nombre in zip(usuarios, nombres):
        if usuario is None:
            print(f'El usuario {nombre} no existe')
            return False
    
    return True
