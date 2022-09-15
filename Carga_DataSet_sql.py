from sqlalchemy import create_engine
import pandas as pd
import json 

engine = create_engine('mysql+pymysql://root:Clave1601**@localhost:3306/lab_individual')

#Motor para conectar con una BD en la nube 
# engine = create_engine('mysql+pymysql://sql10519779:GCQw6lAdZU@sql10.freemysqlhosting.net:3306/sql10519779')


circuits_csv = pd.read_csv('./Datasets/circuits.csv')
circuits_csv.replace('\\N', '')
circuits_csv.to_sql('circuits', con = engine, if_exists = 'replace')
    
races_csv = pd.read_csv('./Datasets/races.csv')
races_csv.to_sql('races', con = engine, if_exists = 'replace')


lap_times_split_1_csv = pd.read_csv('./Datasets/lap_times/lap_times_split_1.csv')
lap_times_split_2_csv = pd.read_csv('./Datasets/lap_times/lap_times_split_2.csv')
lap_times_split_3_csv = pd.read_csv('./Datasets/lap_times/lap_times_split_3.csv')
lap_times_split_4_csv = pd.read_csv('./Datasets/lap_times/lap_times_split_4.csv')
lap_times_split_5_csv = pd.read_csv('./Datasets/lap_times/lap_times_split_5.csv')
lap_times_split = pd.concat([lap_times_split_1_csv, lap_times_split_2_csv, lap_times_split_3_csv, lap_times_split_4_csv, lap_times_split_5_csv])
lap_times_split.to_sql('lap_times_split', con = engine, if_exists = 'replace')


constructors_jsontodicc = [json.loads(line) for line in open('./Datasets/constructors.json', 'r')]
constructors = pd.json_normalize(constructors_jsontodicc)
constructors.to_sql('constructor', con = engine, if_exists = 'replace')


drivers_jsontodicc = [json.loads(line) for line in open('./Datasets/drivers.json', 'r')]
drivers = pd.json_normalize(drivers_jsontodicc)
drivers = drivers.replace('\\N', '')
drivers.to_sql('drivers', con = engine, if_exists = 'replace')


pit_stops_json = pd.read_json('./Datasets/pit_stops.json' )
pit_stops_json.to_sql('pit_stops', con = engine, if_exists = 'replace')


results_json = pd.read_json('./Datasets/results.json', lines=True )
results_json = results_json.replace('\\N', '')
results_json.to_sql('results', con = engine, if_exists = 'replace')


qualifying1_json = pd.read_json('./Datasets/Qualifying/qualifying_split_1.json')
qualifying2_json = pd.read_json('./Datasets/Qualifying/qualifying_split_2.json') 
qualifying_json = pd.concat([qualifying1_json,qualifying2_json])
qualifying_json = qualifying_json.replace('\\N', '')
qualifying_json.to_sql('qualifying', con = engine, if_exists = 'replace')




