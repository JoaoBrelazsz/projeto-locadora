import psycopg2
import os
import random
from datetime import datetime

DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

for i in range(50):
    nome = f"Cliente_{random.randint(1,10000)}"
    estado = random.choice(["SP", "RJ", "MG", "BA"])
    cidade = "Cidade_" + str(random.randint(1,100))
    score = round(random.uniform(5,10),1)

    cursor.execute("""
    INSERT INTO "CLIENTES" (nome, estado, cidade, score, data_cadastro)
    VALUES (%s, %s, %s, %s, CURRENT_DATE)
    """, (nome, estado, cidade, score))

conn.commit()

print("50 clientes inseridos!", datetime.now())
