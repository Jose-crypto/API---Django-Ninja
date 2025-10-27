from ninja import ModelSchema , FilterSchema
from .models import Hospital

# Schema class of pydantics used to validate data reques (validar datos de entrada), and format data of response(validar datos de salida )



# schema para lectura de datos
class HospitalSchema(ModelSchema):
    class Config:
        model = Hospital
        model_fields = '__all__'


#schema para busqueda 