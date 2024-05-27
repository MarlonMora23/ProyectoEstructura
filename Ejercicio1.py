"""
Implementación de una red social con grafos

Autores:
    Marlon Daniel Mora
    Luis Edward Mosquera
"""
from Implementacion.RedSocial import RedSocial

redSocial = RedSocial(dirigido = False)

# Crear usuarios
MARLON = 'Marlon Mora'
LUIS = 'Luis Edward'
DANIEL = 'Daniel Ruiz'

# Agregar Usuarios
redSocial.agregar_usuario(MARLON)
redSocial.agregar_usuario(LUIS)
redSocial.agregar_usuario(DANIEL)

# Agregar relaciones
redSocial.agregar_relacion(MARLON, LUIS)
redSocial.agregar_relacion(LUIS, DANIEL)

# Mostrar conexiones
redSocial.mostrar_conexiones()

# Verificar si dos usuarios están conectados


# Recorrido en Profundidad (DFS)


# Recorrido en Anchura (BFS)


#  Amigos en Común


# Cantidad de amigos


# Menu


# Representacion gráfica


# Guardar estructura del grafo