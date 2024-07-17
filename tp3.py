from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey,create_engine, insert, select;
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship;
from typing import List, Optional



engine=create_engine('sqlite+pysqlite:///:memory:',echo=True)
metadata_obj=MetaData()

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__="user_account"
    
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(30))
    fullname:Mapped[Optional[str]]
    
    adresses:Mapped[List["Address"]]=relationship
    
    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
    
class Address(Base):
    __tablename__="address"
    id:Mapped[int]=mapped_column(primary_key=True)
    email_adress:Mapped[str]
    user_id=mapped_column(ForeignKey("user_account.id"))
    
    user:Mapped[User]=relationship(back_populates="adresses")
    
    def __repr__(self)->str:
        return f"Adress(id={self.id!r}, email_adress={self.email_adress!r})"
    
Base.metadata.create_all(engine)


user_table=Table(
    "user_account",
    metadata_obj,
    Column("id",Integer,primary_key=True),
    Column("name",String(30)),
    Column("fullname",String),
)

adress_table=Table(
    "adress",
    metadata_obj,
    Column("id",Integer, primary_key=True),
    Column("user_id",ForeignKey("user_account.id"),nullable=False),
    Column("email_adress",String,nullable=False),
)

stmt=insert(user_table).values(name="spongebob",fullname="SpongeBob SquarePants")
compiled=stmt.compile()

with engine.connect() as conn:
    result=conn.execute(stmt)
    conn.execute(stmt)
    conn.commit()
    
print(result.inserted_primary_key)
print(insert(user_table))

with engine.connect() as conn:
    result=conn.execute(
        insert(user_table),
        [
            {"name":"Sandy","fullname":"Sandy Cheeks"},
            {"name":"Patrick","fullname":"Patrick Star"}
        ]
    )
    
select_stmt=select(user_table.c.id, user_table.c.name +"@aol.com")
insert_stmt=insert(adress_table).from_select(
    ["user_id","email_adress"], select_stmt
)
print(insert_stmt.returning(adress_table.c.id,adress_table.c.email_adress))