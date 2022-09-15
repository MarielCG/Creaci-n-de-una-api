from sqlalchemy import create_engine, MetaData

#engine = create_engine('mysql+pymysql://root:Clave1601**@localhost:3306/lab_individual')
engine = create_engine('mysql+pymysql://sql10519779:GCQw6lAdZU@sql10.freemysqlhosting.net:3306/sql10519779')

meta = MetaData()

conn = engine.connect()
