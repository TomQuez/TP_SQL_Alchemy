from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey,create_engine;


engine=create_engine('sqlite+pysqlite:///:memory:',echo=True)
metadata_obj=MetaData()
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


print(user_table.c.keys())
metadata_obj.create_all(engine)