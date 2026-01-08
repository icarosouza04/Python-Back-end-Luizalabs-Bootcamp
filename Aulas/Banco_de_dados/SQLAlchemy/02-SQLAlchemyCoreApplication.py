from sqlalchemy import Column, ForeignKey, Integer, String, MetaData, Table, create_engine, text

engine = create_engine("sqlite://")

metadata_obj = MetaData()

user = Table(
    "user",
    metadata_obj,
    Column("user_id", Integer, primary_key = True),
    Column("user_name", String(50), nullable = False),
    Column("email_address", String(50)),
    Column("nickname", String(30))
)

# Inserindo informações na tabela "user"
sql_insert = text("insert into user values (1, 'Icaro', 'icarosouza04@email.com', 'icro')")
engine.execute(sql_insert)


user_prefs = Table(
    "users_prefs",
    metadata_obj,
    Column("pref_id", Integer, primary_key = True),
    Column("user_id", Integer, ForeignKey("user.user_id"), nullable = False),
    Column("pref_name", String(50), nullable = False),
    Column("pref_value", String(100))
)

print(metadata_obj.tables)

for table in metadata_obj.sorted_tables:
    print(table)

# Informações da tabela "users_prefs"
print(user_prefs.primary_key)
print(user_prefs.constraints)

metadata_obj.create_all(engine)

metadata_bd_obj = MetaData()

financial_info = Table(
    "financial_info",
    metadata_bd_obj,
    Column("id", Integer, primary_key = True),
    Column("value", String(100), nullable = False)
)

# Informações da tabela "financial_info"
print(financial_info.primary_key)
print(financial_info.constraints)

# Executando statement "sql"
sql = text("select * from user")
result = engine.execute(sql)

for row in result:
    print(row)
