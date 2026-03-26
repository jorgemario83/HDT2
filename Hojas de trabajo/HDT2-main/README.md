# Hoja de Trabajo 2 — Fundamentos de Programación
## CineData GT 2026: Sistema de Análisis de Cines

**Asignatura:** Fundamentos de Programación — Sección C
**Universidad:** Francisco Marroquín
**Valor:** 5 puntos sobre la nota final
**Entrega:** Jueves 9 de abril de 2026 antes de las 8:30 AM
**Modalidad:** Individual

---

## Contexto

**CineData GT** es la empresa líder en análisis de datos para la industria cinematográfica guatemalteca. Manejan información de salas, películas, ventas y tendencias para la cadena de cines más grande del país.

El equipo de datos necesita que completes varios módulos de su sistema de análisis. Tu misión: implementar las funciones que faltan en cada archivo `.py`.

> Cada archivo contiene variables de prueba, firmas de funciones y comentarios `# TODO`.
> **No cambies** los nombres de las variables, funciones o parámetros ya definidos.

---

## Reglas

1. **Solo Python estándar**: no importes librerías externas (pandas, numpy, etc.)
2. **Restricciones por ejercicio**: donde dice "SIN usar X", respétalo
3. **Todo debe estar en funciones `def`**: nada de lógica suelta fuera de funciones (excepto las pruebas ya escritas)
4. **`return`, no `print`**: todas las funciones deben RETORNAR sus resultados, a menos que se indique lo contrario
5. **El código debe ejecutarse sin errores**: archivo que no corre = 0 en ese archivo
6. **Verifica los casos de prueba**: cada ejercicio incluye el output esperado en comentarios

---

## Estructura y Puntos

| Archivo                       | Tema                                      | Puntos |
|-------------------------------|-------------------------------------------|--------|
| `parte1_basicas.py`           | Funciones básicas, parámetros y return     | 20 pts |
| `parte2_default_kwargs.py`    | Parámetros default, keyword args           | 20 pts |
| `parte3_args_composicion.py`  | *args, **kwargs y composición              | 25 pts |
| `parte4_scope_modularidad.py` | Scope, diseño modular y reutilización      | 20 pts |
| `parte5_integrador.py`        | Integrador: sistema completo con funciones | 15 pts |
| **Total**                     |                                            | **100 pts** |

---

## Rúbrica de Calificación

| Criterio        | Descripción                                               |
|-----------------|-----------------------------------------------------------|
| Correctitud     | El código produce los outputs esperados                   |
| Modularidad     | Las funciones están bien diseñadas (parámetros, return)   |
| Sin errores     | El archivo corre sin excepciones                          |
| Restricciones   | Se respetan los `SIN usar X` de cada ejercicio            |

**Penalizaciones:**
- Archivo que no corre: −5 pts sobre ese archivo
- Usar función/estructura prohibida: −2 pts por instancia
- Modificar variables de prueba ya definidas: −3 pts por instancia
- Función que usa `print` en lugar de `return` (cuando se pide `return`): −2 pts por instancia

---

## Cómo Entregar

1. Haz **fork** de este repositorio en tu cuenta de GitHub
2. Trabaja en los archivos `.py` dentro de la carpeta `HojasDeTrabajo/HDT2/`
3. Antes de entregar, verifica que cada archivo corra sin errores:
   ```bash
   python parte1_basicas.py
   python parte2_default_kwargs.py
   python parte3_args_composicion.py
   python parte4_scope_modularidad.py
   python parte5_integrador.py
   ```
4. En tu fork en GitHub, usa **Add file → Upload files** y sube los archivos `.py` actualizados
5. Verifica **dos veces** que estás subiendo a **tu fork** (tu usuario) y no al repositorio original

---

*CineData GT 2026 — Fundamentos de Programación, Sección C — UFM*
