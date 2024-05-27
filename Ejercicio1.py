"""
Implementación de una red social con grafos

Autores:
    Marlon Daniel Mora
    Luis Edward Mosquera
"""
from Implementacion.RedSocial import RedSocial

redSocial = RedSocial(dirigido = False)

# Crear usuarios
redSocial.agregarUsuario('Marlon Mora')
redSocial.agregarUsuario('Luis Edward')
redSocial.agregarUsuario('Daniel Ruiz')

# Agregar relaciones
redSocial.agregarRelacion('Marlon Mor=a', 'Luis Edward')

# Mostrar conexiones
redSocial.mostrarConexiones()
