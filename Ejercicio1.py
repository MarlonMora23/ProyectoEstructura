"""
Implementación de una red social con grafos

Autores:
    Marlon Daniel Mora
    Luis Edward Mosquera
"""
from Implementacion.RedSocial import RedSocial

red_social = RedSocial(dirigido = False)

# Crear usuarios
MARLON = 'Marlon Mora'
LUIS = 'Luis Edward'
DANIEL = 'Daniel Ruiz'
IAN = 'Ian Arango'
JHONATAN = 'Jhonatan Velazco'

# Agregar Usuarios
red_social.agregar_usuario(MARLON)
red_social.agregar_usuario(LUIS)
red_social.agregar_usuario(DANIEL)
red_social.agregar_usuario(IAN)
red_social.agregar_usuario(JHONATAN)

# Agregar relaciones
red_social.agregar_relacion(MARLON, LUIS)
red_social.agregar_relacion(LUIS, DANIEL)
red_social.agregar_relacion(MARLON, IAN)
red_social.agregar_relacion(IAN, DANIEL)

# Mostrar conexiones
red_social.mostrar_conexiones()

# Verificar si dos usuarios están conectados
red_social.usuarios_estan_relacionados(MARLON, DANIEL)
red_social.usuarios_estan_relacionados(MARLON, IAN)

# Recorrido en Profundidad (DFS)
red_social.recorrido_en_profundidad(LUIS)

# Recorrido en Anchura (BFS)
red_social.recorrido_en_anchura(MARLON)

#  Amigos en Común
red_social.amigos_en_comun(MARLON, DANIEL)

# Cantidad de amigos


# Recomendaciones de amigos


# Detectar comunidades


# Verificar conectividad


# Grado de conexion


# Menu


# Representacion gráfica


# Guardar estructura del grafo