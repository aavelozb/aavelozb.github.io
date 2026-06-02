series = [
   ['Game of thrones','USA',9.4,['ficcion']],
   ['24','USA',8.4,['accion','suspenso']],
   ['La casa de papel','España',9.2,['accion','suspenso','drama']],
   ['Orange is the new black', 'USA', 8.5, ['comedia','drama']],
	['Dark', 'Alemania', 9.2, ['ficcion','drama']],
   ['Sherlock','UK',9.2,['policial','drama','suspenso']],
   ['Merlí','España',9.5,['drama']],
   ['Whitecollar','USA',8.2,['comedia','drama','suspenso']],
   ['Heroes','USA',7.7,['ficcion','accion']],
   ['Mistfit','UK',8.4,['accion','drama','ficcion']]
   # ...
]

def series_x_genero(series):
   d = {}
   for titulo, _, _, generos in series:
      for genero in generos:
         if genero not in d:
            d[genero] = []
         d[genero].append(titulo)

   lista = []
   for genero in d:
      d[genero].sort()
      mini_lista = [genero, d[genero]]
      lista.append(mini_lista)
   lista.sort()
   return lista

print(series_x_genero(series))

def paises_con_mas_series(series):
   d = {}
   for _, pais, _, _ in series:
      if pais not in d:
         d[pais] = 0
      d[pais] += 1

   lista = []
   for pais in d:
      mini_lista = [d[pais], pais]
      lista.append(mini_lista)
   lista.sort()
   lista.reverse()

   resultado = []
   for _, pais in lista[:3]:
      resultado.append(pais)
   return resultado

print(paises_con_mas_series(series))
