from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://root:Clave1601**@localhost:3306/lab_individual_2')

meta = MetaData()

conn = engine.connect()