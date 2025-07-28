from faker import Faker
import pandas as pd
import random

fake = Faker()

data = []
for i in range(1000):
    nombre = fake.first_name()
    apellido = fake.last_name()
    numero_telefono = fake.phone_number()
    pais = random.choice(['+57', '+1', '+54', '+52'])  # Colombia, EE.UU., Argentina, México

    data.append({
        'id': 1000 + i,
        'Nombre': nombre,
        'Apellido': apellido,
        'Numero_Telefono': numero_telefono,
        'Codigo_pais': pais
    })

df = pd.DataFrame(data)
df.to_csv('Dataset_clientes.csv', index=False)

print("✅ Dataset generado con éxito.")
