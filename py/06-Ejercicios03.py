recetas = [
    ["Pizza Margarita", 30, ["queso", "tomate", "harina", "orégano"]],
    ["Hamburguesa", 25, ["carne", "queso", "tomate", "pan"]],
    ["Ensalada César", 15, ["lechuga", "queso", "pollo", "pan"]],
    ["Tacos", 20, ["carne", "tomate", "lechuga", "queso"]],
    ["Pasta Alfredo", 35, ["pasta", "queso", "crema", "pollo"]],
    ["Sándwich de Pollo", 10, ["pollo", "pan", "tomate", "lechuga"]],
    ["Lasaña", 50, ["carne", "queso", "tomate", "pasta"]],
    ["Omelette", 8, ["huevo", "queso", "tomate"]],
    ["Empanadas", 40, ["carne", "cebolla", "harina"]],
    ["Sopa de Verduras", 30, ["zanahoria", "cebolla", "tomate", "papa"]]
]

def platos_con_ingrediente(recetas, ingrediente):
   lista = []
   for plato, tiempo, ings in recetas:
      if ingrediente in ings:
         lista.append([tiempo, plato])
   lista.sort()
   resultado = []
   for elemento in lista[:3]:
      resultado.append(elemento[1])
   return resultado

print(platos_con_ingrediente(recetas, 'tomate'))
print(platos_con_ingrediente(recetas, 'zanahoria'))
print(platos_con_ingrediente(recetas, 'pepino'))

def ingredientes_mas_usados(recetas):
   ingredientes = []
   veces = []
   for plato, tiempo, ings in recetas:
      for ing in ings:
         if ing not in ingredientes:
            ingredientes.append(ing)
            veces.append(0)
         i = ingredientes.index(ing)
         veces[i] += 1
   lista = []
   i = 0
   while i < len(ingredientes):
      lista.append([veces[i], ingredientes[i]])
      i += 1
   lista.sort()
   lista.reverse()
   resultado = []
   for elemento in lista[:3]:
      resultado.append(elemento[1])
   return resultado

print(ingredientes_mas_usados(recetas))
