from fastapi import APIRouter
from config.db import conn , engine
from sqlalchemy import select
import pandas as pd
import json 

user = APIRouter()

#Portada
@user.get("/")
def read_root():
    saludo = "BIENVENIDO"
    return saludo

# Cargar el dataset

@user.get('/dataset', tags = ['Carga de DataSet'])
def get_CargaDataSet():

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

    cargado = 'Dataset cargado'
    return cargado

    
# Resolucion de las preguntas 

@user.get('/pregunta_1', tags = ['Preguntas'])
def get_Top5Carreras():
    carreras = conn.execute("SELECT c.year as Año, count(c.IdRace) as Numero_carreras FROM races c group by c.year order by Numero_carreras desc limit 1")
    return carreras.fetchall()

@user.get('/pregunta_2', tags = ['Preguntas'])
def get_Top1Piloto():
    pilotos = conn.execute("SELECT r.IdDriver, concat(d.Forename, ' ',d.Surname) as Piloto, count(*) AS Cantidad_primeros_puestos FROM results r JOIN drivers d ON (r.IdDriver = d.IdDriver) WHERE r.position = 1 GROUP BY r.IdDriver ORDER BY Cantidad_primeros_puestos desc LIMIT 1")
    return pilotos.fetchall()

@user.get('/pregunta_3', tags = ['Preguntas'])
def get_Top5Recorrido():
    # recorrido = conn.execute ("WITH circuits_race AS (SELECT r.*, c.Name as Nombre_circuito FROM races r JOIN circuits c ON (r.IdCircuit = c.IdCircuit)) SELECT  cr.IdCircuit, cr.Nombre_circuito, sum(r.Laps) as Recorrido_total FROM results r LEFT JOIN circuits_race cr ON (r.IdRace = cr.IdRace) GROUP BY cr.Nombre_circuito ORDER BY Recorrido_total desc LIMIT 1")
    recorrido = conn.execute("SELECT  cr.IdCircuit, cr.Nombre_circuito, sum(r.Laps) as Recorrido_total FROM results r LEFT JOIN (SELECT r.*, c.Name as Nombre_circuito FROM races r JOIN circuits c ON (r.IdCircuit = c.IdCircuit)) as cr ON (r.IdRace = cr.IdRace) GROUP BY cr.Nombre_circuito ORDER BY Recorrido_total desc LIMIT 1")
    return recorrido.fetchall()

    
@user.get('/pregunta_4', tags = ['Preguntas'])
def get_TopPilotoSegunConstructor():
    pilotos_constructor = conn.execute("SELECT r.IdDriver, concat(d.Forename, ' ',d.Surname) as Piloto, sum(r.Points) AS Puntos_totales FROM results r LEFT JOIN drivers d ON (r.IdDriver = d.IdDriver) LEFT JOIN constructor c ON (r.IdConstructor = c.IdConstructor) WHERE c.Nationality in ('American', 'British') GROUP BY r.IdDriver ORDER BY Puntos_totales desc LIMIT 1")
    return pilotos_constructor.fetchall()   