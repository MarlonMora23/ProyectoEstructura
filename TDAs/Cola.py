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
    nodo_actual = self.frente
    cadena = ''
    vez = 0

    while nodo_actual != None:
      if vez == 0:
        cadena += f'{nodo_actual.dato} < --- Frente de la cola\n'
        vez = 1
      elif nodo_actual.siguiente is None:
        cadena += f'{nodo_actual.dato} < ----- Final de la cola\n'
      else:
        cadena += f'{nodo_actual.dato} \n'
            
      nodo_actual = nodo_actual.siguiente

    print(f'{cadena} \n')

  def cola_vacia(self):
    return self.frente is None
    
  def en_frente(self):
    return self.frente.dato
    
  def obtener_tamano(self):
    return self.tamano
    
  def mover_al_final(self):
    dato = self.atencion()
    self.arribo(dato)
    return dato
    
  def mostrar(self):
    print("Lista de los datos en la cola:")
    nodo_actual = self.frente
    cadena = ""
    vez = 0
    while nodo_actual is not None:
      if vez == 0:
        cadena += f"{nodo_actual.dato} <--- frente de la cola \n"
        vez = 1
      elif nodo_actual.siguiente is None:
        cadena += f"{nodo_actual.dato} <--- final de la cola \n"
      else:
        cadena += f"{nodo_actual.dato} \n"
            
      # Mueve nodo_actual al siguiente nodo en cada iteración
      nodo_actual = nodo_actual.siguiente

    print(cadena)
    print()
