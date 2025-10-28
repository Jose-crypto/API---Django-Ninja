from ninja import ModelSchema , FilterSchema, Field
from typing import Optional
from .models import Hospital

# Schema class of pydantics used to validate data reques (validar datos de entrada), and format data of response(validar datos de salida )



# schema para lectura de datos
class HospitalSchema(ModelSchema):
    class Config:
        model = Hospital
        model_fields = '__all__'


#schema para busqueda segun la ciudad y el nombre del hospital
class HospitalFilterSchema(FilterSchema):
    city_town: Optional[str] = None
    hospital_name: Optional[str] = None