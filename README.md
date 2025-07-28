Sustencion de cada ejercicio
1.Ejercicio Conceptual de Creación de Dataset de Números de Teléfono de Clientes
Este proyecto es como una fábrica de datos ficticios pero realistas, creada en Python. Su objetivo es generar información "fake" (como nombres, direcciones, teléfonos, etc.) que parezca real, pero sin usar datos de personas verdaderas. Esto es útil para hacer pruebas de software, machine learning o análisis sin riesgo de privacidad.
Luego de generar los datos, el proyecto los valida para asegurarse de que no haya errores, como números de teléfono inválidos o campos vacíos. Todo esto se hace de forma automática, como una cadena de producción bien organizada.
¿Cómo está estructurado?
Imagina que el proyecto es una cocina con diferentes zonas:
generar_dataset.py:
Es el "chef" que prepara los datos. Usa librerías como Faker (que inventa datos convincentes, como direcciones o emails) y pandas (para organizarlos en tablas, como Excel pero más potente).
validar_dataset.py
Es el "control de calidad". Revisa que todo esté correcto:
¿Los teléfonos tienen el formato correcto? (con phonenumbers).
¿Faltan datos? ¿Hay incoherencias?
Limpieza_datos:
Si los datos generados tienen "suciedad" (errores), aquí se procesan para arreglarlos.
requirements.txt
Es la "lista de ingredientes". Le dice a Python qué librerías instalar para que todo funcione (pandas, Faker, etc.).
.github/workflows/pipeline.yml
Es el "robot de la cocina". Automatiza tareas repetitivas, como:
Hacer pruebas cada vez que se sube código.
Verificar que no haya errores antes de publicar cambios.
2.KPI
Este ejercicio conceptual explora la implementación de un Framework de Calidad de Datos, centrado en un "Data Quality Scorecard" o tablero interactivo. El objetivo es monitorear KPIs (Key Performance Indicators) esenciales para evaluar la salud de los datos, demostrando la importancia de la calidad de los datos en el ciclo de vida de la información.
Se propone un tablero interactivo (conceptual) que visualice los siguientes KPIs clave de calidad de datos:
*Integridad: Porcentaje de registros completos frente a registros con valores nulos, indicando la completitud de la información.
*Exactitud: Porcentaje de números de teléfono válidos, verificados mediante expresiones regulares (regex), asegurando que los datos cumplen con un formato esperado.
*Unicidad: Porcentaje de registros duplicados identificados, crucial para evitar redundancias y garantizar la singularidad de las entradas.
*Consistencia: Porcentaje de códigos de país que coinciden con los prefijos telefónicos asociados, verificando la coherencia entre diferentes campos de datos.
*Actualidad: Fecha de la última actualización de los datos, un indicador vital para conocer la frescura y relevancia de la información.
Se ha desarrollado una función en Python para calcular algunas de estas métricas clave, utilizando la librería pandas
completeness: Calcula el porcentaje promedio de valores no nulos en todo el DataFrame. 
uniqueness: Determina el porcentaje de filas únicas en el DataFrame. 
valid_phones: Mide el porcentaje de números de teléfono que cumplen con un patrón de expresión regular que valida el formato (+ opcional seguido de al menos 7 dígitos).
Para el KPI de Consistencia (códigos de país que coinciden con prefijos telefónicos), se propone un script SQL que calcula el porcentaje de números de teléfono válidos por código de país
Este script agrupa los clientes por Codigo_pais y calcula el porcentaje de Numero_Telefono que son considerados válidos (contienen solo dígitos y/o +, y tienen al menos 7 dígitos después de eliminar el +) dentro de cada grupo. 
y en el diagrama de flujo ilustra el flujo conceptual de datos dentro de un sistema que integra la calidad de datos:
Data Sources: Origen de los datos (CSV, APIs, Bases de Datos). 
Data Quality Engine: Componente donde se aplican las reglas y se calculan los KPIs de calidad. 
Data Catalog (Metadata): Almacena los metadatos de los datos y los resultados de calidad. 
Business Intelligence Tools: Herramientas para visualizar los datos de calidad y generar insights de negocio. 
3.Rachas
# Carga de Historial de Saldos desde Excel a SQLite

Este script permite cargar un archivo de Excel con información histórica de saldos por cliente en una base de datos local SQLite. Es útil para transformar archivos planos en datos estructurados y consultables desde SQL.

---

## 📁 Archivos requeridos

- `rachas.xlsx`: Archivo de Excel con la hoja `historia`, que contiene los datos.
- El script de Python (`.py`) que hace la carga.
- Opcional: `rachas.db` se crea automáticamente si no existe.

---

## 📌 Estructura esperada del Excel

La hoja de Excel `historia` debe contener al menos estas columnas:

| identificacion | corte_mes  | saldo   |
|----------------|------------|---------|
| 123456789      | 2024-01-01 | 150000  |
| 987654321      | 2024-02-01 | 200000  |

