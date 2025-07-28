import pandas as pd
import phonenumbers

def es_telefono_valido(numero: str) -> bool:
    try:
        parsed = phonenumbers.parse(numero, None)
        return phonenumbers.is_valid_number(parsed)
    except Exception:
        return False

df = pd.read_csv('Dataset_clientes.csv')
df['Es_valido'] = df['Numero_Telefono'].apply(es_telefono_valido)
df_validos = df[df['Es_valido']]
df_validos.to_csv('Dataset_clientes_validado.csv', index=False)

print(f" Validación completada: {len(df_validos)} registros válidos de {len(df)}.")
