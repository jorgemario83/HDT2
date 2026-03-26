# ============================================================
#  HDT2 — Parte 3: *args, **kwargs y Composición  (25 pts)
#  CineData GT 2026 — Sistema de Análisis de Cines
# ============================================================

# ============================================================
#  Ejercicio 3.1 — Funciones con *args  (8 pts)
# ============================================================
# a) Implementa `ingreso_total(*montos)` que reciba cualquier cantidad
#    de montos numéricos y RETORNE la suma de todos.
#    SIN usar sum(). Usa un ciclo for.
#
# b) Implementa `mejor_sala(*salas)` que reciba cualquier cantidad de
#    tuplas (nombre_sala, ventas). RETORNE la tupla con más ventas.
#    SIN usar max().
#    Si no recibe argumentos, retorna ("N/A", 0).
#
# c) Implementa `reporte_multisala(titulo, *funciones)` donde:
#    - titulo (str): título del reporte
#    - *funciones: cada argumento es una tupla (nombre, precio, vendidas, descuento)
#    Para cada función calcula:
#      ingreso = precio * vendidas * (1 - descuento/100)
#    RETORNA un string multilínea con el reporte y el total.
#    (Ver formato en salida esperada)

def ingreso_total(*montos):
    total = 0
    # *montos se comporta como una tupla, así que podemos iterar sobre ella
    for monto in montos:
        total += monto
    return total


def mejor_sala(*salas):
    # Si la tupla está vacía (no mandaron argumentos), retornamos el default
    if not salas:
        return ("N/A", 0)
        
    max_ventas = -1
    mejor = ("N/A", 0)
    
    for sala in salas:
        # sala[1] tiene el número de ventas
        if sala[1] > max_ventas:
            max_ventas = sala[1]
            mejor = sala
            
    return mejor


def reporte_multisala(titulo, *funciones):
    reporte = f"=== {titulo} ===\n"
    total_general = 0
    contador = 1
    
    for nombre, precio, vendidas, descuento in funciones:
        ingreso = precio * vendidas * (1 - descuento/100)
        # Alineamos el nombre a 14 caracteres y el ingreso a 2 decimales
        reporte += f"Función {contador}: {nombre:<14} | Q{ingreso:.2f}\n"
        total_general += ingreso
        contador += 1
        
    reporte += "---\n"
    reporte += f"TOTAL: Q{total_general:.2f}"
    return reporte


# --- Pruebas (NO modificar) ---
print("=== Ejercicio 3.1 ===")
print(f"Ingreso total: Q{ingreso_total(1500.0, 2300.0, 800.0, 4100.0)}")
print(f"Ingreso vacío: Q{ingreso_total()}")

print(f"Mejor: {mejor_sala(('IMAX', 340), ('3D', 280), ('Kids', 180), ('Premium', 310))}")
print(f"Mejor vacío: {mejor_sala()}")

print()
print(reporte_multisala("Sala IMAX — Sábado",
                        ("Dune 2PM", 85.0, 150, 0),
                        ("Dune 5PM", 85.0, 200, 10),
                        ("Dune 8PM", 95.0, 180, 5)))

# Salida esperada:
# === Ejercicio 3.1 ===
# Ingreso total: Q8700.0
# Ingreso vacío: Q0
# Mejor: ('IMAX', 340)
# Mejor vacío: ('N/A', 0)
#
# === Sala IMAX — Sábado ===
# Función 1: Dune 2PM       | Q12750.00
# Función 2: Dune 5PM       | Q15300.00
# Función 3: Dune 8PM       | Q16245.00
# ---
# TOTAL: Q44295.00


