"""
Clase para gestionar la red social
"""

from TDAs.Grafo import Grafo, nodo_vertice

class RedSocial:
  def __init__(self) -> None:
    self.grafo = Grafo(dirigido=False)


  # Operaciones básicas
  def agregar_usuario(self, nombre_usuario:str) -> None:
    usuario = nodo_vertice(nombre_usuario)
    self.grafo.insertar_vertice(usuario.info.lower())

    print(f'Usuario {usuario.info.title()} registrado en la red social.')
    

  def agregar_relacion(self, nombre_usuario1: str, nombre_usuario2: str) -> None: 
    nodo_usuario1, nodo_usuario2 = self.validar_usuario(nombre_usuario1.lower(), nombre_usuario2.lower())

    if nodo_usuario1 and nodo_usuario2:
      self.grafo.insertar_arista(1, nodo_usuario1, nodo_usuario2)

      print(f'Agregada la conexion entre {nombre_usuario1.title()} y {nombre_usuario2.title()}')


  def eliminar_usuario(self, nombre_usuario:str) -> None:
    nodo_usuario = self.validar_usuario(nombre_usuario)[0]

    if nodo_usuario:
      self.grafo.eliminar_vertice(nombre_usuario)

      print(f'Usuario {nombre_usuario.title()} eliminado de la red social.')


  def eliminar_relaciones(self, nombre_usuario1: str, nombre_usuario2: str) -> None:
    nodo_usuario1, nodo_usuario2 = self.validar_usuario(nombre_usuario1.lower(), nombre_usuario2.lower())

    if nodo_usuario1 and nodo_usuario2:
      self.grafo.eliminar_arista(nombre_usuario1, nombre_usuario2)

      print(f'Eliminada la conexion entre {nombre_usuario1.title()} y {nombre_usuario2.title()}')
    

  def mostrar_conexiones(self) -> None:
    usuarios_conectados = self.grafo.ver_conexiones()
    for usuario, conexiones in usuarios_conectados:
      if len(conexiones) == 0:
        print(f'\n{usuario.title()} no tiene conexiones')
        continue
      
      # Recorrer diccionario de conexiones
      print(f'\n{usuario.title()} está conectado con: ')
      for key, _ in conexiones.items():
        print(key.title())

    self.grafo.visualizar_grafo()


  def usuarios_estan_relacionados(self, nombre_usuario1: str, nombre_usuario2: str) -> None:
    nodo_usuario1, nodo_usuario2 = self.validar_usuario(nombre_usuario1, nombre_usuario2)
    
    if nodo_usuario1 and nodo_usuario2:
      estan_relacionados = self.grafo.existe_paso(nodo_usuario1, nodo_usuario2)

      if not estan_relacionados:
        print(f'Los usuarios {nombre_usuario1.title()} y {nombre_usuario2.title()} NO están relacionados directa o indirectamente')
        return
      
      print(f'Los usuarios {nombre_usuario1.title()} y {nombre_usuario2.title()} SI están relacionados directa o indirectamente')


  def recorrido_en_profundidad(self, nombre_usuario: str) -> None:
    nodo_usuario = self.validar_usuario(nombre_usuario)[0]

    if nodo_usuario:
      print('Barrido en profundidad')
      self.grafo.marcar_no_visitado()
      self.grafo.barrido_profundidad(nodo_usuario)
      self.grafo.marcar_no_visitado()

  def recorrido_en_anchura(self, nombre_usuario: str) -> None:
    nodo_usuario = self.validar_usuario(nombre_usuario)[0]

    if nodo_usuario:
      print('Barrido en anchura')
      self.grafo.marcar_no_visitado()
      self.grafo.barrido_amplitud(nodo_usuario)
      self.grafo.marcar_no_visitado()


  def amigos_en_comun(self, nombre_usuario1: str, nombre_usuario2: str) -> None:
    nodo_usuario1, nodo_usuario2 = self.validar_usuario(nombre_usuario1, nombre_usuario2)

    if nodo_usuario1 and nodo_usuario2:
      amigos_comunes = self.grafo.vertices_comunes(nodo_usuario1, nodo_usuario2)

      if len(amigos_comunes) == 0:
        print(f'No hay conexiones en común entre {nombre_usuario1.title()} y {nombre_usuario2.title()}')
        return
      
      print(f'Las conexiones comunes entre {nombre_usuario1.title()} y {nombre_usuario2.title()} son: ')
      for i in amigos_comunes:
        print(i)


  def cantidad_amigos(self, nombre_usuario: str) -> None:
    nodo_usuario = self.validar_usuario(nombre_usuario)[0]
    if nodo_usuario:
      cant_amigos = self.grafo.cantidad_de_conexiones(nodo_usuario)

      print(f'{nombre_usuario.title()} tiene {cant_amigos} amigos')


  # Operaciones clave
  def recomendar_amigos(self, nombre_usuario: str) -> None:
    nodo_usuario = self.validar_usuario(nombre_usuario)[0]

    if nodo_usuario:
      amigos_recomenados = self.grafo.recomendar_vertices(nodo_usuario)
      
      print(f'Los amigos recomendados de {nombre_usuario} son:')
      for amigo in amigos_recomenados:
        print(amigo)

  def detectar_comunidades(self) -> None:
    # Detectar comunidades de tamanño minimo de 5
    comunidades = self.grafo.detectar_comunidades(5)

    if len(comunidades) == 0:
      print('No hay comunidades')
      return
    
    for comunidad in comunidades:
      print(comunidad)


  def verificar_conectividad(self) -> None:
    es_conexo = self.grafo.es_conexo()

    if not es_conexo: 
      print('El grafo no es conexo')
      return
    
    print('El grafo si es conexo')


  def grado_de_conexion(self) -> None:
    usuario_mas_conexiones, cant_mas_conexiones = self.grafo.vertice_con_mas_conexiones()
    usuario_menos_conexiones, cant_menos_conexiones = self.grafo.vertice_con_menos_conexiones()

    print(f'El usuario con mas conexiones es {usuario_mas_conexiones.title()} con {cant_mas_conexiones} conexiones')
    print(f'El usuario con menos conexiones es {usuario_menos_conexiones.title()} con {cant_menos_conexiones} conexiones')


  # Guardar estructura del grafo
  def guardar_red_social(self, direccion_archivo):
        self.grafo.guardar_grafo(direccion_archivo)
    
  def cargar_red_social(self, direccion_archivo):
      self.grafo = Grafo.cargar_grafo(direccion_archivo)


  # Operaciones complementarias
  def validar_usuario(self, *args) -> list:
    nombre_usuarios = []
    nodo_usuarios = []

    for i in range(len(args)):
      # Obtener usuarios de los parámetros
      nombre_usuarios.append(args[i])

      # Buscar el vertice del usuario
      nodo_usuarios.append(self.buscar_usuario(nombre_usuarios[i]))

      # Verificar si el vertice existe
      if not self.verificar_usuarios(nodo_usuarios[i], nombre_usuarios[i]):
        return [None, None]
    
    return nodo_usuarios
  

  def buscar_usuario(self, nombre_usuario) -> nodo_vertice | None:
    return self.grafo.buscar_vertice(nombre_usuario)


  def verificar_usuarios(self, *args) -> bool:
    # Obtener los nodos de usuario de args
    usuarios = args[0::2]  

    # Obtener los nombres de usuario de args
    nombres = args[1::2]   
    
    for usuario, nombre in zip(usuarios, nombres):
        if usuario is None:
            print(f'El usuario {nombre.title()} no existe')
            return False
    
    return True
