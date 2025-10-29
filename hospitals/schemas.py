from ninja import ModelSchema, FilterSchema, Field
from typing import Optional
from .models import Hospital

# Schema class of pydantics used to validate data reques (validar datos de entrada), and format data of response(validar datos de salida )


# schema para lectura de datos
class HospitalSchema(ModelSchema):
    class Config:
        model = Hospital
        model_fields = '__all__'


# schema para busqueda segun la ciudad y el nombre del hospital (Filter es case sensitive)
class HospitalFilterSchema(FilterSchema):
    city_town: Optional[str] = None
    hospital_name: Optional[str] = Field(None, q='hospital_name__startswith')


# schema para busqueda segun el nombre del hospital (Filter es case sensitive)
class HospitalNameSchema(FilterSchema):
    hospital_name: Optional[str] = None 

#schema para busqueda segun el district
class HospitalDistrictSchema(FilterSchema):
    district : Optional[str] = None
    
    
#schema para busqueda segun el namewebsite
class HospiltaWebsiteSchema(FilterSchema):
    website : Optional[str] = None