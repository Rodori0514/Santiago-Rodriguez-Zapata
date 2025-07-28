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

