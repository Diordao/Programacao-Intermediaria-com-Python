"""
Trabalho - ORM com SQLAlchemy e Pandas
Criação de modelo ORM, conexão com SQLite, criação de tabelas,
população com dados do CSV e execução de consultas SQL e ORM.
"""

from sqlalchemy import (
    create_engine, Column, Integer, String, Float, Date, Enum as SAEnum, func, select, text
)
from sqlalchemy.orm import declarative_base, Session
import enum
import pandas as pd
import re
import os

# --------------------------
# Leitura inicial do CSV (para descobrir valores únicos)
# --------------------------
CSV_FILE = 'salaries.csv'
if not os.path.exists(CSV_FILE):
    raise FileNotFoundError(f"Arquivo '{CSV_FILE}' não encontrado no diretório atual.")

# Carrega o CSV (sem modificar colunas ainda)
df_raw = pd.read_csv(CSV_FILE)

# Normaliza nomes de colunas (minúsculas e underscores)
df_raw.columns = [col.strip().lower().replace(" ", "_") for col in df_raw.columns]

# Converte datas preliminarmente
df_raw['doj'] = pd.to_datetime(df_raw.get('doj'), errors='coerce')
df_raw['current_date'] = pd.to_datetime(df_raw.get('current_date'), errors='coerce')

# Extrai valores únicos para criar Enums
unique_sex = sorted(df_raw['sex'].dropna().astype(str).unique().tolist())
unique_designation = sorted(df_raw['designation'].dropna().astype(str).unique().tolist())
unique_unit = sorted(df_raw['unit'].dropna().astype(str).unique().tolist())

# --------------------------
# Helper: cria nomes válidos para membros Enum a partir de strings
# --------------------------
def make_member_name(s: str) -> str:
    # Remove caracteres não alfanuméricos substituindo por underscore
    s_clean = re.sub(r'\W+', '_', s.strip())
    # Se começar com dígito, prefixa underscore
    if re.match(r'^\d', s_clean):
        s_clean = f"_{s_clean}"
    # Evitar nomes vazios
    if not s_clean:
        s_clean = "VAL"
    return s_clean

# --------------------------
# Cria Enums dinamicamente com os valores reais do CSV
# Cada membro terá como value exatamente a string original do CSV
# --------------------------
def create_enum_class(enum_name: str, values_list):
    members = {}
    for v in values_list:
        key = make_member_name(v)
        # garantir que não exista chave duplicada
        i = 1
        base_key = key
        while key in members:
            i += 1
            key = f"{base_key}_{i}"
        members[key] = v
    return enum.Enum(enum_name, members)

SexEnum = create_enum_class("SexEnum", unique_sex)
DesignationEnum = create_enum_class("DesignationEnum", unique_designation)
UnitEnum = create_enum_class("UnitEnum", unique_unit)

# --------------------------
# Q2 - Modelagem ORM (definir Base e classe usando os Enums gerados)
# --------------------------
Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    # Usar values_callable para garantir que o SQL armazene/recupere os *values* do Enum
    sex = Column(SAEnum(SexEnum, values_callable=lambda obj: [e.value for e in obj], native_enum=False))
    doj = Column(Date)
    current_date = Column(Date)
    designation = Column(SAEnum(DesignationEnum, values_callable=lambda obj: [e.value for e in obj], native_enum=False))
    age = Column(Integer)
    salary = Column(Float)
    unit = Column(SAEnum(UnitEnum, values_callable=lambda obj: [e.value for e in obj], native_enum=False))
    leaves_used = Column(Integer)
    leaves_remaining = Column(Integer)
    ratings = Column(Float)
    past_exp = Column(Float)

# --------------------------
# Q3 - Conexão com o banco
# --------------------------
engine = create_engine('sqlite:///salarios.db', future=True)
print("✅ Conexão com o banco criada com sucesso!")

# --------------------------
# Para evitar inconsistências anteriores: remover tabela antiga (se existir)
# e criar novamente com os tipos atuais (incluindo enums dinamicamente gerados).
# --------------------------
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
print("✅ Tabelas criadas (ou recriadas) com sucesso!")

# --------------------------
# Q5 - Populando com CSV (usamos df_raw já carregado)
# Observação: pandas.to_sql irá inserir strings nas colunas enum no SQLite;
# desde que os valores strings coincidam com os Enum.value, SQLAlchemy consegue mapear depois.
# --------------------------

# Antes de inserir, garantimos que as colunas existem e estão no formato correto
df = df_raw.copy()

# As colunas do CSV devem ter exatamente os nomes usados no modelo; garantir
expected_cols = {
    'first_name', 'last_name', 'sex', 'doj', 'current_date', 'designation',
    'age', 'salary', 'unit', 'leaves_used', 'leaves_remaining', 'ratings', 'past_exp'
}
missing = expected_cols - set(df.columns)
if missing:
    raise RuntimeError(f"Colunas esperadas faltando no CSV: {missing}")

# Convert types (novamente, para garantir)
df['age'] = pd.to_numeric(df['age'], errors='coerce').astype('Int64')
df['salary'] = pd.to_numeric(df['salary'], errors='coerce').astype(float)
df['leaves_used'] = pd.to_numeric(df['leaves_used'], errors='coerce').astype('Int64')
df['leaves_remaining'] = pd.to_numeric(df['leaves_remaining'], errors='coerce').astype('Int64')
df['ratings'] = pd.to_numeric(df['ratings'], errors='coerce').astype(float)
df['past_exp'] = pd.to_numeric(df['past_exp'], errors='coerce').astype(float)

# Insere no banco (replace/append: como recriamos a tabela, usamos append)
df.to_sql('employees', con=engine, if_exists='append', index=False)
print("✅ Dados do CSV inseridos com sucesso no banco!")

# --------------------------
# Q6 - Consultas SQL e ORM
# --------------------------
print("\n=========================")
print(" Q6 - Consultas SQL e ORM ")
print("=========================\n")

# --- 6.1 - Query SQL direta (usando text)
print("🔹 Consulta direta via SQLAlchemy Engine:")
with engine.connect() as conn:
    q = text("""
        SELECT designation,
               MIN(salary/12) AS min_mensal,
               MAX(salary/12) AS max_mensal,
               AVG(salary/12) AS media_mensal
        FROM employees
        GROUP BY designation
        ORDER BY designation;
    """)
    result = conn.execute(q)
    rows = result.fetchall()
    for r in rows:
        print(r)

# --- 6.2 - Query via Pandas
print("\n🔹 Consulta via Pandas:")
query = """
    SELECT designation,
           MIN(salary/12) AS min_mensal,
           MAX(salary/12) AS max_mensal,
           AVG(salary/12) AS media_mensal
    FROM employees
    GROUP BY designation
    ORDER BY designation;
"""
df_query = pd.read_sql_query(query, engine)
print(df_query)

# --- 6.3 - Query via ORM (SQLAlchemy) usando Session
print("\n🔹 Consulta via ORM (Session):")
with Session(engine) as session:
    stmt = select(
        Employee.designation,
        func.min(Employee.salary / 12).label("min_mensal"),
        func.max(Employee.salary / 12).label("max_mensal"),
        func.avg(Employee.salary / 12).label("media_mensal"),
    ).group_by(Employee.designation).order_by(Employee.designation)

    result = session.execute(stmt).all()
    for row in result:
        print(row)

print("\n✅ Fim da execução.")