# ============================================================
#  Ejercicio 3.2 — Funciones con **kwargs  (8 pts)
# ============================================================
# Implementa `ficha_pelicula(titulo, duracion, rating, **extras)` que
# RETORNE un string multilínea con la ficha de la película:
#
# Parámetros fijos: titulo, duracion (min), rating (float)
# **extras puede incluir: director, genero, año, idioma, pais, etc.
#
# Formato del string retornado:
# ┌──────────────────────────────┐
# │ TÍTULO                       │
# ├──────────────────────────────┤
# │ Duración: 175 min            │
# │ Rating  : ★ 8.7              │
# │ director: Villeneuve         │  ← Solo si hay extras
# │ genero  : Sci-Fi             │
# │ ...                          │
# └──────────────────────────────┘
#
# Ancho total del cuadro: 35 caracteres (contando bordes).
# El título va centrado. Las líneas de datos van alineadas a la izquierda.
# Cada clave de **extras se muestra capitalizada.

def ficha_pelicula(titulo, duracion, rating, **extras):
    # Dibujamos las líneas fijas del cuadro
    linea_techo = "┌" + ("─" * 33) + "┐\n"
    linea_div = "├" + ("─" * 33) + "┤\n"
    
    # {titulo:^31} centra el texto en un espacio de 31 caracteres
    linea_titulo = f"│ {titulo:^31} │\n"
    
    # Preparamos las líneas fijas obligatorias asegurando que la etiqueta mida 8 chars
    duracion_texto = f"{'Duración':<8} : {duracion} min"
    rating_texto = f"{'Rating':<8} : ★ {rating}"
    
    reporte = linea_techo + linea_titulo + linea_div
    reporte += f"│ {duracion_texto:<31} │\n"
    reporte += f"│ {rating_texto:<31} │\n"
    
    # Procesamos los argumentos dinámicos iterando sobre el diccionario extras
    for clave, valor in extras.items():
        # Capitalizamos la clave y la forzamos a ocupar 8 espacios para alinear los ":"
        clave_fmt = f"{clave.capitalize():<8}"
        linea_extra = f"{clave_fmt} : {valor}"
        reporte += f"│ {linea_extra:<31} │\n"
        
    reporte += "└" + ("─" * 33) + "┘"
    return reporte


# --- Pruebas (NO modificar) ---
print("\n=== Ejercicio 3.2 ===")
print(ficha_pelicula("Dune: Parte 3", 175, 8.7,
                     director="Villeneuve", genero="Sci-Fi", año=2026))

print(ficha_pelicula("Inside Out 3", 105, 8.9))

# Salida esperada:
# === Ejercicio 3.2 ===
# ┌─────────────────────────────────┐
# │         Dune: Parte 3           │
# ├─────────────────────────────────┤
# │ Duración : 175 min              │
# │ Rating   : ★ 8.7                │
# │ Director : Villeneuve           │
# │ Genero   : Sci-Fi               │
# │ Año      : 2026                 │
# └─────────────────────────────────┘
# ┌─────────────────────────────────┐
# │          Inside Out 3           │
# ├─────────────────────────────────┤
# │ Duración : 105 min              │
# │ Rating   : ★ 8.9                │
# └─────────────────────────────────┘


# ============================================================
#  Ejercicio 3.3 — Composición de Funciones  (9 pts)
# ============================================================
# Aquí vas a construir un pipeline de análisis usando composición:
# cada función usa las anteriores como building blocks.
#
# a) `calcular_totales(ventas_por_sala)` — recibe un diccionario
#    {nombre_sala: [ventas_lun, ..., ventas_dom]}.
#    RETORNA una lista de tuplas [(nombre, total), ...].
#    Para sumar cada lista, usa `ingreso_total(*lista)` del ejercicio 3.1.
#
# b) `ordenar_salas(lista_tuplas)` — recibe una lista de tuplas (nombre, valor).
#    RETORNA una nueva lista ordenada de MAYOR a MENOR por valor.
#    Implementa ordenamiento burbuja. SIN usar sorted() ni .sort().
#
# c) `tendencia(valores)` — recibe una lista de números.
#    RETORNA: "ascendente" si cada valor >= anterior,
#             "descendente" si cada valor <= anterior,
#             "irregular" en otro caso.
#
# d) `reporte_semanal(nombre_cine, ventas_por_sala)` — función principal.
#    Usa calcular_totales, ordenar_salas, mejor_sala (3.1), y tendencia.
#    RETORNA un string con el reporte completo (ver formato abajo).
#    Para el promedio semanal de cada sala, divide total / 7.

