"""
Implementación de una red social con grafos

Autores:
  Marlon Daniel Mora
  Luis Edward Mosquera
"""

from Implementacion.RedSocial import RedSocial

def imprimir_titulo():
  print()
  print('='*30)
  print('Red Social con Grafos')
  print('='*30)
  print()

def opciones_menu() -> dict:
  return {
    1 : 'Agregar un usuario',
    2 : 'Agregar Relacion entre usuarios',
    3 : 'Eliminar un usuario',
    4 : 'Eliminar una relacion',
    5 : 'Mostrar conexiones',
    6 : 'Verificar si dos usuarios están relacionados',
    7 : 'Recorrido en profundidad',
    8 : 'Recorrido en anchura',
    9 : 'Amigos en comun',
    10 : 'Cantidad de amigos',
    11 : 'Recomendaciones de amigos',
    12 : 'Detectar comunidades',
    13 : 'Verificar conectividad',
    14 : 'Analizar grado de conexion'
  }

def imprimir_opciones() -> None:
  opciones: dict = opciones_menu()
  for index, opcion in opciones.items():
    print(f'{index}. {opcion}')

def validar_opcion() -> int:
  try:
      opcion = int(input())
      return opcion
  except ValueError:
      print('\nPor favor, digite un numero')
      return validar_opcion()
  
# Operaciones Basicas
def agregar_usuario(red_social: RedSocial) -> None:
  nombre = input('\nDigite el nombre del usuario: ')
  red_social.agregar_usuario(nombre)

def agregar_relacion(red_social: RedSocial) -> None:
  print('\nIngrese los nombres de los usuarios que quiere agregar la relacion')
  usuario1 = input('Usuario 1: ')
  usuario2 = input('Usuario 2: ')

  red_social.agregar_relacion(usuario1, usuario2)

def eliminar_usuario(red_social: RedSocial) -> None:
  nombre = input('\nIngrese el nombre de el usuario a eliminar: ')
  red_social.eliminar_usuario(nombre)

def eliminar_relacion(red_social: RedSocial) -> None:
  print('\nIngrese los nombres de los que quiere eliminar la relacion')
  usuario1 = input('Usuario 1: ')
  usuario2 = input('Usuario 2: ')

  red_social.eliminar_relaciones(usuario1, usuario2)

# Representacion gráfica
def mostrar_conexiones(red_social: RedSocial) -> None:
  red_social.mostrar_conexiones()

def usuarios_estan_relacionados(red_social: RedSocial) -> None:
  print('\nIngrese los nombres de los que quiere ver si estan relacionados')
  usuario1 = input('Usuario 1: ')
  usuario2 = input('Usuario 2: ')

  red_social.usuarios_estan_relacionados(usuario1, usuario2)

def recorrido_en_profundidad(red_social: RedSocial) -> None:
  nombre = input('\nIngrese el nombre de el usuario a recorrer: ')
  red_social.recorrido_en_profundidad(nombre)

def recorrido_en_anchura(red_social: RedSocial) -> None:
  nombre = input('\nIngrese el nombre de el usuario a recorrer: ')
  red_social.recorrido_en_anchura(nombre)

def amigos_en_comun(red_social: RedSocial) -> None:
  print('\nIngrese los nombres de los usuarios que quiere ver sus amigos en comun')
  usuario1 = input('Usuario 1: ')
  usuario2 = input('Usuario 2: ')

  red_social.amigos_en_comun(usuario1, usuario2)

def cantidad_amigos(red_social: RedSocial) -> None:
  nombre = input('\nIngrese el nombre de el usuario a ver su cantidad de amigos:')
  red_social.cantidad_amigos(nombre)

# Operaciones Clave
def recomendar_amigos(red_social: RedSocial) -> None:
  nombre = input('\nIngrese el nombre de el usuario a recomendar amigos:')
  red_social.recomendar_amigos(nombre)

def detectar_comunidades(red_social: RedSocial) -> None:
  red_social.detectar_comunidades()

def verificar_conectividad(red_social: RedSocial) -> None:
  red_social.verificar_conectividad()

def grado_conexion(red_social: RedSocial) -> None:
  red_social.grado_de_conexion()


def menu(red_social: RedSocial, direccion_archivo_red_social):
  while True:
    imprimir_titulo()
    imprimir_opciones()
    print('\n0. Salir del programa')
    
    opcion = validar_opcion()

    match(opcion):
      case 1:
        agregar_usuario(red_social)

      case 2: 
        agregar_relacion(red_social)

      case 3:
        eliminar_usuario(red_social)

      case 4:
        eliminar_relacion(red_social)

      case 5:
        mostrar_conexiones(red_social)

      case 6: 
        usuarios_estan_relacionados(red_social)

      case 7:
        recorrido_en_profundidad(red_social)

      case 8:
        recorrido_en_anchura(red_social)

      case 9:
        amigos_en_comun(red_social)

      case 10:
        cantidad_amigos(red_social)

      case 11:
        recomendar_amigos(red_social)

      case 12:
        detectar_comunidades(red_social)

      case 13:
        verificar_conectividad(red_social)

      case 14:
        grado_conexion(red_social)

      case 0:
        # Guardar estructura del grafo
        red_social.guardar_red_social(direccion_archivo_red_social)
        print('Se guardó la red social')
        return

def main():
  red_social = RedSocial()
  DIRECCION_ARCHIVO_RED_SOCIAL = 'Implementacion/red_social.pkl'

  # Cargar la red social desde un archivo si existe, de lo contrario crear una nueva
  try:
      red_social.cargar_red_social(DIRECCION_ARCHIVO_RED_SOCIAL)
      print("Red social cargada desde el archivo.")
  except FileNotFoundError:
      print("Archivo no encontrado. Se ha creado una nueva red social.")
  
  menu(red_social, DIRECCION_ARCHIVO_RED_SOCIAL)

if __name__ == '__main__':
  main()