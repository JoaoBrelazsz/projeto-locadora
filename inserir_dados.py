import psycopg2
import os
import random

DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

nome = f"Cliente_{random.randint(1,1000)}"

cursor.execute("""
INSERT INTO "CLIENTES" (nome, estado, cidade, score, data_cadastro)
VALUES (%s, %s, %s, %s, CURRENT_DATE)
""", (nome, "SP", "São Paulo", 8.0))

conn.commit()

print("Inserido!")
