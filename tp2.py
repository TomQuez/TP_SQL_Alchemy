from sqlalchemy import MetaData, create_engine, Table, Column, Integer, String;


#engine=create_engine('sqlite+pysqlite:///:memory:',echo=True)
metadata_obj=MetaData()
user_table=Table(
    "user_account",
    metadata_obj,
    Column("id",Integer,primary_key=True),
    Column("name",String(30)),
    Column("fullname",String),
)


print(user_table.c.keys())