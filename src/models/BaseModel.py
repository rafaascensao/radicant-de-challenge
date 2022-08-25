from peewee import SqliteDatabase, Model

psql_db = SqliteDatabase('db/radicant_challenge.db')

class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = psql_db