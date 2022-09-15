
# **Proyecto individual**


## **Creación del entorno virtual**
Se crea el entorno virtual en `ANACONDA` con el nombre de 

  
![img](https://imgur.com/lsZKehf.png)

## **Importacion de los datos y normalizacion**

###  - *IMPORTACION DE LOS DATOS*

La importacion de los datos se realiza a través de un SCRIPT en PYTHON ***Carga_DataSet_sql.py***.

Se importa a la BD (base de datos) *lab_individual* creada en MYSQL (Workbench). 

Para conectar el script de Python a MYSQL usamos la libreria `sqlalchemy `

###  - *NORMALIZACION DE LA BD*

En el archivo ***Normalizacion.sql*** se encuentra el codigo de la normalizacion. 

A continuacion veremos el diagrama de las relaciones de las tablas.

![img](https://i.imgur.com/c7jFvFG.png)


## **CREACION DE LA API**

1. Primero realizacon la installacion de `FAST API` y `UVICORN`
Nota: En ***requirements.txt*** se encuentran todas las dependencias necesarioas para este proyecto

2. La creacion de los 4 scripts para el desarrollo de la API, ordenanda en carpetas.

    - **app.py**       : Contiene la inicializacion de la API
    - **db.py**         : Contiene la conxion de la API con nuestra BD  
    - **user.py (route)**: Contiene las diferentes subrutas de nuestra API
    - **user.py (schema)**: Contiene el esquema de las respuestas de las sub rutas.

    2.1 En el script **user.py (route)**, se tiene 4 sub rutas que muestran las respuestas para las cuatro consultas solicitadas.

    
3. Con los script realizados, ahora se prueba la funcionalidad de la API a traves de `uvicorn app:app --reload`

A continuacion se presenta imagenes de la API:

- FAST API - DOCUMENTACION

![img](https://imgur.com/UAsILGq.png)

- FAST API - PREGUNTA 1: Año con más carreras

![img](https://imgur.com/QIXDgFB.jpg)


- FAST API - PREGUNTA 2: Piloto con mayor cantidad de primeros puestos
![img](https://imgur.com/zLQRf2s.jpg)


- FAST API - PREGUNTA 3: Nombre del circuito más corrido
![img](https://i.imgur.com/AauwhYN.jpg)

- FAST API - PREGUNTA 4: Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British


![img](https://i.imgur.com/KKYwUpM.jpg)

----------------------------------------------------------------------------------------------------------------

