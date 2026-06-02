transitos = [
['BBJJ77',2], ['CCHH19',3], ['AAFF37',3], ['BBJJ77',1],
['AAFF37',1], ['DDKK33',3], ['AAFF37',1], ['AAFF37',2]
]

def mayor_movilidad(transitos):
   d = {}
   for patente, portico in transitos:
      if patente not in d:
         d[patente] = 0
      d[patente] += 1
   lista = []
   for patente in d:
      lista.append((d[patente],patente))
   lista.sort()
   lista.reverse()
   resultado = []
   for i in range(3):
      veces, patente = lista[i]
      resultado.append([patente,veces])
   return resultado

print(mayor_movilidad(transitos))

def reportar(transitos):
   d = {}
   for patente, portico in transitos:
      if portico not in d:
         d[portico] = []
      if patente not in d[portico]:
         d[portico].append(patente)
         d[portico].sort()
   return d

print(reportar(transitos))
