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