def calcular_totales(ventas_por_sala):
    lista_totales = []
    # Iteramos sobre el diccionario (clave, valor)
    for sala, ventas in ventas_por_sala.items():
        # Usamos el operador * para "desempaquetar" la lista y mandarla como args
        total = ingreso_total(*ventas)
        lista_totales.append((sala, total))
    return lista_totales


def ordenar_salas(lista_tuplas):
    # Hacemos una copia de la lista para no modificar la original (Buena práctica)
    copia = lista_tuplas[:]
    
    # Averiguamos el tamaño sin usar len()
    n = 0
    for _ in copia:
        n += 1
        
    # Algoritmo de Ordenamiento Burbuja (Bubble Sort) descendente
    for i in range(n):
        for j in range(0, n - i - 1):
            # Comparamos el valor de las ventas en [j][1]
            if copia[j][1] < copia[j + 1][1]:
                copia[j], copia[j + 1] = copia[j + 1], copia[j]
                
    return copia


def tendencia(valores):
    if not valores:
        return "irregular"
        
    n = 0
    for _ in valores:
        n += 1
        
    es_asc = True
    es_desc = True
    
    # Comparamos cada elemento con el siguiente
    for i in range(n - 1):
        if valores[i] > valores[i+1]:
            es_asc = False
        if valores[i] < valores[i+1]:
            es_desc = False
            
    if es_asc:
        return "ascendente"
    elif es_desc:
        return "descendente"
    else:
        return "irregular"


def reporte_semanal(nombre_cine, ventas_por_sala):
    reporte = f"=== REPORTE SEMANAL: {nombre_cine} ===\n"
    
    # Usamos composición llamando a las funciones de arriba
    totales = calcular_totales(ventas_por_sala)
    salas_ordenadas = ordenar_salas(totales)
    
    contador = 1
    for sala, total in salas_ordenadas:
        promedio = total / 7
        tend = tendencia(ventas_por_sala[sala])
        
        # Formateamos cada columna: nombre(10), total(4), promedio(6 con 2 decimales)
        reporte += f"#{contador} {sala:<10} | Total: {total:>4} | Prom: {promedio:>6.2f} | Tendencia: {tend}\n"
        contador += 1
        
    # Para encontrar la mejor sala, desempaquetamos la lista ya ordenada
    mejor = mejor_sala(*salas_ordenadas)
    reporte += "---\n"
    reporte += f"Mejor sala de la semana: {mejor[0]} ({mejor[1]} entradas)"
    
    return reporte


# --- Pruebas (NO modificar) ---
print("\n=== Ejercicio 3.3 ===")

ventas = {
    "IMAX":     [120, 135, 140, 155, 200, 310, 280],
    "Sala 3D":  [200, 180, 160, 150, 140, 130, 110],
    "Kids":     [90, 95, 100, 105, 110, 115, 120],
    "Premium":  [100, 80, 95, 105, 170, 300, 250],
}

print(reporte_semanal("CineData Plaza", ventas))

# Salida esperada:
# === Ejercicio 3.3 ===
# === REPORTE SEMANAL: CineData Plaza ===
# #1 IMAX       | Total: 1340 | Prom: 191.43 | Tendencia: irregular
# #2 Premium    | Total: 1100 | Prom: 157.14 | Tendencia: irregular
# #3 Sala 3D    | Total: 1070 | Prom: 152.86 | Tendencia: descendente
# #4 Kids       | Total:  735 | Prom: 105.00 | Tendencia: ascendente
# ---
# Mejor sala de la semana: IMAX (1340 entradas)
