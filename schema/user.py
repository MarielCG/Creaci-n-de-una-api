from pydantic import BaseModel

# Se define el tipo de dato del resultado para cada sub-ruta

class Item_1(BaseModel):
    Año : int
    Numero_carreras : int

class Item_2(BaseModel):
    IdDriver: int
    Piloto : str
    Cantidad_primeros_puestos: int