from TDAs.Cola import Cola

# IMPLEMENTACIÓN DE NODOS Y SUS FUNCIONES
class nodoArista():
  def __init__(self, info, destino):
    self.info = info
    self.destino = destino
    self.sig = None

class nodoVertice():
  def __init__(self, info):
    self.info = info
    self.sig = None
    self.visitado = False
    self.adyacentes = Arista()

def adyacentes(vertice):
  aux = vertice.adyacentes.inicio
  while aux is not None:
    print(aux.destino, aux.info)
    aux = aux.sig

def esAdyacente(vertice, destino):
  resultado = False
  aux = vertice.adyacentes.inicio
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

def agregarArista(origen, dato, destino):
  nodo = nodoArista(dato, destino)
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

def buscarArista(vertice, clave):
  aux = vertice.adyacentes.inicio
  while aux is not None and aux.destino != clave:
    aux = aux.sig
  return aux

def eliminarArista(vertice, destino):
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

  def insertarVertice(self, dato):
    nodo = nodoVertice(dato)
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

  def insertarArista(self, dato, origen, destino):
    agregarArista(origen.adyacentes, dato, destino.info)
    if not self.dirigido:
      agregarArista(destino.adyacentes, dato, origen.info)

  def eliminarVertice(self, clave):
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
          eliminarArista(aux.adyacentes, clave)
        aux = aux.sig
    return x

  def buscarVertice(self, clave):
    aux = self.inicio
    while aux is not None and aux.info != clave:
      aux = aux.sig
    return aux

  def tamanio(self):
    return self.tamanio

  def grafoVacio(self):
    return self.inicio is None

  def existePaso(self, origen, destino):
    resultado = False
    if (not origen.visitado):
      origen.visitado = True
      vAdyacentes = origen.adyacentes.inicio
      while vAdyacentes is not None and not resultado:
        adyacente = self.buscarVertice(vAdyacentes.destino)
        if adyacente.info == destino.info:
          return True
        elif not adyacente.visitado:
          resultado = self.existePaso(adyacente, destino)
        vAdyacentes = vAdyacentes.sig
    return resultado

  def marcarNoVisitado(self):
    aux = self.inicio
    while aux is not None:
      aux.visitado = False
      aux = aux.sig

  def barridoVertices(self):
    aux = self.inicio
    while aux is not None:
      print(aux.info)
      aux = aux.sig

  def barridoProfundidad(self, vertice):
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

  def barridoAmplitud(self, vertice):
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

if __name__ == '__main__':
    
  grafo = Grafo()
  a = nodoVertice("A")
  grafo.insertarVertice(a.info)
  b = nodoVertice("B")
  grafo.insertarVertice(b.info)
  d = nodoVertice("D")
  grafo.insertarVertice(d.info)
  c = nodoVertice("C")
  grafo.insertarVertice(c.info)
  e = nodoVertice("E")
  grafo.insertarVertice(e.info)
  f = nodoVertice("F")
  grafo.insertarVertice(f.info)

  grafo.insertarArista(7, a, b)
  grafo.insertarArista(5, a, d)
  grafo.insertarArista(5, a, c)
  grafo.insertarArista(4, b, d)
  grafo.insertarArista(11, b, e)
  grafo.insertarArista(6, e, f)
  grafo.insertarArista(9, c, f)
  grafo.insertarArista(1, f, d)
  grafo.insertarArista(18, c, e)
  grafo.insertarArista(2, d, c)

  adyacentes(a)
  print(esAdyacente(a, "C"))
  print(buscarArista(a, "B").info)
  a = grafo.buscarVertice("A")
  print(a.info)
  print(grafo.existePaso(a, b))

  print("Barrido vertices")
  grafo.barridoVertices()

  grafo.marcarNoVisitado()
  print("Barrido profundidad")
  grafo.barridoProfundidad(a)
  grafo.marcarNoVisitado()

  print("Barrido amplitud")
  grafo.barridoAmplitud(a)
  grafo.marcarNoVisitado()

  print('grafo')