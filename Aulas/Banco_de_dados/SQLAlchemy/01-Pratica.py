from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, inspect

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
        return f"Address (id = {self.id}, email = {self.email_address})"
    

# Conexão com o banco de dados
engine = create_engine("sqlite://")

# Criando as classes como tabela no banco de dados
Base.metadata.create_all(engine)

# Investiga o esquema do banco de dados
insp_engine = inspect(engine)

print(insp_engine.has_table("user_account"))
print(insp_engine.get_table_names())
print(insp_engine.default_schema_name)