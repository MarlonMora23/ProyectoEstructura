from TDAs.Cola import Cola
import networkx as nx
import matplotlib.pyplot as plt
import pickle

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
  resultado = {}
  while aux is not None:
    resultado[aux.destino] = aux.info
    # print(aux.destino, aux.info)
    aux = aux.sig
  
  return resultado

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
    # Verificar si ya existe una arista entre los vértices
    aux = origen.inicio
    while aux is not None:
        if aux.destino == destino:
            aux.info = dato
            return
        aux = aux.sig
    
    # Si no existe la arista, insertar una nueva
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

  def existe_paso(self, origen: nodo_vertice, destino: nodo_vertice):
    resultado = False
    if (not origen.visitado):
      origen.visitado = True
      v_adyacentes: nodo_arista = origen.adyacentes.inicio
      while v_adyacentes is not None and not resultado:
        adyacente = self.buscar_vertice(v_adyacentes.destino)
        if adyacente.info == destino.info:
          return True
        elif not adyacente.visitado:
          resultado = self.existe_paso(adyacente, destino)
        v_adyacentes = v_adyacentes.sig
    return resultado

  def marcar_no_visitado(self):
    aux = self.inicio
    while aux is not None:
      aux.visitado = False
      aux = aux.sig

  def barrido_vertices(self):
    barrido = []
    aux = self.inicio
    while aux is not None:
      barrido.append(aux.info)
      aux = aux.sig

    return barrido

  def barrido_profundidad(self, vertice: nodo_vertice):
    while vertice is not None:
      if not vertice.visitado:
        vertice.visitado = True
        print(vertice.info.title())
        adyacentes = vertice.adyacentes.inicio
        while adyacentes is not None:
          adyacente = self.buscar_vertice(adyacentes.destino)
          if not adyacente.visitado:
            self.barrido_profundidad(adyacente)
          adyacentes = adyacentes.sig
      vertice = vertice.sig

  def barrido_amplitud(self, vertice: nodo_vertice):
    cola = Cola()
    while vertice is not None:
      if not vertice.visitado:
        vertice.visitado = True
        cola.arribo(vertice)
        while not cola.cola_vacia():
          nodo = cola.atencion()
          print(nodo.info.title())
          adyacentes = nodo.adyacentes.inicio
          while adyacentes is not None:
            adyacente = self.buscar_vertice(adyacentes.destino)
            if not adyacente.visitado:
              adyacente.visitado = True
              cola.arribo(adyacente)
            adyacentes = adyacentes.sig
      vertice = vertice.sig

  def ver_conexiones(self):
    aux = self.inicio
    conexiones = []
    while aux is not None:
        conexiones.append([aux.info, adyacentes(aux)])
        aux = aux.sig

    return conexiones
  
  def visualizar_grafo(self, camino=None) -> None:
    conexiones = self.ver_conexiones()
    G = nx.Graph()
    
    for vertice, adyacentes in conexiones:
        G.add_node(vertice.title())
        for adyacente, peso in adyacentes.items():
            G.add_edge(vertice.title(), adyacente.title(), weight=peso)
    
    pos = nx.spring_layout(G)  # Layout para los nodos

    plt.figure(figsize=(16, 12))
    nx.draw(G, pos, with_labels=True, node_size=4000, node_color='skyblue', font_color='black', edge_color='gray', font_weight='bold')

    # Extraer los pesos de las aristas para mostrarlos
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_weight='bold')

    # Si se desea mostrar un camino
    if camino:
        camino_edges = [(u.title(), v.title()) for u, v in zip(camino, camino[1:])]
        nx.draw_networkx_edges(G, pos, edgelist=camino_edges, edge_color='red', width=2)
    plt.show()

  def vertices_comunes(self, vertice1: nodo_vertice, vertice2: nodo_vertice) -> list:
    vertices_comunes = []

    adyacentes_vertice1 = vertice1.adyacentes.inicio
    adyacentes_vertice2 = vertice2.adyacentes.inicio

    while adyacentes_vertice1 is not None and adyacentes_vertice2 is not None:
      if adyacentes_vertice1.destino == adyacentes_vertice2.destino:
          vertices_comunes.append(adyacentes_vertice1.destino)
          adyacentes_vertice1 = adyacentes_vertice1.sig
          adyacentes_vertice2 = adyacentes_vertice2.sig
      elif adyacentes_vertice1.destino < adyacentes_vertice2.destino:
          adyacentes_vertice1 = adyacentes_vertice1.sig
      else:
          adyacentes_vertice2 = adyacentes_vertice2.sig

    return vertices_comunes
  
  def cantidad_de_conexiones(self, vertice: nodo_vertice) -> int:
    return vertice.adyacentes.tamanio

  def recomendar_vertices(self, vertice: nodo_vertice) -> list:
    vertices_directos = set(adyacentes(vertice))
    posibles_vertices = set()
    
    self.marcar_no_visitado()
    vertice.visitado = True
    
    for directo in vertices_directos:
        vertice_directo = self.buscar_vertice(directo)
        if vertice_directo and not vertice_directo.visitado:
            vertice_directo.visitado = True
            adyacentes_de_directo = adyacentes(vertice_directo)
            for a in adyacentes_de_directo:
                if a != vertice.info and a not in vertices_directos:
                    posibles_vertices.add(a)
    
    return list(posibles_vertices)
  
  def detectar_comunidades(self, tamano_minimo):
    def bron_kerbosch(R: set, P: set, X: set):
        if len(P) == 0 and len(X) == 0 and len(R) >= tamano_minimo:
            cliques.append(R)
        while P:
            v = P.pop()
            vecinos = set(adyacentes(self.buscar_vertice(v)))
            bron_kerbosch(R.union([v]), P.intersection(vecinos), X.intersection(vecinos))
            X.add(v)

    cliques = []
    P = set()
    aux = self.inicio
    while aux is not None:
        P.add(aux.info)
        aux = aux.sig
    
    bron_kerbosch(set(), P, set())
    return cliques
  
  def es_conexo(self):
    def dfs(vertice, visitados):
        visitados.add(vertice.info)
        adyacentes = vertice.adyacentes.inicio
        while adyacentes is not None:
            adyacente = self.buscar_vertice(adyacentes.destino)
            if adyacente.info not in visitados:
                dfs(adyacente, visitados)
            adyacentes = adyacentes.sig
    
    # Empezar desde el primer vértice
    if self.inicio is None:
        return True  # Un grafo vacío puede considerarse conexo
    
    visitados = set()
    dfs(self.inicio, visitados)
    
    # Verificar si todos los vértices han sido visitados
    aux = self.inicio
    while aux is not None:
        if aux.info not in visitados:
            return False
        aux = aux.sig
    
    return True

  def vertice_con_mas_conexiones(self):
      if self.inicio is None:
          return None  
      
      max_conexiones = -1
      vertice_max_conexiones = None
      
      aux = self.inicio
      while aux is not None:
          num_conexiones = self.cantidad_de_conexiones(aux)
          if num_conexiones > max_conexiones:
              max_conexiones = num_conexiones
              vertice_max_conexiones = aux.info
          aux = aux.sig
      
      return vertice_max_conexiones, max_conexiones
  
  def vertice_con_menos_conexiones(self):
      if self.inicio is None:
          return None  
      
      min_conexiones = float('inf')
      vertice_min_conexiones = None
      
      aux = self.inicio
      while aux is not None:
          num_conexiones = self.cantidad_de_conexiones(aux)
          if num_conexiones < min_conexiones:
              min_conexiones = num_conexiones
              vertice_min_conexiones = aux.info
          aux = aux.sig
      
      return vertice_min_conexiones, min_conexiones

  def guardar_grafo(self, direccion_archivo):
        with open(direccion_archivo, 'wb') as file:
            pickle.dump(self, file)

  @staticmethod
  def cargar_grafo(direccion_archivo):
      with open(direccion_archivo, 'rb') as file:
          return pickle.load(file)

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
  resultado = grafo.barrido_vertices()
  print(resultado)

  grafo.marcar_no_visitado()
  print("Barrido profundidad")
  grafo.barrido_profundidad(a)
  grafo.marcar_no_visitado()

  print("Barrido amplitud")
  grafo.barrido_amplitud(a)
  grafo.marcar_no_visitado()

  print('grafo')