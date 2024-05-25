from TDAs.Nodo import Nodo

class Cola():
  def __init__(self) -> None:
    self.frente, self.final = None, None
    self.tamano = 0

  def arribo(self, dato) -> None:
    nodo = Nodo(dato)

    if self.frente is None:
      self.frente = nodo 
    else:
      self.final.siguiente = nodo
      
    self.final = nodo
    self.tamano += 1

  def atencion(self):
    if self.frente is None:
      return None
      
    dato = self.frente.dato
    self.frente = self.frente.siguiente

    if self.frente is None:
      self.final = None

    self.tamano -= 1

    return dato
    
  def mostrar(self):
    nodoActual = self.frente
    cadena = ''
    vez = 0

    while nodoActual != None:
      if vez == 0:
        cadena += f'{nodoActual.dato} < --- Frente de la cola\n'
        vez = 1
      elif nodoActual.siguiente is None:
        cadena += f'{nodoActual.dato} < ----- Final de la cola\n'
      else:
        cadena += f'{nodoActual.dato} \n'
            
      nodoActual = nodoActual.siguiente

    print(f'{cadena} \n')

  def colaVacia(self):
    return self.frente is None
    
  def enFrente(self):
    return self.frente.dato
    
  def obtenerTamano(self):
    return self.tamano
    
  def moverAlFinal(self):
    dato = self.atencion()
    self.arribo(dato)
    return dato
    
  def mostrar(self):
    print("Lista de los datos en la cola:")
    nodoActual = self.frente
    cadena = ""
    vez = 0
    while nodoActual is not None:
      if vez == 0:
        cadena += f"{nodoActual.dato} <--- frente de la cola \n"
        vez = 1
      elif nodoActual.siguiente is None:
        cadena += f"{nodoActual.dato} <--- final de la cola \n"
      else:
        cadena += f"{nodoActual.dato} \n"
            
      # Mueve nodoActual al siguiente nodo en cada iteración
      nodoActual = nodoActual.siguiente

    print(cadena)
    print()
