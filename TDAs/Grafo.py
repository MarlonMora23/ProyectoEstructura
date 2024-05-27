from TDAs.Cola import Cola

# IMPLEMENTACIÓN DE NODOS Y SUS FUNCIONES
class nodo_arista():
  def __init__(self, info, destino):
    self.info = info
    self.destino = destino
    self.sig = None

class nodo_vertice():
  def __init__(self, info):
    self.info = info
    self.sig = None
    self.visitado = False
    self.adyacentes = Arista()

def adyacentes(vertice: nodo_vertice):
  aux: nodo_arista = vertice.adyacentes.inicio
  while aux is not None:
    print(aux.destino, aux.info)
    aux = aux.sig

def es_adyacente(vertice: nodo_vertice, destino):
  resultado = False
  aux: nodo_arista = vertice.adyacentes.inicio
  while aux is not None and not resultado:
    if aux.destino == destino:
      resultado = True
    aux = aux.sig
  return resultado

# CLASE ARISTA Y SUS FUNCIONES
class Arista():
  def __init__(self):
    self.inicio = None
    self.tamanio = 0

def agregar_arista(origen: Arista, dato, destino):
  nodo = nodo_arista(dato, destino)
  if origen.inicio is None or origen.inicio.destino > destino:
    nodo.sig = origen.inicio
    origen.inicio = nodo
  else:
    ant = origen.inicio
    act = origen.inicio.sig
    while act is not None and act.destino < nodo.destino:
      ant = act
      act = act.sig
    nodo.sig = act
    ant.sig = nodo
  origen.tamanio += 1

def buscar_arista(vertice, clave):
  aux = vertice.adyacentes.inicio
  while aux is not None and aux.destino != clave:
    aux = aux.sig
  return aux

def eliminar_arista(vertice, destino):
  x = None
  if vertice.inicio.destino == destino:
    x = vertice.inicio.info
    vertice.inicio = vertice.inicio.sig
    vertice.tamanio -= 1
  else:
    ant = vertice.inicio
    act = vertice.inicio.sig
    while act is not None and act.destino != destino:
      ant = act
      act = act.sig
    if act is not None:
      x = act.info
      ant.sig = act.sig
      vertice.tamanio -= 1
  return x

# CLASE GRAFO Y SUS MÉTODOS
class Grafo():
  def __init__(self, dirigido=True):
    self.inicio = None
    self.dirigido = dirigido
    self.tamanio = 0

  def insertar_vertice(self, dato):
    nodo = nodo_vertice(dato)
    if self.inicio is None or self.inicio.info > dato:
      nodo.sig = self.inicio
      self.inicio = nodo
    else:
      ant = self.inicio
      act = self.inicio.sig
      while act is not None and act.info < nodo.info:
        ant = act
        act = act.sig
      nodo.sig = act
      ant.sig = nodo
    self.tamanio += 1

  def eliminar_vertice(self, clave):
    x = None
    if self.inicio.info == clave:
      x = self.inicio.info
      self.inicio = self.inicio.sig
      self.tamanio -= 1
    else:
      ant = self.inicio
      act = self.inicio.sig
      while act is not None and act.info != clave:
        ant = act
        act = act.sig
      if act is not None:
        x = act.info
        ant.sig = act.sig
        self.tamanio -= 1
    if x is not None:
      aux = self.inicio
      while aux is not None:
        if aux.adyacentes.inicio is not None:
          eliminar_arista(aux.adyacentes, clave)
        aux = aux.sig
    return x

  def insertar_arista(self, dato, origen: nodo_vertice, destino: nodo_vertice):
    agregar_arista(origen.adyacentes, dato, destino.info)
    if not self.dirigido:
      agregar_arista(destino.adyacentes, dato, origen.info)

  def eliminar_arista(self, vertice, destino):
    eliminar_arista(vertice, destino)

  def buscar_vertice(self, clave):
    aux = self.inicio
    while aux is not None and aux.info != clave:
      aux = aux.sig
    return aux

  def tamanio(self):
    return self.tamanio

  def grafo_vacio(self):
    return self.inicio is None

  def existe_paso(self, origen, destino):
    resultado = False
    if (not origen.visitado):
      origen.visitado = True
      v_adyacentes = origen.adyacentes.inicio
      while v_adyacentes is not None and not resultado:
        adyacente = self.buscarVertice(v_adyacentes.destino)
        if adyacente.info == destino.info:
          return True
        elif not adyacente.visitado:
          resultado = self.existePaso(adyacente, destino)
        v_adyacentes = v_adyacentes.sig
    return resultado

  def marcar_no_visitado(self):
    aux = self.inicio
    while aux is not None:
      aux.visitado = False
      aux = aux.sig

  def barrido_vertices(self):
    aux = self.inicio
    while aux is not None:
      print(aux.info)
      aux = aux.sig

  def barrido_profundidad(self, vertice):
    while vertice is not None:
      if not vertice.visitado:
        vertice.visitado = True
        print(vertice.info)
        adyacentes = vertice.adyacentes.inicio
        while adyacentes is not None:
          adyacente = self.buscarVertice(adyacentes.destino)
          if not adyacente.visitado:
            self.barridoProfundidad(adyacente)
          adyacentes = adyacentes.sig
      vertice = vertice.sig

  def barrido_amplitud(self, vertice):
    cola = Cola()
    while vertice is not None:
      if not vertice.visitado:
        vertice.visitado = True
        cola.arribo(vertice)
        while not cola.colaVacia():
          nodo = cola.atencion()
          print(nodo.info)
          adyacentes = nodo.adyacentes.inicio
          while adyacentes is not None:
            adyacente = self.buscarVertice(adyacentes.destino)
            if not adyacente.visitado:
              adyacente.visitado = True
              cola.arribo(adyacente)
            adyacentes = adyacentes.sig
      vertice = vertice.sig

  def ver_conexiones(self):
      aux = self.inicio
      while aux is not None:
          print(f"Conexiones de {aux.info}:")
          adyacentes(aux)
          aux = aux.sig

if __name__ == '__main__':
    
  grafo = Grafo()
  a = nodo_vertice("A")
  grafo.insertar_vertice(a.info)
  b = nodo_vertice("B")
  grafo.insertar_vertice(b.info)
  d = nodo_vertice("D")
  grafo.insertar_vertice(d.info)
  c = nodo_vertice("C")
  grafo.insertar_vertice(c.info)
  e = nodo_vertice("E")
  grafo.insertar_vertice(e.info)
  f = nodo_vertice("F")
  grafo.insertar_vertice(f.info)

  grafo.insertar_arista(7, a, b)
  grafo.insertar_arista(5, a, d)
  grafo.insertar_arista(5, a, c)
  grafo.insertar_arista(4, b, d)
  grafo.insertar_arista(11, b, e)
  grafo.insertar_arista(6, e, f)
  grafo.insertar_arista(9, c, f)
  grafo.insertar_arista(1, f, d)
  grafo.insertar_arista(18, c, e)
  grafo.insertar_arista(2, d, c)

  adyacentes(a)
  print(es_adyacente(a, "C"))
  print(buscar_arista(a, "B").info)
  a = grafo.buscar_vertice("A")
  print(a.info)
  print(grafo.existe_paso(a, b))

  print("Barrido vertices")
  grafo.barrido_vertices()

  grafo.marcar_no_visitado()
  print("Barrido profundidad")
  grafo.barrido_profundidad(a)
  grafo.marcar_no_visitado()

  print("Barrido amplitud")
  grafo.barrido_amplitud(a)
  grafo.marcar_no_visitado()

  print('grafo')