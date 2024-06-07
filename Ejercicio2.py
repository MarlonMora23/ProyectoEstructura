"""
Implementación del algoritmo Dijkstra con grafos

Autores:
  Marlon Daniel Mora
  Luis Edward Mosquera
"""

from Implementacion.SistemaRutas import SistemaRutas

def imprimir_titulo():
  print()
  print('='*30)
  print('Sistema de Rutas con Grafos')
  print('='*30)
  print()

def opciones_menu() -> dict:
  return {
    1 : 'Agregar una ubicacion',
    2 : 'Agregar conexion entre dos ubicaciones',
    3 : 'Eliminar ubicacion',
    4 : 'Eliminar Conexion entre dos ubicaciones',
    5 : 'Visualizar mapa',
    6 : 'Encontrar el camino mas corto entre dos ubicaciones',
    7 : 'Encontrar la ruta mas corta',
    
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
  
def agregar_ubicacion(sistema_rutas: SistemaRutas) -> None:
  nombre = input('Digite el nombre de la ubicacion: ')
  sistema_rutas.agregar_ubicacion(nombre)

def agregar_conexion(sistema_rutas: SistemaRutas) -> None:
  print('Digite las dos ubicaciones a crear una conexion')
  ubicacion1 = input('ubicacion 1: ')
  ubicacion2 = input('ubicacion 2: ')
  distancia = input('Digite la distancia entre las ubicaciones (Numero): ')

  sistema_rutas.agregar_conexion(ubicacion1, ubicacion2, distancia)

def eliminar_ubicacion(sistema_rutas: SistemaRutas) -> None:
  nombre = input('Digite la ubicacion a eliminar')
  sistema_rutas.eliminar_ubicacion(nombre)

def eliminar_conexion(sistema_rutas: SistemaRutas) -> None:
  print('Digite las dos ubicaciones a eliminar conexion')
  ubicacion1 = input('ubicacion 1: ')
  ubicacion2 = input('ubicacion 2: ')

  sistema_rutas.eliminar_conexion(ubicacion1, ubicacion2)

def camino_mas_corto(sistema_rutas: SistemaRutas) -> None:
  print('Digite las dos ubicaciones a buscar el camino mas corto')
  ubicacion1 = input('ubicacion 1: ')
  ubicacion2 = input('ubicacion 2: ')
  sistema_rutas.camino_mas_corto(ubicacion1, ubicacion2)


def ruta_mas_corta(sistema_rutas: SistemaRutas) -> None:
  sistema_rutas.ruta_mas_corta()


def ver_mapa(sistema_rutas: SistemaRutas) -> None:
  sistema_rutas.ver_mapa()


def menu(sistema_rutas: SistemaRutas, direccion_archivo_sistema_rutas):
  while True:
    imprimir_titulo()
    imprimir_opciones()
    print('\n0. Salir del programa')
    
    opcion = validar_opcion()

    match(opcion):
      case 1:
        agregar_ubicacion(sistema_rutas)

      case 2: 
        agregar_conexion(sistema_rutas)

      case 3: 
        eliminar_ubicacion(sistema_rutas)

      case 4:
        eliminar_conexion(sistema_rutas)

      case 5:
        ver_mapa(sistema_rutas)

      case 6:
        camino_mas_corto(sistema_rutas)

      case 7:
        ruta_mas_corta(sistema_rutas)

      case 0:
        # Guardar estructura del grafo
        sistema_rutas.guardar_rutas(direccion_archivo_sistema_rutas)
        print('Se guardo el sistema de rutas')
        return
      
def main():
  sistema_rutas = SistemaRutas()
  DIRECCION_ARCHIVO_SISTEMA_RUTAS = 'Implementacion/sistema_rutas.pkl'

  # Cargar el sistema de rutas desde un archivo si existe, de lo contrario crear uno nuevo
  try:
      sistema_rutas.cargar_rutas(DIRECCION_ARCHIVO_SISTEMA_RUTAS)
      print("Rutas cargadas desde el archivo.")
  except FileNotFoundError:
      print("Archivo no encontrado. Se ha creado un nuevo sistema de rutas")
  
  menu(sistema_rutas, DIRECCION_ARCHIVO_SISTEMA_RUTAS)

if __name__ == '__main__':
  main()