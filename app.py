from fastapi import FastAPI
from route.user import user

app = FastAPI(title = 'Proyecto individual', descripcion = 'Analisis de carreras', version = '0.0.1', openapi_tags=[{'name': 'KPI', 'description': 'KPI routes'}])

app.include_router(user)