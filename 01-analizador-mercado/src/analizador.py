import pandas as pd

# Creamos una lista de diccionarios (como si fueran vacantes de trabajo)
vacantes = [
    {"puesto": "Dev Python", "salario": 2500, "moneda": "USD"},
    {"puesto": "Dev Java", "salario": 2200, "moneda": "USD"},
    {"puesto": "Data Scientist", "salario": 3000, "moneda": "USD"},
    {"puesto": "Dev fullstak", "salario": 2000, "moneda": "USD"},
    {"puesto": "Dev backend", "salario": 4200, "moneda": "USD"},
    {"puesto": "Dev frontend", "salario": 4000, "moneda": "USD"},
    {"puesto": "dev python ", "salario": 2500}, # Espacios extra
    {"puesto": "Data Scientist", "salario": None}, # Dato faltante
    {"puesto": "DEV PYTHON", "salario": 3100}, # Mayúsculas inconsistentes
    {"puesto": "Backend Dev", "salario": 2800},
    {"puesto": "dev python", "salario": "3200"}, # Salario como texto
]

    # Limpiar datos: eliminar espacios, convertir a mayúsculas, manejar nulos
def limpiar_y_analizar(datos):
    df = pd.DataFrame(datos)
   # --- LIMPIEZA DE DATOS ---
    # Convertimos salarios a números, los errores se vuelven NaN (Not a Number)
    df['salario'] = pd.to_numeric(df['salario'], errors='coerce')
    
    # Eliminamos filas que no tengan salario (datos incompletos)
    df = df.dropna(subset=['salario'])
    
    # Estandarizamos los nombres de los puestos (Todo a minúsculas y sin espacios extra)
    df['puesto'] = df['puesto'].str.lower().str.strip()
    
    # --- ANÁLISIS ---
    # Filtramos solo vacantes de Python
    python_df = df[df['puesto'].str.contains('python')]
    promedio_python = python_df['salario'].mean()
    
    return df, promedio_python

# Ejecución
df_limpio, promedio = limpiar_y_analizar(vacantes)

print("--- DATOS LIMPIOS Y PROCESADOS ---")
print(df_limpio)
print(f"\nPromedio Salarial Python: ${promedio:.2f} USD")

# --- PERSISTENCIA PROFESIONAL ---
df_limpio.to_csv("reporte_limpio.csv", index=False)
print("\n✅ Archivo 'reporte_limpio.csv' generado con éxito.")

# Convertimos la lista en un DataFrame (una tabla poderosa de Pandas)
df = pd.DataFrame(vacantes)

# Filtrar vacantes de alto nivel
print("\n--- Vacantes de Alto Nivel (> 2800) ---")
for vacante in vacantes:
    if vacante["salario"] > 2800:
        print(f"¡Oportunidad Pro!: {vacante['puesto']} paga {vacante['salario']}")
print("--- REPORTE DE VACANTES 2026 ---")
print(df)
print("\nEl salario promedio es:", df["salario"].mean())

# Definimos el nombre del archivo
nombre_archivo = "reporte_empleabilidad.txt"

# Usamos 'w' para indicar que vamos a escribir (write)
with open(nombre_archivo, "w", encoding="utf-8") as archivo:
    archivo.write("========================================\n")
    archivo.write("   REPORTE DE VACANTES PYTHON 2026\n")
    archivo.write("========================================\n\n")
    
    # Escribimos el promedio que calculamos con Pandas
    archivo.write(f"Salario Promedio del Mercado: {df['salario'].mean()} USD\n\n")
    
    archivo.write("Detalle de puestos analizados:\n")
    for v in vacantes:
        archivo.write(f"- {v['puesto']}: ${v['salario']}\n")

print(f"✅ ¡Éxito! El archivo '{nombre_archivo}' se ha creado en tu carpeta.")