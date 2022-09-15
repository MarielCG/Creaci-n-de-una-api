from fastapi import APIRouter
from config.db import conn 
from schema.user import Item_1, Item_2

user = APIRouter()

#Portada
@user.get("/", tags = ["Portada"])
def read_root():
    saludo = "BIENVENIDO AL PI"
    return saludo
       
# Resolucion de las preguntas 
# Cada subruta responde a las consultas solicitadas.

#PREGUNTA 1 Año con más carreras
@user.get('/pregunta_1', tags = ['Preguntas'], response_model = list[Item_1])
def get_Top1Carreras():
    carreras = conn.execute("""SELECT c.year as Año, count(c.IdRace) as Numero_carreras 
                               FROM races c 
                               GROUP BY c.year 
                               ORDER BY Numero_carreras desc 
                               LIMIT 1""")
    return carreras.fetchall() 


#PREGUNTA 2 Piloto con mayor cantidad de primeros puestos
@user.get('/pregunta_2', tags = ['Preguntas'], response_model = list[Item_2])
def get_Top1Piloto():
    pilotos = conn.execute("""SELECT r.IdDriver, concat(d.Forename, ' ',d.Surname) as Piloto, 
                              count(*) AS Cantidad_primeros_puestos 
                              FROM results r JOIN drivers d ON (r.IdDriver = d.IdDriver) 
                              WHERE r.position = 1 
                              GROUP BY r.IdDriver 
                              ORDER BY Cantidad_primeros_puestos desc
                              LIMIT 1""")
    return pilotos.fetchall()


# PREGUNTA 3: Nombre del circuito más corrido
@user.get('/pregunta_3', tags = ['Preguntas'])
def get_Top1CircuitoRecorrido():
    # recorrido = conn.execute ("WITH circuits_race AS (SELECT r.*, c.Name as Nombre_circuito FROM races r JOIN circuits c ON (r.IdCircuit = c.IdCircuit)) SELECT  cr.IdCircuit, cr.Nombre_circuito, sum(r.Laps) as Recorrido_total FROM results r LEFT JOIN circuits_race cr ON (r.IdRace = cr.IdRace) GROUP BY cr.Nombre_circuito ORDER BY Recorrido_total desc LIMIT 1")
    recorrido = conn.execute("""SELECT  cr.IdCircuit, cr.Nombre_circuito, sum(r.Laps) as Recorrido_total
                              FROM results r 
                              LEFT JOIN (SELECT r.*, c.Name as Nombre_circuito 
                                         FROM races r JOIN circuits c ON (r.IdCircuit = c.IdCircuit)) as cr
                              ON (r.IdRace = cr.IdRace) 
                              GROUP BY cr.Nombre_circuito 
                              ORDER BY Recorrido_total desc 
                              LIMIT 1""")
    return recorrido.fetchall()

# PREGUNTA 4:Piloto con mayor cantidad de puntos en total,
# cuyo constructor sea de nacionalidad sea American o British

@user.get('/pregunta_4', tags = ['Preguntas'])
def get_TopPilotoSegunConstructor():
    pilotos_constructor = conn.execute("""SELECT r.IdDriver, concat(d.Forename, ' ',d.Surname) as Piloto, 
                                          sum(r.Points) AS Puntos_totales 
                                          FROM results r LEFT JOIN drivers d ON (r.IdDriver = d.IdDriver) 
                                                         LEFT JOIN constructor c ON (r.IdConstructor 
                                                         = c.IdConstructor) 
                                          WHERE c.Nationality in ('American', 'British')
                                          GROUP BY r.IdDriver 
                                          ORDER BY Puntos_totales desc 
                                          LIMIT 1""")
    return pilotos_constructor.fetchall()   