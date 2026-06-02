estaciones = [
   'Estacion Central' ,
   'Puente Sal y Santo' ,
   'Pytronato' ,
   'La Pysterna' ,
   'Pynstein' ,
   'Estadio Nacional' ,
   'Pio-Pio' ,
   'Plaza Python Alto'   # ...
]

tipos = {
   'Expreso': ['E07','F07','F08', ...],
   'Normal' : ['G00','H00', ...],
   'Corto'  : ['B00','C01', ...]
}

trenes = {
   'E07':[9,3],'F07':[10,14],'H00':[9,23], 'B00':[8,0],
   'G00':[8,46],'C01':[13,59],'F08':[11,2]   # ...
}

# Retorna el tiempo entre estaciones para un tren particular, según su id
def tiempo_entre_estaciones(tipos, id):
   for tipo in tipos:
      if id in tipos[tipo]:
         if tipo=='Expreso':
             return 2
         elif tipo=='Normal':
             return 5
         return 7

# Dada una hora particular [hh,mm] le suma una cantidad de minutos
# y retorna la hora resultante como una lista [h,m]
def sumar_minutos(actual, cantidad):
   hh, mm = actual
   min = hh*60+mm+cantidad
   hres = (min//60)%24
   mres = min%60
   return [hres,mres]

# Determina la cantidad de minutos entre dos horas en formato [h,m]
def restar(grande, chica):
   hh_g, mm_g = grande
   hh_c, mm_c = chica
   min = (hh_g*60+mm_g-hh_c*60-mm_c)
   return min

def proximos_trenes(estaciones, tipos, trenes, estacion_actual, hora_actual):
    resultado = {}
    indice_estacion = estaciones.index(estacion_actual)
    hora_actual, minutos_actuales = hora_actual
    for id_tren in trenes:
        h_salida, m_salida = trenes[id_tren]
        hora_salida = [h_salida, m_salida]
        minutos_en_llegar = indice_estacion * tiempo_entre_estaciones(tipos, id_tren)
        h_llegada, m_llegada = sumar_minutos(hora_salida, minutos_en_llegar)
        if [h_llegada, m_llegada] >= [hora_actual, minutos_actuales]:
           resultado[id_tren] = restar([h_llegada, m_llegada], [hora_actual, minutos_actuales])
    return resultado

print(proximos_trenes(estaciones, tipos, trenes, 'Pytronato', [9,6]))
print(proximos_trenes(estaciones, tipos, trenes, 'Pio-Pio', [11,0]))
print(proximos_trenes(estaciones, tipos, trenes, 'Puente Sal y Santo', [15,00]))