- `identificacion`: ID del cliente.
- `corte_mes`: Fecha del saldo (una por mes).
- `saldo`: Valor en pesos.

---

## 🚀 ¿Qué hace el script?

1. Verifica que el archivo Excel exista.
2. Crea (si no existe) una base de datos SQLite en la ruta indicada.
3. Crea una tabla `historial_saldos` con tres campos:
   - `identificacion` (texto)
   - `corte_mes` (fecha)
   - `saldo` (número decimal)
4. Lee los datos desde la hoja `historia` del archivo Excel.
5. Convierte la columna `corte_mes` a formato fecha.
6. Inserta los datos en la base de datos.
7. Informa cuántos registros fueron insertados.

---

## 🧠 Código explicativo

```python
import sqlite3
import pandas as pd
from pathlib import Path

# 1. Rutas de los archivos
excel_path = r"C:\Users\natac\OneDrive\Escritorio\rachas.xlsx"
db_path = r"C:\Users\natac\OneDrive\Escritorio\rachas.db"

# 2. Verificar que el Excel exista
if not Path(excel_path).exists():
    raise FileNotFoundError(f"No se encontró el archivo Excel en: {excel_path}")

# 3. Conectarse (o crear) la base de datos SQLite
conn = sqlite3.connect(db_path)

# 4. Crear tabla si no existe
create_table_query = """
CREATE TABLE IF NOT EXISTS historial_saldos (
    identificacion TEXT,
    corte_mes TEXT,
    saldo REAL,
    PRIMARY KEY (identificacion, corte_mes)
)
"""
try:
    conn.execute(create_table_query)
    conn.commit()
    print("Tabla creada exitosamente")
except sqlite3.Error as e:
    print(f"Error al crear la tabla: {str(e)}")

# 5. Leer Excel y cargar a la base de datos
try:
    # Leer hoja 'historia'
    df = pd.read_excel(excel_path, sheet_name='historia')

    # Convertir corte_mes a fecha
    df['corte_mes'] = pd.to_datetime(df['corte_mes'])

    # Insertar en la base de datos
    df.to_sql('historial_saldos', conn, if_exists='append', index=False, 
              dtype={'corte_mes': 'DATETIME'})

    print(f"Datos cargados exitosamente a la base de datos: {db_path}")
    print(f"Total de registros insertados: {len(df)}")

except Exception as e:
    print(f"Error al procesar el archivo Excel: {str(e)}")

finally:
    # Cerrar conexión
    conn.close()
3.1 consultas
Análisis de Clientes por Historial de Saldos y Rachas
Este proyecto contiene una consulta SQL diseñada para identificar y clasificar a los clientes basándose en sus "rachas" (períodos consecutivos) de saldos. En términos simples, nos ayuda a descubrir qué clientes han mantenido un nivel de saldo particular durante un tiempo específico.
¿Qué Buscamos con Esta Consulta?
Imagina que quieres saber:
¿Qué clientes han sido consistentemente "VIP" (con saldos altos) por varios meses seguidos?
¿Cuáles han estado en un rango de saldo "intermedio" durante un período prolongado?
Esta consulta está hecha precisamente para responder a esas preguntas. Su objetivo principal es:
Clasificar los saldos de cada cliente en diferentes categorías o "niveles" (por ejemplo, Nivel 0 para saldos bajos, Nivel 4 para saldos muy altos).
Identificar cuántos meses seguidos un cliente ha permanecido en el mismo nivel de saldo.
Filtrar estas secuencias para encontrar solo las rachas que duran un mínimo de meses que nosotros definimos.
Para cada cliente, elegir la "mejor" racha que cumpla nuestros criterios (generalmente, la más larga y la más reciente).
¿Cómo nos Ayuda Esto?
Entender las rachas de saldos de los clientes es muy útil para:
Marketing: Puedes identificar a tus clientes más valiosos y ofrecerles beneficios exclusivos.
Gestión de Relaciones: Permite detectar cambios en el comportamiento financiero de los clientes, quizás para ofrecerles soporte o nuevos productos.
Análisis Financiero: Ayuda a ver tendencias en los saldos de los clientes a lo largo del tiempo.
¿Qué Necesitas para Usar Esta Consulta?
La consulta está escrita en SQL, y está optimizada para bases de datos como SQLite (a partir de la versión 3.25.0 que soporta funciones de ventana).
Parámetros Configurables:
Antes de ejecutarla, puedes ajustar dos cosas fácilmente al inicio de la consulta:
fecha_base: La fecha hasta la cual quieres que la consulta revise el historial de saldos. Por ejemplo, '2024-12-31'.
n_minimo: El número mínimo de meses consecutivos que debe durar una racha para que la consideremos interesante. Por ejemplo, si pones 3, solo veremos rachas de 3 meses o más.
Resultado Final:
La consulta te devolverá una lista donde para cada cliente (identificacion), verás:
racha: La duración de su racha más relevante (en meses).
fecha_fin: La fecha en que terminó esa racha.
nivel: El nivel de saldo que mantuvieron durante esa racha.


