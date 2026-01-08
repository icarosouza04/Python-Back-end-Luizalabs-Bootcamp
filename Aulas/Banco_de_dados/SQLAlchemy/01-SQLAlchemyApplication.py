from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, func, inspect, select

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"
    # Atributos
    id = Column(Integer, primary_key = True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates = "user", cascade = "all, delete-orphan"
    )

    def __repr__ (self):
        return f"User (id = {self.id}, name = {self.name}, fullname = {self.fullname})"


class Address(Base):
    __tablename__ = "address"
    # Atributos
    id = Column(Integer, primary_key = True)
    email_address = Column(String(50), nullable = False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable = False)

    user = relationship(
        "User", back_populates = "address"
    )

    def __repr__ (self):
        return f"Address (id = {self.id}, email_address = {self.email_address})"
    

# Conexão com o banco de dados
engine = create_engine("sqlite://")

# Criando as classes como tabela no banco de dados
Base.metadata.create_all(engine)

# Investiga o esquema do banco de dados
insp_engine = inspect(engine)

print(insp_engine.has_table("user_account"))
print(insp_engine.get_table_names())
print(insp_engine.default_schema_name)


with Session(engine) as session:
    icaro = User(
        name = "Icaro",
        fullname = "Icaro Souza",
        address = [Address(email_address = "icarsouza04@email.com")]
    )

    eryck = User(
        name = "Eryck",
        fullname = "Eryck Mota",
        address = [Address(email_address = "eryckmota01@email.com"), 
                   Address(email_address = "eryckmartins01@email.com")]
    )

    larry = User(
        name = "Larry",
        fullname = "Larry Reis"
    )

    # Enviando para o banco de dados (persistência de dados)
    session.add_all([icaro, eryck, larry])
    session.commit()


# Recuperando usuários a partir de condição de filtragem
stmt_user = select(User).where(User.name.in_(["Icaro"]))

for user in session.scalars(stmt_user):
    print(user)

# Recuperando os endereços de Eryck
stmt_address = select(Address).where(Address.user_id.in_([2]))

for address in session.scalars(stmt_address):
    print(address)

# Recuperando os usuários de maneira ordenada em ordem descendente
stmt_order = select(User).order_by(User.fullname.desc())
for result in session.scalars(stmt_order):
    print(result)

stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
for result in session.scalars(stmt_join):
    print(result)

# Executando statement a partir da connection
connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
for result in results:
    print(result)

# Total de instâncias em User
stmt_count = select(func.count("*")).select_from(User)
for result in session.scalars(stmt_count):
    print(result)

# Encerrando a sessão
session.close()
