"""
Implementación de una red social con grafos

Autores:
    Marlon Daniel Mora
    Luis Edward Mosquera
"""
from Implementacion.RedSocial import RedSocial

redSocial = RedSocial(dirigido = False)

# Crear usuarios
redSocial.agregar_usuario('Marlon Mora')
redSocial.agregar_usuario('Luis Edward')
redSocial.agregar_usuario('Daniel Ruiz')

# Agregar relaciones
redSocial.agregar_relacion('Marlon Mora', 'Luis Edward')
redSocial.agregar_relacion('Luis Edward', 'Daniel Ruiz')

# Mostrar conexiones
redSocial.mostrar_conexiones()
