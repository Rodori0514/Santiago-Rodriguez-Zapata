mi nombre es Santiago Rodriguez y estoy emocionado de compartir este proyecto demuestran mi pasión y habilidades en el manejo de datos, el desarrollo de herramientas y la optimización de procesos. Cada uno de estos ejercicios representa un desafío que abordé con curiosidad y dedicación, buscando siempre soluciones eficientes y robustas.
Estos proyectos no solo muestran mis capacidades técnicas en Python, SQL y manipulación de datos, sino también mi enfoque en la calidad, la eficiencia y la resolución de problemas reales.

1. Ejercicio Conceptual: Creación y Validación de un Dataset de Números de Teléfono de Clientes
Imagina que necesitamos datos para probar un nuevo software o un modelo de aprendizaje automático, pero no podemos usar información real para proteger la privacidad. Este proyecto es mi solución para ese dilema: una fábrica de datos ficticios, pero sorprendentemente realistas, construida en Python.
¿Qué hace?
Genera datos "fake": Crea información como nombres, direcciones y números de teléfono que parecen auténticos, sin usar datos de personas reales. Es perfecto para entornos de prueba, desarrollo o análisis sin riesgos de privacidad.
Valida la información: Después de generar los datos, el proyecto los revisa automáticamente para asegurarse de que no haya errores, como números de teléfono inválidos o campos vacíos. Es como un control de calidad automático que garantiza la fiabilidad de los datos.
¿Cómo está organizado?
Piensa en este proyecto como una cocina bien organizada con diferentes secciones:
generar_dataset.py: Este es el "chef" principal. Utiliza librerías como Faker para inventar datos convincentes y pandas para organizarlos de manera estructurada, como si fuera una hoja de cálculo muy potente.
validar_dataset.py: Es nuestro "control de calidad". Se encarga de revisar que todo esté en orden: ¿Los teléfonos tienen el formato correcto? ¿Faltan datos? ¿Hay alguna inconsistencia?
Limpieza_datos: Si los datos generados tienen algún "desorden" o error, aquí se procesan para corregirlos y dejarlos impecables.
requirements.txt: Esta es nuestra "lista de ingredientes". Indica qué librerías de Python necesitas instalar para que el proyecto funcione perfectamente (por ejemplo, pandas, Faker).
.github/workflows/pipeline.yml: Este es el "robot de la cocina". Automatiza tareas repetitivas, como ejecutar pruebas cada vez que se actualiza el código o verificar que no haya errores antes de publicar cambios.

2. KPI: Framework de Calidad de Datos
Desarrollé un tablero conceptual para medir la calidad de datos mediante indicadores clave (KPIs):
Integridad: % de registros completos vs. nulos.
Exactitud: % de teléfonos válidos (validados con regex).
Unicidad: % de registros duplicados.
Consistencia: Coherencia entre códigos de país y prefijos telefónicos.
Actualidad: Fecha de última actualización.
Implementación:
Python: Funciones con pandas para calcular completitud, unicidad y validación de formatos.
SQL: Consulta que agrupa teléfonos por código de país y verifica su validez.
Flujo de datos:
Fuentes (CSV, APIs).
Motor de calidad (aplica reglas y KPIs).
Catálogo de metadatos (almacena resultados).
Visualización en herramientas de BI.

3. Análisis de Rachas de Saldos
Este módulo carga información histórica de saldos mensuales desde un archivo Excel hacia una base de datos SQLite. Luego permite identificar comportamientos financieros consistentes de los clientes a lo largo del tiempo.
Carga de datos
El script revisa que el archivo Excel exista y tenga los datos esperados.
Crea la tabla historial_saldos en SQLite (si no existe).
Inserta los datos convertidos al formato adecuado.
Análisis de Rachas
Se clasifican los saldos mensuales en niveles (por ejemplo, bajo, medio, alto).
Se identifican rachas consecutivas de meses en las que un cliente se mantiene en un mismo nivel.
Se filtran rachas de al menos cierto número de meses (parámetro configurable).
Se selecciona la mejor racha por cliente: la más larga y reciente.
Aplicaciones del análisis
Permite detectar clientes VIP o estables.
Se puede usar para campañas de marketing o análisis financiero.
Útil para ver tendencias en el comportamiento del cliente a lo largo del tiempo.

4. Procesamiento de HTML con Imágenes Embebidas en Base64
Este script en Python es una herramienta inteligente para manejar imágenes dentro de archivos HTML. Su función principal es encontrar imágenes referenciadas en etiquetas <img>, convertirlas a un formato especial llamado Base64, y luego incrustar directamente esos datos en el código HTML. Al final, genera un nuevo archivo HTML con las imágenes ya "dentro" de él.
¿Para qué sirve?
Este procesador es increíblemente útil cuando:
Necesitas compartir HTMLs sin dependencias externas: Si envías un HTML por correo o lo usas en una aplicación sin conexión a internet, este script asegura que las imágenes se vean correctamente, ya que no dependen de que los archivos de imagen estén en una ruta específica.
Quieres garantizar la visualización: Elimina el problema de "imágenes rotas" que ocurre cuando los archivos de imagen no se encuentran.
Optimización para ciertos usos: Facilita el almacenamiento o la distribución de documentos HTML autocontenidos.
¿Cómo funciona?
Analiza directorios o archivos: Busca archivos HTML (.html o .htm) en las rutas que le indiques.
Busca imágenes: Dentro del código HTML, identifica las etiquetas <img> que referencian a un archivo de imagen (ignorando las que ya están embebidas).
Lee y convierte: Intenta leer esos archivos de imagen desde el disco y los transforma a formato Base64.
Reemplaza las rutas: Modifica la ruta src="..." de la imagen por su versión Base64 (por ejemplo, src="data:image/png;base64,...").
Guarda nuevos archivos: Genera una copia del archivo HTML original con un sufijo .procesado para indicar que ya contiene las imágenes incrustadas.
Estructura del proyecto
El código está organizado en clases y funciones para mantener un diseño limpio y reutilizable:
AnalizadorHtmlImagenes: Esta clase se encarga de analizar el contenido HTML y extraer las rutas de las imágenes. Es lo suficientemente inteligente como para ignorar las imágenes que ya están embebidas. Utiliza las capacidades estándar de análisis de HTML de Python.
ProcesadorHtml: Recibe una lista de rutas (ya sean archivos individuales o carpetas). Recorre estas rutas, busca los HTML, extrae las imágenes, las convierte, las incrusta y genera las nuevas copias de los archivos. Al final, produce un informe detallado con los resultados del procesamiento (éxitos o fallos).
Ejemplo de ejecución
El código incluye un bloque de ejemplo (if __name__ == "__main__") que te permite ver el procesador en acción:
Crea un entorno de prueba con algunos archivos HTML y una imagen.
Genera un archivo .png a partir de una codificación Base64.
Crea dos archivos HTML: uno que referencia una imagen válida y otro que referencia una imagen que no existe.
Ejecuta el proceso de conversión y muestra los resultados directamente en la consola.
